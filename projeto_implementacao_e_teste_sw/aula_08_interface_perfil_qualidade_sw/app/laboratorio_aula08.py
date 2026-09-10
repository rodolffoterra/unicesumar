import hashlib
import os
import sys
from pathlib import Path

import requests
import streamlit as st
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

load_dotenv(ROOT_DIR / ".env")

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "techport123")

st.set_page_config(
    page_title="TechPort - Aula 08",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
      .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
      [data-testid="stMetric"] {background:#f7fbff; border:1px solid #d9eafa; padding:14px; border-radius:14px;}
      .techport-title {font-size:2rem; font-weight:800; color:#0b2f5b; margin-bottom:.2rem;}
      .techport-sub {color:#4a647f; margin-bottom:1rem;}
      .role-card {padding:14px 16px; border-radius:12px; background:#f7fbff; border:1px solid #d8e8f7;}
      .status-box {padding:10px 12px; border-radius:10px; background:#f4f8fc; border-left:4px solid #2389e8; margin:5px 0;}
      .lab-note {padding:12px 14px; border-radius:10px; background:#fff8dd; border:1px solid #f2d66b;}
    </style>
    """,
    unsafe_allow_html=True,
)


def api(method: str, path: str, **kwargs):
    url = f"{API_BASE_URL}{path}"
    try:
        response = requests.request(method, url, timeout=8, **kwargs)
    except requests.RequestException as exc:
        st.error("Não foi possível acessar a API do TechPort.")
        st.caption(f"Endereço configurado: {API_BASE_URL}")
        st.code("python -m uvicorn app.api.fastapi_app:app --reload")
        raise RuntimeError(str(exc)) from exc

    if response.status_code >= 400:
        try:
            detalhe = response.json().get("detail", response.text)
        except Exception:
            detalhe = response.text
        raise RuntimeError(f"API {response.status_code}: {detalhe}")

    if not response.content:
        return None
    return response.json()


def api_segura(method: str, path: str, **kwargs):
    try:
        return api(method, path, **kwargs)
    except RuntimeError as exc:
        st.error(str(exc))
        return None


def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def norm_status(status):
    return str(status or "").strip().lower().replace(" ", "_")


def status_legivel(status):
    mapa = {
        "aberto": "Aberto",
        "atribuido": "Atribuído",
        "em_atendimento": "Em atendimento",
        "resolvido": "Resolvido",
        "finalizado": "Finalizado",
        "aguardando": "Aguardando",
    }
    valor = norm_status(status)
    return mapa.get(valor, str(status or "-").replace("_", " ").title())


def cabecalho(titulo, subtitulo):
    st.markdown(f'<div class="techport-title">🎧 TechPort — {titulo}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="techport-sub">{subtitulo}</div>', unsafe_allow_html=True)


def tabela_chamados(chamados, key_prefix="tabela"):
    if not chamados:
        st.info("Nenhum chamado encontrado.")
        return
    dados = []
    for c in chamados:
        dados.append(
            {
                "ID": c.get("id"),
                "Título": c.get("titulo"),
                "Categoria": c.get("categoria"),
                "Prioridade": c.get("prioridade"),
                "Status": status_legivel(c.get("status")),
                "Usuário": c.get("usuario_id"),
                "Técnico": c.get("tecnico_id") or "—",
                "Abertura": str(c.get("data_abertura", ""))[:19],
            }
        )
    st.dataframe(dados, use_container_width=True, hide_index=True)


def selecionar_usuario():
    usuarios = api_segura("GET", "/usuarios") or []
    ativos = [u for u in usuarios if u.get("ativo")]
    if not ativos:
        st.warning("Nenhum usuário ativo cadastrado. Crie um novo usuário.")
        return None
    opcoes = {f"#{u['id']} — {u['nome']} ({u['email']})": u for u in ativos}
    escolha = st.selectbox("Escolha um usuário existente", list(opcoes.keys()))
    return opcoes[escolha]


def selecionar_tecnico():
    tecnicos = api_segura("GET", "/tecnicos") or []
    ativos = [t for t in tecnicos if t.get("ativo")]
    if not ativos:
        st.warning("Nenhum técnico ativo cadastrado. Crie um novo técnico.")
        return None
    opcoes = {f"#{t['id']} — {t['nome']} | {t['especialidade']} | {t['nivel']}": t for t in ativos}
    escolha = st.selectbox("Escolha um técnico existente", list(opcoes.keys()))
    return opcoes[escolha]


# ==========================================================
# SIDEBAR - NAVEGAÇÃO E DEMONSTRAÇÃO
# ==========================================================
with st.sidebar:
    st.markdown("## 🎧 TechPort")
    st.caption("Laboratório — Interfaces, Perfis e Qualidade")

    st.markdown("### Perfil da demonstração")
    perfil = st.radio(
        "Selecione a interface",
        ["👤 Usuário", "🛠️ Técnico", "⚙️ Administrador"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("### Exemplos para a aula")
    st.markdown("**Usuário:** selecione um usuário existente ou cadastre um novo.")
    st.markdown("**Técnico:** selecione um técnico existente ou cadastre um novo.")
    st.markdown("**Administrador:**")
    st.code(f"Usuário: {ADMIN_USER}\nSenha: {ADMIN_PASSWORD}")
    st.caption("Credenciais didáticas. Em produção, não exibir senhas na interface.")

    st.divider()
    st.markdown("### Arquitetura")
    st.caption("Streamlit → FastAPI → Service → Repository → MySQL")
    st.caption(f"API: {API_BASE_URL}")


# ==========================================================
# TESTE DE SAÚDE DA API
# ==========================================================
try:
    health = api("GET", "/")
    api_online = health.get("status") == "online"
except Exception:
    api_online = False

if not api_online:
    st.error("A API não está disponível. Abra outro terminal e inicie a FastAPI.")
    st.code("python -m uvicorn app.api.fastapi_app:app --reload")
    st.stop()


# ==========================================================
# PERFIL USUÁRIO
# ==========================================================
if perfil == "👤 Usuário":
    cabecalho("Interface do Usuário", "Abrir chamados, acompanhar status, comentar e consultar histórico.")

    tab_existente, tab_novo = st.tabs(["Entrar com usuário existente", "Criar novo usuário"])

    with tab_existente:
        usuario = selecionar_usuario()
        if usuario and st.button("Entrar como este usuário", type="primary", key="entrar_usuario"):
            st.session_state.usuario_logado = usuario

    with tab_novo:
        with st.form("form_novo_usuario"):
            nome = st.text_input("Nome")
            email = st.text_input("E-mail")
            senha = st.text_input("Senha do laboratório", type="password")
            criar = st.form_submit_button("Cadastrar usuário", type="primary")
        if criar:
            if not nome or not email or not senha:
                st.warning("Preencha nome, e-mail e senha.")
            else:
                payload = {
                    "nome": nome,
                    "email": email,
                    "senha_hash": hash_senha(senha),
                    "perfil": "cliente",
                    "ativo": True,
                }
                resp = api_segura("POST", "/usuarios", json=payload)
                if resp:
                    st.success(f"Usuário cadastrado com sucesso. ID #{resp['id']}")
                    novo = api_segura("GET", f"/usuarios/{resp['id']}")
                    if novo:
                        st.session_state.usuario_logado = novo

    usuario = st.session_state.get("usuario_logado")
    if usuario:
        st.divider()
        st.markdown(f"### Olá, {usuario['nome']} 👋")
        chamados = api_segura("GET", "/chamados") or []
        meus = [c for c in chamados if c.get("usuario_id") == usuario["id"]]

        c1, c2, c3 = st.columns(3)
        c1.metric("Abertos", sum(norm_status(c.get("status")) == "aberto" for c in meus))
        c2.metric("Em atendimento", sum(norm_status(c.get("status")) == "em_atendimento" for c in meus))
        c3.metric("Finalizados", sum(norm_status(c.get("status")) in {"finalizado", "resolvido"} for c in meus))

        sub1, sub2 = st.tabs(["Meus chamados", "➕ Novo chamado"])
        with sub1:
            tabela_chamados(meus, "usuario")
            if meus:
                ids = [c["id"] for c in meus]
                chamado_id = st.selectbox("Ver detalhes do chamado", ids, format_func=lambda x: f"Chamado #{x}")
                chamado = next(c for c in meus if c["id"] == chamado_id)
                st.markdown(f"**{chamado['titulo']}** — {status_legivel(chamado['status'])}")
                st.write(chamado["descricao"])

                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("#### Comentários")
                    comentarios = api_segura("GET", f"/chamados/{chamado_id}/comentarios") or []
                    for item in comentarios[-10:]:
                        st.markdown(
                            f"<div class='status-box'><b>{item['autor_tipo'].title()}</b>: {item['comentario']}<br><small>{item['data_comentario']}</small></div>",
                            unsafe_allow_html=True,
                        )
                    with st.form(f"comentario_usuario_{chamado_id}"):
                        texto = st.text_area("Adicionar informação ao chamado")
                        enviar_coment = st.form_submit_button("Enviar comentário")
                    if enviar_coment and texto.strip():
                        payload = {
                            "autor_tipo": "usuario",
                            "usuario_id": usuario["id"],
                            "tecnico_id": None,
                            "comentario": texto.strip(),
                            "visibilidade": "publico",
                        }
                        if api_segura("POST", f"/chamados/{chamado_id}/comentarios", json=payload):
                            st.success("Comentário registrado.")
                            st.rerun()

                with col_b:
                    st.markdown("#### Histórico")
                    hist = api_segura("GET", f"/chamados/{chamado_id}/historico") or []
                    if not hist:
                        st.caption("Ainda não há eventos de histórico para este chamado.")
                    for item in hist[-10:]:
                        anterior = item.get("status_anterior") or "—"
                        novo = item.get("status_novo") or "—"
                        st.markdown(
                            f"<div class='status-box'><b>{item['evento']}</b><br>{anterior} → {novo}<br><small>{item['data_evento']}</small></div>",
                            unsafe_allow_html=True,
                        )

        with sub2:
            with st.form("novo_chamado"):
                titulo = st.text_input("Título", placeholder="Ex.: Notebook não inicializa")
                descricao = st.text_area("Descrição", placeholder="Descreva o problema com clareza.")
                categoria = st.selectbox("Categoria", ["Hardware", "Software", "Acesso", "Rede", "Infraestrutura", "Outros"])
                prioridade = st.selectbox("Prioridade", ["BAIXA", "MÉDIA", "ALTA", "CRÍTICA"])
                enviar = st.form_submit_button("ABRIR CHAMADO", type="primary")
            if enviar:
                payload = {
                    "usuario_id": usuario["id"],
                    "tecnico_id": None,
                    "titulo": titulo,
                    "descricao": descricao,
                    "categoria": categoria,
                    "prioridade": prioridade,
                    "status": "aberto",
                    "canal_abertura": "streamlit",
                }
                resp = api_segura("POST", "/chamados", json=payload)
                if resp:
                    st.success(f"Chamado #{resp['id']} aberto com sucesso.")
                    st.info("Agora troque para o perfil Técnico e localize este mesmo chamado.")


# ==========================================================
# PERFIL TÉCNICO
# ==========================================================
elif perfil == "🛠️ Técnico":
    cabecalho("Interface do Técnico", "Prioridade + Informação + Ação para atender os chamados.")

    tab_existente, tab_novo = st.tabs(["Entrar com técnico existente", "Criar novo técnico"])

    with tab_existente:
        tecnico = selecionar_tecnico()
        if tecnico and st.button("Entrar como este técnico", type="primary", key="entrar_tecnico"):
            st.session_state.tecnico_logado = tecnico

    with tab_novo:
        with st.form("form_novo_tecnico"):
            nome = st.text_input("Nome do técnico")
            email = st.text_input("E-mail do técnico")
            especialidade = st.selectbox("Especialidade", ["Hardware", "Software", "Redes", "Acesso", "Infraestrutura", "Geral"])
            nivel = st.selectbox("Nível", ["júnior", "pleno", "sênior"])
            criar = st.form_submit_button("Cadastrar técnico", type="primary")
        if criar:
            payload = {
                "nome": nome,
                "email": email,
                "especialidade": especialidade,
                "nivel": nivel,
                "disponivel": True,
                "ativo": True,
            }
            resp = api_segura("POST", "/tecnicos", json=payload)
            if resp:
                st.success(f"Técnico cadastrado. ID #{resp['id']}")
                novo = api_segura("GET", f"/tecnicos/{resp['id']}")
                if novo:
                    st.session_state.tecnico_logado = novo

    tecnico = st.session_state.get("tecnico_logado")
    if tecnico:
        st.divider()
        st.markdown(f"### Técnico: {tecnico['nome']} 🛠️")
        chamados = api_segura("GET", "/chamados") or []
        disponiveis = [c for c in chamados if norm_status(c.get("status")) in {"aberto", "aguardando"}]
        meus = [c for c in chamados if c.get("tecnico_id") == tecnico["id"] and norm_status(c.get("status")) not in {"finalizado", "resolvido"}]

        c1, c2, c3 = st.columns(3)
        c1.metric("Críticos na fila", sum(str(c.get("prioridade", "")).upper() == "CRÍTICA" for c in disponiveis))
        c2.metric("Aguardando", len(disponiveis))
        c3.metric("Meus em atendimento", len(meus))

        tab_fila, tab_meus = st.tabs(["Fila de atendimento", "Meus chamados"])
        with tab_fila:
            tabela_chamados(disponiveis, "fila")
            if disponiveis:
                ids = [c["id"] for c in disponiveis]
                chamado_id = st.selectbox("Chamado para assumir", ids, format_func=lambda x: f"#{x} — {next(c['titulo'] for c in disponiveis if c['id']==x)}")
                if st.button("ASSUMIR CHAMADO", type="primary"):
                    resp = api_segura("POST", f"/chamados/{chamado_id}/assumir", json={"tecnico_id": tecnico["id"]})
                    if resp:
                        st.success(f"Chamado #{chamado_id} assumido. Status: Em atendimento.")
                        st.rerun()

        with tab_meus:
            tabela_chamados(meus, "meus_tecnico")
            if meus:
                ids = [c["id"] for c in meus]
                chamado_id = st.selectbox("Atender chamado", ids, format_func=lambda x: f"#{x} — {next(c['titulo'] for c in meus if c['id']==x)}", key="atender_id")
                chamado = next(c for c in meus if c["id"] == chamado_id)
                st.write(chamado["descricao"])

                col1, col2 = st.columns(2)
                with col1:
                    novo_status = st.selectbox("Novo status", ["em_atendimento", "aguardando", "resolvido", "finalizado"], format_func=status_legivel)
                    observacao = st.text_area("Observação do atendimento", value="Atendimento atualizado pelo técnico.")
                    if st.button("ATUALIZAR STATUS", type="primary"):
                        payload = {"status": novo_status, "tecnico_id": tecnico["id"], "observacao": observacao}
                        if api_segura("PATCH", f"/chamados/{chamado_id}/status", json=payload):
                            st.success("Status atualizado com sucesso.")
                            st.rerun()

                with col2:
                    with st.form(f"comentario_tecnico_{chamado_id}"):
                        texto = st.text_area("Registrar atendimento/comentário")
                        registrar = st.form_submit_button("REGISTRAR ATENDIMENTO")
                    if registrar and texto.strip():
                        payload = {
                            "autor_tipo": "tecnico",
                            "usuario_id": None,
                            "tecnico_id": tecnico["id"],
                            "comentario": texto.strip(),
                            "visibilidade": "publico",
                        }
                        if api_segura("POST", f"/chamados/{chamado_id}/comentarios", json=payload):
                            st.success("Atendimento registrado.")
                            st.rerun()


# ==========================================================
# PERFIL ADMINISTRADOR
# ==========================================================
else:
    cabecalho("Interface Administrativa", "Do operacional para o gerencial: gestão, controle e visibilidade.")

    if not st.session_state.get("admin_logado"):
        st.markdown('<div class="lab-note">Acesso administrativo único para o laboratório.</div>', unsafe_allow_html=True)
        with st.form("login_admin"):
            usuario_admin = st.text_input("Usuário administrativo")
            senha_admin = st.text_input("Senha", type="password")
            entrar = st.form_submit_button("Entrar", type="primary")
        if entrar:
            if usuario_admin == ADMIN_USER and senha_admin == ADMIN_PASSWORD:
                st.session_state.admin_logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos.")
    else:
        topo1, topo2 = st.columns([5, 1])
        with topo2:
            if st.button("Sair do Admin"):
                st.session_state.admin_logado = False
                st.rerun()

        resumo = api_segura("GET", "/dashboard/resumo") or {}
        c1, c2, c3 = st.columns(3)
        c1.metric("Usuários", resumo.get("usuarios", 0))
        c2.metric("Técnicos", resumo.get("tecnicos", 0))
        c3.metric("Chamados", resumo.get("chamados", 0))

        por_status = resumo.get("por_status", {})
        s1, s2, s3 = st.columns(3)
        s1.metric("Abertos", por_status.get("aberto", 0))
        s2.metric("Em atendimento", por_status.get("em_atendimento", 0))
        s3.metric("Finalizados", por_status.get("finalizado", 0) + por_status.get("resolvido", 0))

        tab_dash, tab_usuarios, tab_tecnicos, tab_chamados = st.tabs(["Visão global", "Usuários", "Técnicos", "Chamados"])
        with tab_dash:
            st.markdown("### Chamados por status")
            if por_status:
                st.bar_chart(por_status)
            st.markdown("### Chamados por categoria")
            categorias = resumo.get("por_categoria", [])
            if categorias:
                st.bar_chart({x["categoria"]: x["total"] for x in categorias})

        with tab_usuarios:
            usuarios = api_segura("GET", "/usuarios") or []
            st.dataframe(usuarios, use_container_width=True, hide_index=True)

        with tab_tecnicos:
            tecnicos = api_segura("GET", "/tecnicos") or []
            st.dataframe(tecnicos, use_container_width=True, hide_index=True)

        with tab_chamados:
            chamados = api_segura("GET", "/chamados") or []
            tabela_chamados(chamados, "admin")
            if chamados:
                ids = [c["id"] for c in chamados]
                chamado_id = st.selectbox("Inspecionar chamado", ids, format_func=lambda x: f"Chamado #{x}")
                hist = api_segura("GET", f"/chamados/{chamado_id}/historico") or []
                comentarios = api_segura("GET", f"/chamados/{chamado_id}/comentarios") or []
                col_h, col_c = st.columns(2)
                with col_h:
                    st.markdown("#### Histórico")
                    st.dataframe(hist, use_container_width=True, hide_index=True)
                with col_c:
                    st.markdown("#### Comentários")
                    st.dataframe(comentarios, use_container_width=True, hide_index=True)

st.divider()
st.caption("Professor Rodolfo Terra | linkedin.com/in/rodolffoterra/ | github.com/rodolffoterra")
