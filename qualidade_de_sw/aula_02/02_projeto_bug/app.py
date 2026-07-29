import streamlit as st


# ---------------------------------------------------------
# Configuração geral
# ---------------------------------------------------------
st.set_page_config(
    page_title="Laboratório de Qualidade de Software",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Estilos visuais
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 20px;
            color: #6b7280;
            margin-bottom: 30px;
        }

        .quality-card {
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 18px;
            min-height: 190px;
            margin-bottom: 16px;
            background-color: rgba(255, 255, 255, 0.03);
        }

        .quality-card h3 {
            margin-top: 0;
        }

        .failure-box {
            border-left: 6px solid #ef4444;
            background-color: rgba(239, 68, 68, 0.08);
            padding: 18px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .objective-box {
            border-left: 6px solid #2563eb;
            background-color: rgba(37, 99, 235, 0.08);
            padding: 18px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------
with st.sidebar:
    st.title("🧪 Qualidade de Software")

    st.markdown(
        """
        Esta aplicação apresenta exemplos propositalmente incorretos.

        Cada página demonstrará uma falha relacionada a uma característica
        da qualidade de software.
        """
    )

    st.divider()

    st.subheader("Conteúdo do laboratório")

    st.markdown(
        """
        🏠 **Início**

        🎯 Adequação Funcional

        ⚡ Eficiência de Desempenho

        🔌 Compatibilidade

        🧑‍💻 Usabilidade

        🛡️ Confiabilidade

        🔐 Segurança

        🛠️ Manutenibilidade

        📦 Portabilidade
        """
    )

    st.info(
        "As páginas serão adicionadas gradualmente durante a aula."
    )

    st.divider()

    st.caption(
        "Aplicação didática — Medição e Avaliação da Qualidade de Software"
    )


# ---------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">Laboratório de Falhas de Software</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
        Aprendendo qualidade de software por meio de exemplos incorretos
        desenvolvidos em Python e Streamlit.
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Objetivo
# ---------------------------------------------------------
st.markdown(
    """
    <div class="objective-box">
        <h3>🎓 Objetivo da aplicação</h3>

        <p>
            Demonstrar, de forma prática, como diferentes falhas podem
            comprometer a qualidade de um sistema.
        </p>

        <p>
            Cada página apresentará uma aplicação propositalmente problemática,
            seguida de uma explicação sobre a falha encontrada, seus impactos
            e uma possível forma de correção.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Aviso didático
# ---------------------------------------------------------
st.markdown(
    """
    <div class="failure-box">
        <h3>⚠️ Atenção</h3>

        <p>
            Os códigos apresentados nas páginas deste projeto conterão
            erros, más práticas e decisões inadequadas de forma intencional.
        </p>

        <p>
            O objetivo não é utilizar esses códigos em produção, mas analisar
            as falhas e compreender como elas afetam a qualidade do software.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Etapas do laboratório
# ---------------------------------------------------------
st.header("Como funcionará o laboratório")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        **1. Observar**

        O aluno utiliza uma aplicação que contém uma falha proposital.
        """
    )

with col2:
    st.warning(
        """
        **2. Identificar**

        O aluno analisa o comportamento e identifica o problema de qualidade.
        """
    )

with col3:
    st.success(
        """
        **3. Corrigir**

        O aluno compara a implementação inadequada com uma solução melhor.
        """
    )


st.divider()


# ---------------------------------------------------------
# Características da qualidade
# ---------------------------------------------------------
st.header("Características que serão demonstradas")

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
    },
    {
        "icone": "⚡",
        "nome": "Eficiência",
        "descricao": (
            "Avalia o tempo de resposta, o consumo de recursos "
            "e a velocidade de execução."
        ),
        "falha": "Processamento desnecessariamente lento.",
    },
    {
        "icone": "🔌",
        "nome": "Compatibilidade",
        "descricao": (
            "Avalia a capacidade do sistema de funcionar com APIs, "
            "bancos de dados e outras plataformas."
        ),
        "falha": "Integração que depende de um formato rígido.",
    },
    {
        "icone": "🧑‍💻",
        "nome": "Usabilidade",
        "descricao": (
            "Mede a facilidade de aprendizado e utilização da aplicação."
        ),
        "falha": "Formulário confuso e mensagens pouco claras.",
    },
    {
        "icone": "🛡️",
        "nome": "Confiabilidade",
        "descricao": (
            "Mede a capacidade do sistema de continuar operando "
            "corretamente e sem interrupções."
        ),
        "falha": (
            "Aplicação que encerra ao receber uma entrada inesperada."
        ),
    },
    {
        "icone": "🔐",
        "nome": "Segurança",
        "descricao": (
            "Avalia a proteção dos dados, autenticação, autorização "
            "e transações."
        ),
        "falha": "Senha exposta ou validação inadequada.",
    },
    {
        "icone": "🛠️",
        "nome": "Manutenibilidade",
        "descricao": (
            "Representa a facilidade de corrigir, compreender, "
            "testar e modificar o software."
        ),
        "falha": "Código duplicado, extenso e sem organização.",
    },
    {
        "icone": "📦",
        "nome": "Portabilidade",
        "descricao": (
            "Avalia a facilidade de executar o sistema em diferentes "
            "ambientes e plataformas."
        ),
        "falha": "Uso de caminhos fixos e dependências locais.",
    },
]


for inicio in range(0, len(caracteristicas), 4):
    colunas = st.columns(4)
    grupo = caracteristicas[inicio:inicio + 4]

    for coluna, caracteristica in zip(colunas, grupo):
        with coluna:
            st.markdown(
                f"""
                <div class="quality-card">
                    <h3>
                        {caracteristica["icone"]}
                        {caracteristica["nome"]}
                    </h3>

                    <p>{caracteristica["descricao"]}</p>

                    <strong>Exemplo de falha:</strong>
                    <p>{caracteristica["falha"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


st.divider()


# ---------------------------------------------------------
# Estrutura das páginas
# ---------------------------------------------------------
st.header("Estrutura de cada página")

st.markdown(
    """
    Cada exemplo seguirá aproximadamente esta sequência:

    1. **Descrição do cenário**
    2. **Aplicação com comportamento inadequado**
    3. **Bloco explicando a falha**
    4. **Impactos causados pelo problema**
    5. **Métrica que poderia identificar a falha**
    6. **Sugestão de melhoria**
    7. **Versão corrigida do código**
    """
)


# ---------------------------------------------------------
# Métricas
# ---------------------------------------------------------
st.header("Métricas que poderão ser analisadas")

metricas = {
    "Característica": [
        "Adequação Funcional",
        "Eficiência",
        "Compatibilidade",
        "Usabilidade",
        "Confiabilidade",
        "Segurança",
        "Manutenibilidade",
        "Portabilidade",
    ],
    "Possível métrica": [
        "Percentual de requisitos atendidos",
        "Tempo de resposta e uso de memória",
        "Taxa de sucesso das integrações",
        "Tempo para concluir uma tarefa",
        "Taxa de falhas e disponibilidade",
        "Quantidade de vulnerabilidades",
        "Tempo necessário para realizar alterações",
        "Quantidade de ambientes suportados",
    ],
}

st.dataframe(
    metricas,
    use_container_width=True,
    hide_index=True,
)


st.divider()

st.success(
    """
    As páginas serão liberadas gradualmente durante a aula.
    """
)

st.caption(
    """
    A qualidade não deve ser adicionada apenas ao final do projeto.
    Ela precisa ser considerada desde os requisitos, passando pela
    implementação, testes, implantação e manutenção.
    """
)