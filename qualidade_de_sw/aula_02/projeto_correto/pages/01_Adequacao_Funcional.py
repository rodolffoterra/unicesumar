import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Falha de Adequação Funcional",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# FUNÇÕES DO EXEMPLO
# =========================================================
def calcular_total_com_falha(
    valor_compra: float,
) -> tuple[float, float]:
    """
    Implementação propositalmente incorreta.

    Requisito correto:
    - Compras a partir de R$ 500,00 recebem 10% de desconto.

    Falhas propositalmente implementadas:
    - Utiliza > 500 em vez de >= 500.
    - Aplica 5% de desconto em vez de 10%.
    """

    percentual_desconto = 0.0

    # FALHA FUNCIONAL 1:
    # Uma compra de exatamente R$ 500,00 não recebe desconto.
    if valor_compra > 500:

        # FALHA FUNCIONAL 2:
        # O requisito determina 10%, mas o sistema aplica 5%.
        percentual_desconto = 0.05

    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final


def calcular_total_correto(
    valor_compra: float,
) -> tuple[float, float]:
    """
    Implementação correta conforme o requisito.
    """

    percentual_desconto = 0.0

    if valor_compra >= 500:
        percentual_desconto = 0.10

    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final


def formatar_moeda(valor: float) -> str:
    """
    Formata um número no padrão monetário brasileiro.
    """

    valor_formatado = (
        f"{valor:,.2f}"
        .replace(",", "TEMP")
        .replace(".", ",")
        .replace("TEMP", ".")
    )

    return f"R$ {valor_formatado}"


def voltar_para_inicio() -> None:
    """
    Retorna para o arquivo principal da aplicação.
    """

    st.switch_page("app.py")


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🎯 Adequação Funcional")

    st.write(
        """
        Nesta página será demonstrada uma falha funcional em um
        sistema de cálculo de descontos.
        """
    )

    st.divider()

    if st.button(
        "🏠 Voltar para a página inicial",
        key="voltar_inicio_sidebar",
        use_container_width=True,
    ):
        voltar_para_inicio()

    st.divider()

    st.subheader("Nesta demonstração")

    st.markdown(
        """
        - requisito do cliente;
        - sistema com falha;
        - resultado incorreto;
        - comparação com o resultado esperado;
        - impactos da falha;
        - métrica de qualidade;
        - código corrigido.
        """
    )

    st.warning(
        """
        A falha apresentada nesta página é proposital e possui
        finalidade exclusivamente didática.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🎯 Falha de Adequação Funcional")

st.markdown(
    """
    Nesta página, analisaremos um sistema de descontos que executa
    normalmente, mas não atende corretamente ao requisito definido
    pelo cliente.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Adequação Funcional?

    Adequação Funcional avalia se o software executa corretamente
    as funções para as quais foi desenvolvido.

    Um sistema pode não apresentar erros técnicos e ainda possuir
    uma falha funcional quando entrega um resultado diferente
    daquele solicitado.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma loja solicitou um sistema para calcular automaticamente
    o desconto das compras realizadas pelos clientes.
    """
)

st.success(
    """
    ### Requisito definido pelo cliente

    Compras com valor **maior ou igual a R$ 500,00** devem receber
    **10% de desconto**.

    Compras abaixo de R$ 500,00 não recebem desconto.
    """
)


# =========================================================
# EXPLICAÇÃO INICIAL
# =========================================================
st.warning(
    """
    ### O problema implementado

    O sistema contém duas falhas propositais:

    1. Utiliza `valor_compra > 500`, excluindo compras de exatamente
       R$ 500,00.

    2. Aplica 5% de desconto, embora o requisito determine 10%.
    """
)


st.divider()


# =========================================================
# ENTRADA DO USUÁRIO
# =========================================================
st.header("Teste o sistema com falha")

valor_compra = st.number_input(
    label="Informe o valor da compra",
    min_value=0.0,
    value=500.0,
    step=50.0,
    format="%.2f",
    help=(
        "Experimente os valores R$ 400,00, "
        "R$ 500,00 e R$ 1.000,00."
    ),
)

calcular = st.button(
    "Calcular desconto",
    key="calcular_desconto",
    type="primary",
    use_container_width=True,
)


# =========================================================
# PROCESSAMENTO
# =========================================================
if calcular:
    desconto_incorreto, total_incorreto = (
        calcular_total_com_falha(valor_compra)
    )

    desconto_esperado, total_esperado = (
        calcular_total_correto(valor_compra)
    )

    resultado_esta_correto = (
        abs(total_incorreto - total_esperado) < 0.001
    )

    st.divider()

    st.subheader("Resultado apresentado pelo sistema")

    coluna_1, coluna_2, coluna_3 = st.columns(3)

    with coluna_1:
        st.metric(
            label="Valor da compra",
            value=formatar_moeda(valor_compra),
        )

    with coluna_2:
        st.metric(
            label="Desconto aplicado pelo sistema",
            value=formatar_moeda(desconto_incorreto),
        )

    with coluna_3:
        st.metric(
            label="Total apresentado pelo sistema",
            value=formatar_moeda(total_incorreto),
        )

    if resultado_esta_correto:
        st.success(
            """
            ### Resultado correto para este caso

            Para este valor específico, o sistema apresentou o
            resultado esperado.

            Teste agora uma compra de exatamente **R$ 500,00** ou uma
            compra superior a esse valor para visualizar a falha.
            """
        )

    else:
        st.error(
            """
            ### Falha funcional identificada

            A aplicação foi executada sem apresentar erro técnico,
            mas o resultado não atende ao requisito definido pelo cliente.
            """
        )

        st.subheader("Comparação dos resultados")

        coluna_sistema, coluna_requisito = st.columns(2)

        with coluna_sistema:
            with st.container(border=True):
                st.markdown("### ❌ Resultado do sistema")

                st.write(
                    "Desconto aplicado:"
                )

                st.error(
                    formatar_moeda(desconto_incorreto)
                )

                st.write(
                    "Total calculado:"
                )

                st.error(
                    formatar_moeda(total_incorreto)
                )

        with coluna_requisito:
            with st.container(border=True):
                st.markdown("### ✅ Resultado esperado")

                st.write(
                    "Desconto correto:"
                )

                st.success(
                    formatar_moeda(desconto_esperado)
                )

                st.write(
                    "Total correto:"
                )

                st.success(
                    formatar_moeda(total_esperado)
                )

        diferenca = total_incorreto - total_esperado

        if diferenca > 0:
            st.warning(
                f"""
                Devido à falha, o cliente está pagando
                **{formatar_moeda(diferenca)} a mais**.
                """
            )

        elif diferenca < 0:
            st.warning(
                f"""
                Devido à falha, a loja está cobrando
                **{formatar_moeda(abs(diferenca))} a menos**.
                """
            )


st.divider()


# =========================================================
# EXPLICAÇÃO DA FALHA
# =========================================================
st.header(
    "Por que essa é uma falha de Adequação Funcional?"
)

st.write(
    """
    O programa não apresenta erro de sintaxe, não encerra inesperadamente
    e consegue realizar um cálculo.

    Entretanto, o resultado não corresponde ao requisito solicitado.

    Portanto, o problema não é que o sistema deixou de executar.
    O problema é que ele executou uma regra de negócio incorreta.
    """
)

falha_1, falha_2 = st.columns(2)

with falha_1:
    with st.container(border=True):
        st.subheader("❌ Falha 1: condição incorreta")

        st.code(
            """
if valor_compra > 500:
    percentual_desconto = 0.05
            """.strip(),
            language="python",
        )

        st.write(
            """
            O operador `>` exclui uma compra de exatamente
            R$ 500,00.

            O requisito determina que o desconto seja aplicado a
            partir de R$ 500,00. Portanto, o operador correto seria
            `>=`.
            """
        )

with falha_2:
    with st.container(border=True):
        st.subheader("❌ Falha 2: percentual incorreto")

        st.code(
            """
percentual_desconto = 0.05
            """.strip(),
            language="python",
        )

        st.write(
            """
            O sistema aplica 5% de desconto, mas o requisito determina
            10%.

            O software executa o cálculo, porém utiliza uma regra de
            negócio diferente daquela definida pelo cliente.
            """
        )


st.divider()


# =========================================================
# CASOS DE TESTE
# =========================================================
st.header("Casos de teste")

casos_teste = [
    {
        "Valor da compra": formatar_moeda(400.00),
        "Desconto esperado": formatar_moeda(0.00),
        "Desconto aplicado": formatar_moeda(0.00),
        "Total esperado": formatar_moeda(400.00),
        "Total calculado": formatar_moeda(400.00),
        "Situação": "✅ Correto",
    },
    {
        "Valor da compra": formatar_moeda(500.00),
        "Desconto esperado": formatar_moeda(50.00),
        "Desconto aplicado": formatar_moeda(0.00),
        "Total esperado": formatar_moeda(450.00),
        "Total calculado": formatar_moeda(500.00),
        "Situação": "❌ Falha",
    },
    {
        "Valor da compra": formatar_moeda(1000.00),
        "Desconto esperado": formatar_moeda(100.00),
        "Desconto aplicado": formatar_moeda(50.00),
        "Total esperado": formatar_moeda(900.00),
        "Total calculado": formatar_moeda(950.00),
        "Situação": "❌ Falha",
    },
]

st.dataframe(
    casos_teste,
    use_container_width=True,
    hide_index=True,
)


st.divider()


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos da falha")

impacto_1, impacto_2 = st.columns(2)

with impacto_1:
    with st.container(border=True):
        st.subheader("Impactos para o cliente")

        st.markdown(
            """
            - pagamento de valor incorreto;
            - insatisfação com a empresa;
            - necessidade de solicitar correção;
            - perda de confiança;
            - experiência negativa.
            """
        )

with impacto_2:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - descumprimento das regras do negócio;
            - reclamações de clientes;
            - necessidade de estornos;
            - aumento dos chamados de suporte;
            - retrabalho;
            - possível perda financeira;
            - prejuízo à reputação.
            """
        )


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir essa falha?")

metrica_1, metrica_2, metrica_3 = st.columns(3)

with metrica_1:
    st.metric(
        label="Casos testados",
        value="3",
    )

with metrica_2:
    st.metric(
        label="Casos com falha",
        value="2",
    )

with metrica_3:
    st.metric(
        label="Taxa de sucesso",
        value="33,33%",
    )

st.info(
    """
    Uma possível métrica é o **percentual de casos de teste atendidos
    corretamente**.

    A fórmula utilizada pode ser:

    **Taxa de sucesso = casos corretos ÷ total de casos × 100**

    Neste exemplo:

    **1 ÷ 3 × 100 = 33,33%**
    """
)


st.divider()


# =========================================================
# CÓDIGO COM A FALHA
# =========================================================
st.header("Código com a falha")

with st.expander(
    "Visualizar implementação incorreta",
    expanded=True,
):
    st.code(
        """
def calcular_total_com_falha(valor_compra):
    percentual_desconto = 0.0

    if valor_compra > 500:
        percentual_desconto = 0.05

    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final
        """.strip(),
        language="python",
    )


# =========================================================
# CÓDIGO CORRIGIDO
# =========================================================
st.header("Como corrigir?")

st.write(
    """
    A correção deve seguir exatamente a regra definida pelo cliente:

    - utilizar `>=` para incluir compras de exatamente R$ 500,00;
    - utilizar `0.10` para representar 10% de desconto.
    """
)

with st.expander(
    "Visualizar implementação corrigida",
    expanded=True,
):
    st.code(
        """
def calcular_total_correto(valor_compra):
    percentual_desconto = 0.0

    if valor_compra >= 500:
        percentual_desconto = 0.10

    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final
        """.strip(),
        language="python",
    )


st.divider()


# =========================================================
# COMPARAÇÃO ENTRE OS CÓDIGOS
# =========================================================
st.header("Comparação da correção")

codigo_falha, codigo_correto = st.columns(2)

with codigo_falha:
    with st.container(border=True):
        st.subheader("❌ Implementação com falha")

        st.code(
            """
if valor_compra > 500:
    percentual_desconto = 0.05
            """.strip(),
            language="python",
        )

with codigo_correto:
    with st.container(border=True):
        st.subheader("✅ Implementação corrigida")

        st.code(
            """
if valor_compra >= 500:
    percentual_desconto = 0.10
            """.strip(),
            language="python",
        )


st.divider()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um software funcionalmente adequado não deve apenas executar
    sem apresentar erros.

    Ele precisa entregar o resultado correto, utilizando os requisitos
    e as regras de negócio definidos pelo cliente.
    """
)


# =========================================================
# BOTÃO FINAL
# =========================================================
if st.button(
    "🏠 Voltar para a página inicial",
    key="voltar_inicio_final",
    use_container_width=True,
):
    voltar_para_inicio()