import json
from pathlib import Path

import pandas as pd
import streamlit as st

from typing import Optional

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="Cadastro de Usuários",
    page_icon="👥",
    layout="wide",
)

ARQUIVO_JSON = Path(__file__).with_name("usuarios.json")


# =========================================================
# FUNÇÕES DE ACESSO AO JSON
# =========================================================

def garantir_arquivo_json() -> None:
    """Cria o arquivo JSON com cinco registros caso ele ainda não exista."""
    if not ARQUIVO_JSON.exists():
        salvar_usuarios(DADOS_INICIAIS)


def carregar_usuarios() -> list[dict]:
    """Carrega todos os usuários do arquivo JSON."""
    garantir_arquivo_json()

    try:
        with ARQUIVO_JSON.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            st.error("O arquivo usuarios.json precisa conter uma lista.")
            return []

        return dados

    except json.JSONDecodeError:
        st.error("O arquivo usuarios.json está com formato inválido.")
        return []

    except OSError as erro:
        st.error(f"Não foi possível abrir o arquivo JSON: {erro}")
        return []


def salvar_usuarios(usuarios: list[dict]) -> None:
    """Salva a lista de usuários no arquivo JSON."""
    with ARQUIVO_JSON.open("w", encoding="utf-8") as arquivo:
        json.dump(
            usuarios,
            arquivo,
            ensure_ascii=False,
            indent=4,
        )


def buscar_usuario_por_id(
    usuarios: list[dict],
    usuario_id: int
) -> Optional[dict]:
    """Retorna um usuário pelo ID."""
    return next(
        (
            usuario
            for usuario in usuarios
            if usuario["id"] == usuario_id
        ),
        None,
    )


def gerar_proximo_id(usuarios: list[dict]) -> int:
    """Gera automaticamente o próximo ID disponível."""
    if not usuarios:
        return 1

    return max(usuario["id"] for usuario in usuarios) + 1


def validar_dados(
    nome: str,
    idade: int,
    endereco: str,
    profissao: str,
    salario: float,
) -> list[str]:
    """Valida os campos informados e devolve uma lista de erros."""
    erros = []

    if not nome.strip():
        erros.append("Informe o nome.")

    if idade < 0 or idade > 120:
        erros.append("A idade deve estar entre 0 e 120 anos.")

    if not endereco.strip():
        erros.append("Informe o endereço.")

    if not profissao.strip():
        erros.append("Informe a profissão.")

    if salario < 0:
        erros.append("O salário não pode ser negativo.")

    return erros


# =========================================================
# INTERFACE
# =========================================================

st.title("👥 Gerenciamento de Usuários")
st.caption(
    "Aplicação Streamlit para consultar, adicionar, alterar e excluir "
    "registros armazenados em um arquivo JSON local."
)

usuarios = carregar_usuarios()

total_usuarios = len(usuarios)
media_idade = (
    sum(usuario["idade"] for usuario in usuarios) / total_usuarios
    if total_usuarios
    else 0
)
media_salarial = (
    sum(usuario["salario"] for usuario in usuarios) / total_usuarios
    if total_usuarios
    else 0
)

coluna1, coluna2, coluna3 = st.columns(3)
coluna1.metric("Usuários cadastrados", total_usuarios)
coluna2.metric("Média de idade", f"{media_idade:.1f} anos")
coluna3.metric("Média salarial", f"R$ {media_salarial:,.2f}")

aba_lista, aba_consulta, aba_adicionar, aba_alterar, aba_excluir = st.tabs(
    [
        "📋 Todos",
        "🔎 Consultar",
        "➕ Adicionar",
        "✏️ Alterar",
        "🗑️ Excluir",
    ]
)


# =========================================================
# LISTAR TODOS
# =========================================================

with aba_lista:
    st.subheader("Todos os usuários")

    if usuarios:
        tabela = pd.DataFrame(usuarios)
        tabela = tabela[
            ["id", "nome", "idade", "endereco", "profissao", "salario"]
        ]

        st.dataframe(
            tabela,
            use_container_width=True,
            hide_index=True,
            column_config={
                "id": st.column_config.NumberColumn("ID", format="%d"),
                "nome": "Nome",
                "idade": st.column_config.NumberColumn("Idade", format="%d"),
                "endereco": "Endereço",
                "profissao": "Profissão",
                "salario": st.column_config.NumberColumn(
                    "Salário",
                    format="R$ %.2f",
                ),
            },
        )

        with st.expander("Visualizar JSON completo"):
            st.json(usuarios)

    else:
        st.info("Nenhum usuário cadastrado.")


# =========================================================
# CONSULTAR USUÁRIO
# =========================================================

with aba_consulta:
    st.subheader("Consultar um usuário específico")

    if usuarios:
        opcoes = {
            f'{usuario["id"]} — {usuario["nome"]}': usuario["id"]
            for usuario in usuarios
        }

        usuario_selecionado = st.selectbox(
            "Selecione o usuário",
            options=list(opcoes.keys()),
            key="consulta_usuario",
        )

        id_consulta = opcoes[usuario_selecionado]
        usuario = buscar_usuario_por_id(usuarios, id_consulta)

        if usuario:
            coluna_a, coluna_b = st.columns(2)

            with coluna_a:
                st.text_input(
                    "Nome",
                    value=usuario["nome"],
                    disabled=True,
                    key="consulta_nome",
                )
                st.number_input(
                    "Idade",
                    value=int(usuario["idade"]),
                    disabled=True,
                    key="consulta_idade",
                )
                st.text_input(
                    "Profissão",
                    value=usuario["profissao"],
                    disabled=True,
                    key="consulta_profissao",
                )

            with coluna_b:
                st.text_area(
                    "Endereço",
                    value=usuario["endereco"],
                    disabled=True,
                    key="consulta_endereco",
                )
                st.number_input(
                    "Salário",
                    value=float(usuario["salario"]),
                    disabled=True,
                    key="consulta_salario",
                )

            st.markdown("#### Registro em JSON")
            st.json(usuario)

    else:
        st.info("Não existem usuários para consultar.")


# =========================================================
# ADICIONAR USUÁRIO
# =========================================================

with aba_adicionar:
    st.subheader("Adicionar um novo usuário")

    with st.form("formulario_adicionar", clear_on_submit=True):
        proximo_id = gerar_proximo_id(usuarios)

        st.text_input(
            "ID gerado automaticamente",
            value=str(proximo_id),
            disabled=True,
        )

        nome = st.text_input("Nome")
        idade = st.number_input(
            "Idade",
            min_value=0,
            max_value=120,
            step=1,
        )
        endereco = st.text_input("Endereço")
        profissao = st.text_input("Profissão")
        salario = st.number_input(
            "Salário",
            min_value=0.0,
            step=100.0,
            format="%.2f",
        )

        cadastrar = st.form_submit_button(
            "Cadastrar usuário",
            use_container_width=True,
        )

    if cadastrar:
        erros = validar_dados(
            nome=nome,
            idade=int(idade),
            endereco=endereco,
            profissao=profissao,
            salario=float(salario),
        )

        if erros:
            for erro in erros:
                st.error(erro)
        else:
            novo_usuario = {
                "id": proximo_id,
                "nome": nome.strip(),
                "idade": int(idade),
                "endereco": endereco.strip(),
                "profissao": profissao.strip(),
                "salario": float(salario),
            }

            usuarios.append(novo_usuario)
            salvar_usuarios(usuarios)

            st.success(
                f'Usuário "{novo_usuario["nome"]}" cadastrado com sucesso!'
            )
            st.rerun()


# =========================================================
# ALTERAR USUÁRIO
# =========================================================

with aba_alterar:
    st.subheader("Alterar um usuário existente")

    if usuarios:
        opcoes_alteracao = {
            f'{usuario["id"]} — {usuario["nome"]}': usuario["id"]
            for usuario in usuarios
        }

        usuario_alteracao = st.selectbox(
            "Selecione o registro que será alterado",
            options=list(opcoes_alteracao.keys()),
            key="alteracao_usuario",
        )

        id_alteracao = opcoes_alteracao[usuario_alteracao]
        registro = buscar_usuario_por_id(usuarios, id_alteracao)

        with st.form("formulario_alterar"):
            nome_alterado = st.text_input(
                "Nome",
                value=registro["nome"],
            )
            idade_alterada = st.number_input(
                "Idade",
                min_value=0,
                max_value=120,
                value=int(registro["idade"]),
                step=1,
            )
            endereco_alterado = st.text_input(
                "Endereço",
                value=registro["endereco"],
            )
            profissao_alterada = st.text_input(
                "Profissão",
                value=registro["profissao"],
            )
            salario_alterado = st.number_input(
                "Salário",
                min_value=0.0,
                value=float(registro["salario"]),
                step=100.0,
                format="%.2f",
            )

            atualizar = st.form_submit_button(
                "Salvar alterações",
                use_container_width=True,
            )

        if atualizar:
            erros = validar_dados(
                nome=nome_alterado,
                idade=int(idade_alterada),
                endereco=endereco_alterado,
                profissao=profissao_alterada,
                salario=float(salario_alterado),
            )

            if erros:
                for erro in erros:
                    st.error(erro)
            else:
                registro["nome"] = nome_alterado.strip()
                registro["idade"] = int(idade_alterada)
                registro["endereco"] = endereco_alterado.strip()
                registro["profissao"] = profissao_alterada.strip()
                registro["salario"] = float(salario_alterado)

                salvar_usuarios(usuarios)

                st.success("Usuário atualizado com sucesso!")
                st.rerun()

    else:
        st.info("Não existem usuários para alterar.")


# =========================================================
# EXCLUIR USUÁRIO
# =========================================================

with aba_excluir:
    st.subheader("Excluir um usuário")

    if usuarios:
        opcoes_exclusao = {
            f'{usuario["id"]} — {usuario["nome"]}': usuario["id"]
            for usuario in usuarios
        }

        usuario_exclusao = st.selectbox(
            "Selecione o registro que será excluído",
            options=list(opcoes_exclusao.keys()),
            key="exclusao_usuario",
        )

        id_exclusao = opcoes_exclusao[usuario_exclusao]
        registro_exclusao = buscar_usuario_por_id(
            usuarios,
            id_exclusao,
        )

        st.warning(
            f'Você está prestes a excluir "{registro_exclusao["nome"]}".'
        )
        st.json(registro_exclusao)

        confirmar = st.checkbox(
            "Confirmo que desejo excluir este usuário.",
            key="confirmar_exclusao",
        )

        if st.button(
            "Excluir usuário",
            type="primary",
            disabled=not confirmar,
            use_container_width=True,
        ):
            usuarios_atualizados = [
                usuario
                for usuario in usuarios
                if usuario["id"] != id_exclusao
            ]

            salvar_usuarios(usuarios_atualizados)

            st.success("Usuário excluído com sucesso!")
            st.rerun()

    else:
        st.info("Não existem usuários para excluir.")


# =========================================================
# RODAPÉ
# =========================================================

st.divider()
st.caption(f"Arquivo utilizado: {ARQUIVO_JSON}")
