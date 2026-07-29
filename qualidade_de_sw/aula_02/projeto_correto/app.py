import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Laboratório de Qualidade de Software",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# FUNÇÕES DE NAVEGAÇÃO
# =========================================================
PAGINAS = {
    "Adequação Funcional": "pages/01_Adequacao_Funcional.py",
    "Eficiência de Desempenho": "pages/02_eficiencia_desempenho.py",
    "Compatibilidade": "pages/03_compatibilidade.py",
    "Usabilidade": "pages/04_usabilidade.py",
    "Confiabilidade": "pages/05_confiabilidade.py",
    "Segurança": "pages/06_seguranca.py",
    "Manutenibilidade": "pages/07_manutenibilidade.py",
    "Portabilidade": "pages/08_portabilidade.py",
    "Dashboard de Qualidade": "pages/09_dashboard.py",
}


def acessar_pagina(nome_pagina: str) -> None:
    """
    Navega para uma página registrada no dicionário PAGINAS.
    """

    caminho = PAGINAS.get(nome_pagina)

    if caminho is None:
        st.error(f"A página '{nome_pagina}' não foi configurada.")
        return

    st.switch_page(caminho)


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🧪 Qualidade de Software")

    st.markdown(
        """
        Esta aplicação apresenta exemplos didáticos de falhas relacionadas
        à qualidade de software.

        Cada característica é demonstrada em uma página separada.
        """
    )

    st.divider()

    st.subheader("Conteúdo da aplicação")
    st.markdown("🏠 **Página inicial**")

    botoes_sidebar = [
        ("🎯", "Adequação Funcional"),
        ("⚡", "Eficiência de Desempenho"),
        ("🔌", "Compatibilidade"),
        ("👩‍💻", "Usabilidade"),
        ("🛡️", "Confiabilidade"),
        ("🔐", "Segurança"),
        ("🛠️", "Manutenibilidade"),
        ("📦", "Portabilidade"),
        ("📊", "Dashboard de Qualidade"),
    ]

    for icone, nome in botoes_sidebar:
        if st.button(
            f"{icone} {nome}",
            key=f"sidebar_{nome}",
            use_container_width=True,
        ):
            acessar_pagina(nome)

    st.success(
        """
        Todas as oito páginas do laboratório estão disponíveis.
        """
    )

    st.divider()

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🧪 Laboratório de Falhas de Software")

st.subheader(
    "Aprendendo qualidade de software por meio de exemplos incorretos"
)

st.write(
    """
    Esta aplicação foi criada para demonstrar, de forma prática, como
    diferentes falhas podem comprometer a qualidade de um sistema.
    """
)


# =========================================================
# OBJETIVO
# =========================================================
st.info(
    """
    ### 🎓 Objetivo da aplicação

    Cada página apresentará uma aplicação propositalmente problemática.

    O aluno deverá observar o comportamento do sistema, identificar a falha,
    compreender seu impacto e analisar uma possível solução.
    """
)


# =========================================================
# AVISO
# =========================================================
st.warning(
    """
    ### ⚠️ Atenção

    Os códigos apresentados neste projeto poderão conter erros, más práticas
    e decisões inadequadas de forma intencional.

    O objetivo é utilizar essas falhas como exemplos didáticos.

    Os códigos com falhas não devem ser utilizados em sistemas reais.
    """
)


st.divider()


# =========================================================
# COMO FUNCIONARÁ O LABORATÓRIO
# =========================================================
st.header("Como funcionará o laboratório")

coluna_1, coluna_2, coluna_3 = st.columns(3)

with coluna_1:
    with st.container(border=True):
        st.subheader("1️⃣ Observar")

        st.write(
            """
            O aluno utiliza uma aplicação que contém uma falha proposital.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("2️⃣ Identificar")

        st.write(
            """
            O aluno analisa o comportamento e identifica o problema
            relacionado à qualidade do software.
            """
        )

with coluna_3:
    with st.container(border=True):
        st.subheader("3️⃣ Corrigir")

        st.write(
            """
            O aluno compara a implementação inadequada com uma solução
            que atende corretamente ao requisito.
            """
        )


st.divider()


# =========================================================
# DADOS DAS CARACTERÍSTICAS
# =========================================================
caracteristicas = [
    {
        "icone": "🎯",
        "nome": "Adequação Funcional",
        "descricao": (
            "Verifica se o software executa corretamente as funções "
            "para as quais foi desenvolvido."
        ),
        "falha": (
            "Cálculo incorreto ou funcionalidade que não atende ao requisito."
        ),
        "disponivel": True,
    },
    {
        "icone": "⚡",
        "nome": "Eficiência de Desempenho",
        "descricao": (
            "Avalia o tempo de resposta, o consumo de recursos e a "
            "velocidade de execução."
        ),
        "falha": (
            "Processamento lento ou consumo desnecessário de memória e CPU."
        ),
        "disponivel": True,
    },
    {
        "icone": "🔌",
        "nome": "Compatibilidade",
        "descricao": (
            "Avalia a capacidade do sistema de funcionar com APIs, bancos "
            "de dados, arquivos e outras plataformas."
        ),
        "falha": (
            "Integração que aceita apenas um formato rígido de dados."
        ),
        "disponivel": True,
    },
    {
        "icone": "👩‍💻",
        "nome": "Usabilidade",
        "descricao": (
            "Mede a facilidade de aprendizado e utilização da aplicação."
        ),
        "falha": (
            "Formulário confuso, mensagens pouco claras ou excesso de etapas."
        ),
        "disponivel": True,
    },
    {
        "icone": "🛡️",
        "nome": "Confiabilidade",
        "descricao": (
            "Mede a capacidade do sistema de continuar operando corretamente "
            "e sem interrupções."
        ),
        "falha": (
            "Aplicação que encerra ao receber uma entrada inesperada."
        ),
        "disponivel": True,
    },
    {
        "icone": "🔐",
        "nome": "Segurança",
        "descricao": (
            "Avalia a proteção dos dados, autenticação, autorização e "
            "transações."
        ),
        "falha": (
            "Senha exposta, dados sensíveis visíveis ou validação inadequada."
        ),
        "disponivel": True,
    },
    {
        "icone": "🛠️",
        "nome": "Manutenibilidade",
        "descricao": (
            "Representa a facilidade de corrigir, compreender, testar e "
            "modificar o software."
        ),
        "falha": (
            "Código duplicado, extenso, sem funções e sem organização."
        ),
        "disponivel": True,
    },
    {
        "icone": "📦",
        "nome": "Portabilidade",
        "descricao": (
            "Avalia a facilidade de executar o sistema em diferentes "
            "ambientes e plataformas."
        ),
        "falha": (
            "Uso de caminhos fixos, configurações locais e dependências "
            "não documentadas."
        ),
        "disponivel": True,
    },
    {
    "icone": "📊",
    "nome": "Dashboard de Qualidade",
    "descricao": (
        "Consolida os indicadores, metas, falhas, testes, riscos "
        "e incidentes das oito características de qualidade."
    ),
    "falha": (
        "Ausência de monitoramento consolidado dificulta identificar "
        "riscos, tendências e prioridades de melhoria."
    ),
    "disponivel": True,
    "pagina": "dashboard",
    }
]


# =========================================================
# EXIBIÇÃO DAS CARACTERÍSTICAS
# =========================================================
st.header("Características que serão demonstradas")

for indice in range(0, len(caracteristicas), 4):
    colunas = st.columns(4)
    grupo = caracteristicas[indice:indice + 4]

    for coluna, caracteristica in zip(colunas, grupo):
        with coluna:
            with st.container(border=True):
                st.subheader(
                    f'{caracteristica["icone"]} '
                    f'{caracteristica["nome"]}'
                )

                st.write(caracteristica["descricao"])

                st.markdown("**Exemplo de falha:**")

                st.error(caracteristica["falha"])

                if caracteristica["disponivel"]:
                    if st.button(
                        "Acessar demonstração",
                        key=f'card_{caracteristica["nome"]}',
                        type="primary",
                        use_container_width=True,
                    ):
                        acessar_pagina(
                            caracteristica["nome"]
                        )

                else:
                    st.button(
                        "Página em construção",
                        key=f'card_indisponivel_{caracteristica["nome"]}',
                        disabled=True,
                        use_container_width=True,
                    )


st.divider()


# =========================================================
# ESTRUTURA DAS PÁGINAS
# =========================================================
st.header("Estrutura de cada página")

st.write(
    """
    Cada página do laboratório seguirá uma estrutura semelhante:
    """
)

etapas = [
    "Descrição do cenário",
    "Apresentação do requisito",
    "Aplicação com comportamento inadequado",
    "Demonstração prática da falha",
    "Explicação do problema",
    "Impactos causados pela falha",
    "Métrica que poderia identificar o problema",
    "Exemplo de código corrigido",
]

for numero, etapa in enumerate(etapas, start=1):
    st.write(f"**{numero}.** {etapa}")


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Possíveis métricas de qualidade")

metricas = [
    {
        "Característica": "Adequação Funcional",
        "Possível métrica": "Percentual de requisitos atendidos",
    },
    {
        "Característica": "Eficiência",
        "Possível métrica": "Tempo de resposta e consumo de memória",
    },
    {
        "Característica": "Compatibilidade",
        "Possível métrica": "Taxa de sucesso das integrações",
    },
    {
        "Característica": "Usabilidade",
        "Possível métrica": "Tempo necessário para concluir uma tarefa",
    },
    {
        "Característica": "Confiabilidade",
        "Possível métrica": "Taxa de falhas e disponibilidade",
    },
    {
        "Característica": "Segurança",
        "Possível métrica": "Quantidade de vulnerabilidades encontradas",
    },
    {
        "Característica": "Manutenibilidade",
        "Possível métrica": "Tempo necessário para implementar alterações",
    },
    {
        "Característica": "Portabilidade",
        "Possível métrica": "Quantidade de ambientes suportados",
    },
]

st.dataframe(
    metricas,
    use_container_width=True,
    hide_index=True,
)


st.divider()


# =========================================================
# QUALIDADE DO PRODUTO E DO PROCESSO
# =========================================================
st.header("Qualidade do Produto × Qualidade do Processo")

produto, processo = st.columns(2)

with produto:
    with st.container(border=True):
        st.subheader("📦 Qualidade do Produto")

        st.write(
            """
            Avalia o software entregue ao usuário.
            """
        )

        st.markdown(
            """
            - Funcionalidades
            - Segurança
            - Desempenho
            - Usabilidade
            - Confiabilidade
            """
        )

with processo:
    with st.container(border=True):
        st.subheader("⚙️ Qualidade do Processo")

        st.write(
            """
            Avalia como o software foi planejado, desenvolvido e testado.
            """
        )

        st.markdown(
            """
            - Planejamento
            - Testes
            - Documentação
            - Revisão de código
            - Controle de versões
            """
        )


st.divider()


# =========================================================
# MENSAGEM FINAL
# =========================================================
st.success(
    """
    ### ✅ Mensagem principal

    Qualidade de software não significa apenas ausência de bugs.

    Um software de qualidade precisa atender aos requisitos, ser confiável,
    seguro, eficiente, fácil de utilizar e simples de manter.
    """
)

st.caption(
    """
    A qualidade deve ser construída desde os requisitos, passando pelo
    desenvolvimento, testes, implantação e manutenção.
    """
)