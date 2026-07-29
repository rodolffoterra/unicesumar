import streamlit as st


# ---------------------------------------------------------
# Configuração geral da aplicação
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
            min-height: 180px;
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

        Cada página demonstra uma falha relacionada a uma característica
        da qualidade de software.
        """
    )

    st.divider()

    st.subheader("Páginas do laboratório")

    st.page_link(
        "app.py",
        label="Início",
        icon="🏠",
    )

    st.page_link(
        "pages/01_adequacao_funcional.py",
        label="Adequação Funcional",
        icon="🎯",
    )

    st.page_link(
        "pages/02_eficiencia.py",
        label="Eficiência",
        icon="⚡",
    )

    st.page_link(
        "pages/03_compatibilidade.py",
        label="Compatibilidade",
        icon="🔌",
    )

    st.page_link(
        "pages/04_usabilidade.py",
        label="Usabilidade",
        icon="🧑‍💻",
    )

    st.page_link(
        "pages/05_confiabilidade.py",
        label="Confiabilidade",
        icon="🛡️",
    )

    st.page_link(
        "pages/06_seguranca.py",
        label="Segurança",
        icon="🔐",
    )

    st.page_link(
        "pages/07_manutenibilidade.py",
        label="Manutenibilidade",
        icon="🛠️",
    )

    st.page_link(
        "pages/08_portabilidade.py",
        label="Portabilidade",
        icon="📦",
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
# Introdução
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
# Como a aula será organizada
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

row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

with row1_col1:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🎯 Adequação Funcional</h3>

            <p>
                Verifica se o software executa corretamente as funções
                para as quais foi desenvolvido.
            </p>

            <strong>Exemplo de falha:</strong>
            cálculo incorreto ou funcionalidade que não atende ao requisito.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row1_col2:
    st.markdown(
        """
        <div class="quality-card">
            <h3>⚡ Eficiência</h3>

            <p>
                Avalia o tempo de resposta, o consumo de recursos e a
                velocidade de execução.
            </p>

            <strong>Exemplo de falha:</strong>
            processamento desnecessariamente lento.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row1_col3:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🔌 Compatibilidade</h3>

            <p>
                Avalia a capacidade do sistema de funcionar com APIs,
                bancos de dados e outras plataformas.
            </p>

            <strong>Exemplo de falha:</strong>
            integração que depende de um formato rígido.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row1_col4:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🧑‍💻 Usabilidade</h3>

            <p>
                Mede a facilidade de aprendizado e utilização da aplicação.
            </p>

            <strong>Exemplo de falha:</strong>
            formulário confuso e mensagens pouco claras.
        </div>
        """,
        unsafe_allow_html=True,
    )


row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

with row2_col1:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🛡️ Confiabilidade</h3>

            <p>
                Mede a capacidade do sistema de continuar operando
                corretamente e sem interrupções.
            </p>

            <strong>Exemplo de falha:</strong>
            aplicação que quebra ao receber uma entrada inesperada.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row2_col2:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🔐 Segurança</h3>

            <p>
                Avalia a proteção dos dados, autenticação, autorização
                e transações.
            </p>

            <strong>Exemplo de falha:</strong>
            senha exposta ou validação inadequada.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row2_col3:
    st.markdown(
        """
        <div class="quality-card">
            <h3>🛠️ Manutenibilidade</h3>

            <p>
                Representa a facilidade de corrigir, compreender,
                testar e modificar o software.
            </p>

            <strong>Exemplo de falha:</strong>
            código duplicado e sem organização.
        </div>
        """,
        unsafe_allow_html=True,
    )

with row2_col4:
    st.markdown(
        """
        <div class="quality-card">
            <h3>📦 Portabilidade</h3>

            <p>
                Avalia a facilidade de executar o sistema em diferentes
                ambientes e plataformas.
            </p>

            <strong>Exemplo de falha:</strong>
            uso de caminhos fixos e dependências locais.
        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ---------------------------------------------------------
# Estrutura padrão das páginas
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
# Relação com métricas
# ---------------------------------------------------------
st.header("Métricas que poderão ser analisadas")

metrics = {
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
    metrics,
    use_container_width=True,
    hide_index=True,
)


# ---------------------------------------------------------
# Encerramento
# ---------------------------------------------------------
st.divider()

st.success(
    """
    Selecione uma página no menu lateral para analisar uma característica
    da qualidade de software.
    """
)

st.caption(
    """
    A qualidade não deve ser adicionada apenas ao final do projeto.
    Ela precisa ser considerada desde os requisitos, passando pela
    implementação, testes, implantação e manutenção.
    """
)