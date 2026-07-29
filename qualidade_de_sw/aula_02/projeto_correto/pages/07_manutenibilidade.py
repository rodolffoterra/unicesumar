import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Tuple

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Manutenibilidade",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"

DESCONTO_ANTIGO = 0.10
DESCONTO_NOVO = 0.15

VALOR_PADRAO_PEDIDO = 1000.00


# =========================================================
# MODELO DE DADOS
# =========================================================
@dataclass
class ResultadoCalculo:
    """
    Representa o resultado de um cálculo de desconto.
    """

    origem: str
    valor_original: float
    percentual_desconto: float
    valor_desconto: float
    valor_final: float


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_sistema_dificil" not in st.session_state:
    st.session_state.resultado_sistema_dificil = None

if "resultado_sistema_manutenivel" not in st.session_state:
    st.session_state.resultado_sistema_manutenivel = None

if "testes_manutenibilidade" not in st.session_state:
    st.session_state.testes_manutenibilidade = None


# =========================================================
# NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página principal.
    """

    st.switch_page(PAGINA_INICIAL)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def formatar_moeda(valor: float) -> str:
    """
    Formata um valor monetário no padrão brasileiro.
    """

    valor_formatado = (
        f"{valor:,.2f}"
        .replace(",", "TEMP")
        .replace(".", ",")
        .replace("TEMP", ".")
    )

    return f"R$ {valor_formatado}"


def formatar_percentual(percentual: float) -> str:
    """
    Formata um percentual decimal.
    """

    return f"{percentual * 100:.0f}%"


def formatar_tempo(segundos: float) -> str:
    """
    Formata o tempo de execução.
    """

    if segundos >= 1:
        return f"{segundos:.2f} segundos"

    return f"{segundos * 1000:.2f} ms"


def criar_resultado(
    origem: str,
    valor_original: float,
    percentual_desconto: float,
) -> ResultadoCalculo:
    """
    Cria um resultado padronizado para a demonstração.
    """

    valor_desconto = valor_original * percentual_desconto
    valor_final = valor_original - valor_desconto

    return ResultadoCalculo(
        origem=origem,
        valor_original=valor_original,
        percentual_desconto=percentual_desconto,
        valor_desconto=valor_desconto,
        valor_final=valor_final,
    )


def resultado_para_dicionario(
    resultado: ResultadoCalculo,
) -> Dict[str, str]:
    """
    Converte o resultado para exibição em tabela.
    """

    return {
        "Origem": resultado.origem,
        "Valor original": formatar_moeda(
            resultado.valor_original
        ),
        "Desconto aplicado": formatar_percentual(
            resultado.percentual_desconto
        ),
        "Valor do desconto": formatar_moeda(
            resultado.valor_desconto
        ),
        "Valor final": formatar_moeda(
            resultado.valor_final
        ),
    }


# =========================================================
# SISTEMA DIFÍCIL DE MANTER
# =========================================================
def calcular_desconto_tela(
    valor: float,
) -> ResultadoCalculo:
    """
    Simula uma tela que foi atualizada para a nova regra de 15%.
    """

    desconto = 0.15

    return criar_resultado(
        origem="Tela de vendas",
        valor_original=valor,
        percentual_desconto=desconto,
    )


def calcular_desconto_relatorio(
    valor: float,
) -> ResultadoCalculo:
    """
    Simula um relatório que ainda utiliza a regra antiga de 10%.
    """

    desconto = 0.10

    return criar_resultado(
        origem="Relatório financeiro",
        valor_original=valor,
        percentual_desconto=desconto,
    )


def calcular_desconto_email(
    valor: float,
) -> ResultadoCalculo:
    """
    Simula um e-mail que ainda utiliza a regra antiga de 10%.
    """

    desconto = 0.10

    return criar_resultado(
        origem="E-mail do cliente",
        valor_original=valor,
        percentual_desconto=desconto,
    )


def executar_sistema_dificil(
    valor: float,
) -> Dict[str, Any]:
    """
    Executa o sistema com regras duplicadas.

    Apenas uma das três funções foi atualizada para o novo desconto.
    """

    inicio = time.perf_counter()

    etapas = [
        "Localizando regras de desconto...",
        "Atualizando a tela de vendas...",
        "Executando o relatório...",
        "Gerando a comunicação ao cliente...",
        "Comparando os resultados...",
    ]

    barra = st.progress(0)
    status = st.empty()

    for indice, etapa in enumerate(etapas, start=1):
        percentual = int(
            (indice / len(etapas)) * 100
        )

        status.info(f"⏳ {etapa}")

        barra.progress(
            percentual,
            text=f"Manutenção: {percentual}%",
        )

        time.sleep(0.25)

    resultados = [
        calcular_desconto_tela(valor),
        calcular_desconto_relatorio(valor),
        calcular_desconto_email(valor),
    ]

    percentuais_encontrados = {
        resultado.percentual_desconto
        for resultado in resultados
    }

    consistente = len(percentuais_encontrados) == 1

    tempo_total = time.perf_counter() - inicio

    if consistente:
        status.success(
            "✅ Todas as partes utilizaram a mesma regra."
        )
    else:
        status.error(
            "❌ A alteração gerou resultados inconsistentes."
        )

    return {
        "sucesso": consistente,
        "resultados": resultados,
        "tempo": tempo_total,
        "arquivos_alterados": 1,
        "locais_com_regra": 3,
        "locais_esquecidos": 2,
        "percentuais_encontrados": sorted(
            percentuais_encontrados
        ),
        "mensagem": (
            "A regra estava duplicada em três locais. "
            "Somente a tela de vendas foi atualizada."
        ),
    }


# =========================================================
# SISTEMA MANUTENÍVEL
# =========================================================
class PoliticaDesconto:
    """
    Centraliza a regra de desconto.

    Todos os componentes consultam a mesma política.
    """

    def __init__(self, percentual: float) -> None:
        if percentual < 0 or percentual > 1:
            raise ValueError(
                "O percentual deve estar entre 0 e 1."
            )

        self.percentual = percentual

    def calcular(
        self,
        valor: float,
        origem: str,
    ) -> ResultadoCalculo:
        """
        Calcula o desconto utilizando a regra centralizada.
        """

        if valor < 0:
            raise ValueError(
                "O valor do pedido não pode ser negativo."
            )

        return criar_resultado(
            origem=origem,
            valor_original=valor,
            percentual_desconto=self.percentual,
        )


def gerar_resultados_manuteniveis(
    valor: float,
    politica: PoliticaDesconto,
) -> List[ResultadoCalculo]:
    """
    Utiliza a mesma política em todos os componentes.
    """

    origens = [
        "Tela de vendas",
        "Relatório financeiro",
        "E-mail do cliente",
    ]

    return [
        politica.calcular(
            valor=valor,
            origem=origem,
        )
        for origem in origens
    ]


def executar_sistema_manutenivel(
    valor: float,
) -> Dict[str, Any]:
    """
    Executa o sistema com a regra centralizada.
    """

    inicio = time.perf_counter()

    etapas = [
        "Localizando o módulo de desconto...",
        "Atualizando a política central...",
        "Executando os testes...",
        "Aplicando a regra nos componentes...",
        "Validando a consistência...",
    ]

    barra = st.progress(0)
    status = st.empty()

    for indice, etapa in enumerate(etapas, start=1):
        percentual = int(
            (indice / len(etapas)) * 100
        )

        status.info(f"⏳ {etapa}")

        barra.progress(
            percentual,
            text=f"Manutenção: {percentual}%",
        )

        time.sleep(0.20)

    politica = PoliticaDesconto(
        percentual=DESCONTO_NOVO
    )

    resultados = gerar_resultados_manuteniveis(
        valor=valor,
        politica=politica,
    )

    percentuais_encontrados = {
        resultado.percentual_desconto
        for resultado in resultados
    }

    consistente = (
        len(percentuais_encontrados) == 1
        and DESCONTO_NOVO in percentuais_encontrados
    )

    tempo_total = time.perf_counter() - inicio

    if consistente:
        status.success(
            "✅ Todos os componentes foram atualizados."
        )
    else:
        status.error(
            "❌ A regra não foi aplicada corretamente."
        )

    return {
        "sucesso": consistente,
        "resultados": resultados,
        "tempo": tempo_total,
        "arquivos_alterados": 1,
        "locais_com_regra": 1,
        "locais_esquecidos": 0,
        "percentuais_encontrados": sorted(
            percentuais_encontrados
        ),
        "mensagem": (
            "A regra foi alterada em um único módulo e reutilizada "
            "por todos os componentes."
        ),
    }


# =========================================================
# TESTES AUTOMATIZADOS
# =========================================================
def executar_teste(
    nome: str,
    funcao: Callable[[], None],
) -> Dict[str, str]:
    """
    Executa um teste e retorna seu resultado.
    """

    try:
        funcao()

        return {
            "Teste": nome,
            "Resultado": "✅ Aprovado",
            "Detalhes": "Comportamento conforme o esperado.",
        }

    except AssertionError as erro:
        return {
            "Teste": nome,
            "Resultado": "❌ Reprovado",
            "Detalhes": str(erro),
        }

    except Exception as erro:
        return {
            "Teste": nome,
            "Resultado": "⚠️ Erro",
            "Detalhes": str(erro),
        }


def teste_desconto_15_porcento() -> None:
    """
    Verifica o cálculo de desconto de 15%.
    """

    politica = PoliticaDesconto(0.15)

    resultado = politica.calcular(
        valor=1000.00,
        origem="Teste",
    )

    assert resultado.valor_desconto == 150.00, (
        "O desconto deveria ser R$ 150,00."
    )

    assert resultado.valor_final == 850.00, (
        "O valor final deveria ser R$ 850,00."
    )


def teste_valor_zero() -> None:
    """
    Verifica o comportamento com pedido de valor zero.
    """

    politica = PoliticaDesconto(0.15)

    resultado = politica.calcular(
        valor=0.00,
        origem="Teste",
    )

    assert resultado.valor_final == 0.00, (
        "O valor final deveria permanecer zero."
    )


def teste_valor_negativo() -> None:
    """
    Verifica se valores negativos são rejeitados.
    """

    politica = PoliticaDesconto(0.15)

    erro_identificado = False

    try:
        politica.calcular(
            valor=-100.00,
            origem="Teste",
        )

    except ValueError:
        erro_identificado = True

    assert erro_identificado, (
        "O sistema deveria rejeitar valores negativos."
    )


def teste_consistencia_componentes() -> None:
    """
    Verifica se todos os componentes utilizam a mesma regra.
    """

    politica = PoliticaDesconto(0.15)

    resultados = gerar_resultados_manuteniveis(
        valor=1000.00,
        politica=politica,
    )

    percentuais = {
        resultado.percentual_desconto
        for resultado in resultados
    }

    assert percentuais == {0.15}, (
        "Os componentes utilizaram percentuais diferentes."
    )


def executar_testes_automatizados() -> Dict[str, Any]:
    """
    Executa a suíte didática de testes.
    """

    inicio = time.perf_counter()

    testes = [
        executar_teste(
            nome="Cálculo de desconto de 15%",
            funcao=teste_desconto_15_porcento,
        ),
        executar_teste(
            nome="Cálculo com valor zero",
            funcao=teste_valor_zero,
        ),
        executar_teste(
            nome="Rejeição de valor negativo",
            funcao=teste_valor_negativo,
        ),
        executar_teste(
            nome="Consistência entre componentes",
            funcao=teste_consistencia_componentes,
        ),
    ]

    aprovados = sum(
        1
        for teste in testes
        if teste["Resultado"] == "✅ Aprovado"
    )

    tempo_total = time.perf_counter() - inicio

    return {
        "testes": testes,
        "total": len(testes),
        "aprovados": aprovados,
        "reprovados": len(testes) - aprovados,
        "tempo": tempo_total,
        "sucesso": aprovados == len(testes),
    }


def reiniciar_demonstracao() -> None:
    """
    Limpa os resultados da página.
    """

    st.session_state.resultado_sistema_dificil = None
    st.session_state.resultado_sistema_manutenivel = None
    st.session_state.testes_manutenibilidade = None

    st.rerun()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🧰 Manutenibilidade")

    st.write(
        """
        Esta página demonstra como a organização do código afeta
        a facilidade e a segurança das alterações.
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

    st.subheader("Alteração solicitada")

    st.markdown(
        f"""
        A empresa alterou o desconto de:

        **{formatar_percentual(DESCONTO_ANTIGO)}**
        para
        **{formatar_percentual(DESCONTO_NOVO)}**
        """
    )

    st.subheader("Aspectos avaliados")

    st.markdown(
        """
        - modularidade;
        - reutilização;
        - facilidade de análise;
        - facilidade de modificação;
        - testabilidade;
        - consistência das alterações.
        """
    )

    st.warning(
        """
        A inconsistência do primeiro sistema é proposital e faz parte
        da demonstração.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🧰 Falha de Manutenibilidade")

st.write(
    """
    Nesta demonstração, dois sistemas precisam receber a mesma
    alteração de regra de negócio.

    A empresa aumentou o desconto promocional de 10% para 15%.

    O primeiro sistema possui código duplicado. O segundo utiliza uma
    regra centralizada e reutilizável.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Manutenibilidade?

    Manutenibilidade avalia o quanto um sistema pode ser analisado,
    corrigido, modificado, testado e evoluído com eficiência.

    Um sistema difícil de manter pode funcionar corretamente hoje,
    mas apresentar alto risco quando uma regra de negócio precisar
    ser alterada.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma loja possui três componentes que calculam o valor final de
    um pedido:

    - tela de vendas;
    - relatório financeiro;
    - e-mail enviado ao cliente.

    Inicialmente, os três componentes aplicavam desconto de 10%.
    A nova promoção exige desconto de 15%.
    """
)

st.success(
    """
    ### Requisito de manutenção

    A alteração do percentual de desconto deve ser realizada de forma
    rápida, segura e consistente em todos os componentes.
    """
)


st.divider()


# =========================================================
# ENTRADA DA DEMONSTRAÇÃO
# =========================================================
st.header("Configure a simulação")

valor_pedido = st.number_input(
    "Valor do pedido",
    min_value=0.00,
    value=VALOR_PADRAO_PEDIDO,
    step=50.00,
    format="%.2f",
    help=(
        "Esse valor será utilizado nos dois sistemas para permitir "
        "a comparação dos resultados."
    ),
)

coluna_regra_antiga, coluna_regra_nova = st.columns(2)

with coluna_regra_antiga:
    st.metric(
        label="Regra anterior",
        value=formatar_percentual(DESCONTO_ANTIGO),
    )

with coluna_regra_nova:
    st.metric(
        label="Nova regra",
        value=formatar_percentual(DESCONTO_NOVO),
        delta="+5 pontos percentuais",
    )


st.divider()


# =========================================================
# EXECUÇÃO
# =========================================================
st.header("Execute as demonstrações")

coluna_dificil, coluna_manutenivel = st.columns(2)


# =========================================================
# SISTEMA DIFÍCIL DE MANTER
# =========================================================
with coluna_dificil:
    with st.container(border=True):
        st.subheader("❌ Sistema difícil de manter")

        st.write(
            """
            A regra de desconto está repetida em três funções.

            O desenvolvedor encontrou e atualizou somente a regra
            utilizada pela tela de vendas.
            """
        )

        st.code(
            """
def calcular_tela(valor):
    desconto = 0.15

def calcular_relatorio(valor):
    desconto = 0.10

def calcular_email(valor):
    desconto = 0.10
            """.strip(),
            language="python",
        )

        executar_dificil = st.button(
            "Executar manutenção com código duplicado",
            key="executar_sistema_dificil",
            type="primary",
            use_container_width=True,
        )

        if executar_dificil:
            # Limpa o resultado do outro cenário.
            st.session_state.resultado_sistema_manutenivel = None
            st.session_state.testes_manutenibilidade = None

            st.session_state.resultado_sistema_dificil = (
                executar_sistema_dificil(valor_pedido)
            )

            st.rerun()


# =========================================================
# SISTEMA MANUTENÍVEL
# =========================================================
with coluna_manutenivel:
    with st.container(border=True):
        st.subheader("✅ Sistema manutenível")

        st.write(
            """
            A regra de desconto está centralizada em uma classe.

            Todos os componentes utilizam a mesma política para
            realizar seus cálculos.
            """
        )

        st.code(
            """
politica = PoliticaDesconto(
    percentual=0.15
)

tela = politica.calcular(valor)
relatorio = politica.calcular(valor)
email = politica.calcular(valor)
            """.strip(),
            language="python",
        )

        executar_manutenivel = st.button(
            "Executar manutenção modular",
            key="executar_sistema_manutenivel",
            use_container_width=True,
        )

        if executar_manutenivel:
            # Limpa o resultado do outro cenário.
            st.session_state.resultado_sistema_dificil = None
            st.session_state.testes_manutenibilidade = None

            st.session_state.resultado_sistema_manutenivel = (
                executar_sistema_manutenivel(valor_pedido)
            )

            st.rerun()


# =========================================================
# RESULTADO DO SISTEMA DIFÍCIL
# =========================================================
resultado_dificil = (
    st.session_state.resultado_sistema_dificil
)

if resultado_dificil is not None:
    st.divider()

    st.header("Resultado do sistema difícil de manter")

    if resultado_dificil["sucesso"]:
        st.success(
            "Todos os componentes aplicaram a mesma regra."
        )
    else:
        st.error(
            """
            ### Alteração inconsistente

            A tela de vendas aplicou a nova regra de 15%, mas o
            relatório e o e-mail continuaram aplicando 10%.
            """
        )

    metricas = st.columns(4)

    with metricas[0]:
        st.metric(
            label="Locais com a regra",
            value=str(
                resultado_dificil["locais_com_regra"]
            ),
        )

    with metricas[1]:
        st.metric(
            label="Arquivos alterados",
            value=str(
                resultado_dificil["arquivos_alterados"]
            ),
        )

    with metricas[2]:
        st.metric(
            label="Locais esquecidos",
            value=str(
                resultado_dificil["locais_esquecidos"]
            ),
        )

    with metricas[3]:
        st.metric(
            label="Tempo da alteração",
            value=formatar_tempo(
                resultado_dificil["tempo"]
            ),
        )

    dados_resultado_dificil = [
        resultado_para_dicionario(resultado)
        for resultado in resultado_dificil["resultados"]
    ]

    st.dataframe(
        dados_resultado_dificil,
        use_container_width=True,
        hide_index=True,
    )

    valores_finais = {
        resultado.valor_final
        for resultado in resultado_dificil["resultados"]
    }

    if len(valores_finais) > 1:
        diferenca = (
            max(valores_finais)
            - min(valores_finais)
        )

        st.error(
            f"""
            Para o mesmo pedido, o sistema apresentou valores
            diferentes.

            Diferença identificada: **{formatar_moeda(diferenca)}**.
            """
        )

    st.warning(
        resultado_dificil["mensagem"]
    )

    st.markdown(
        """
        **Possíveis consequências:**

        - o cliente visualiza um valor na tela;
        - o relatório registra outro valor;
        - o e-mail informa um terceiro resultado;
        - o setor financeiro precisa corrigir os dados manualmente;
        - a alteração gera uma falha em uma funcionalidade que antes
          funcionava.
        """
    )


# =========================================================
# RESULTADO DO SISTEMA MANUTENÍVEL
# =========================================================
resultado_manutenivel = (
    st.session_state.resultado_sistema_manutenivel
)

if resultado_manutenivel is not None:
    st.divider()

    st.header("Resultado do sistema manutenível")

    if resultado_manutenivel["sucesso"]:
        st.success(
            """
            ### Alteração concluída com sucesso

            A política foi modificada em um único local e todos os
            componentes passaram a utilizar o desconto de 15%.
            """
        )
    else:
        st.error(
            "A regra não foi aplicada de maneira consistente."
        )

    metricas = st.columns(4)

    with metricas[0]:
        st.metric(
            label="Locais com a regra",
            value=str(
                resultado_manutenivel["locais_com_regra"]
            ),
        )

    with metricas[1]:
        st.metric(
            label="Arquivos alterados",
            value=str(
                resultado_manutenivel["arquivos_alterados"]
            ),
        )

    with metricas[2]:
        st.metric(
            label="Locais esquecidos",
            value=str(
                resultado_manutenivel["locais_esquecidos"]
            ),
        )

    with metricas[3]:
        st.metric(
            label="Tempo da alteração",
            value=formatar_tempo(
                resultado_manutenivel["tempo"]
            ),
        )

    dados_resultado_manutenivel = [
        resultado_para_dicionario(resultado)
        for resultado in resultado_manutenivel["resultados"]
    ]

    st.dataframe(
        dados_resultado_manutenivel,
        use_container_width=True,
        hide_index=True,
    )

    valores_finais = {
        resultado.valor_final
        for resultado in resultado_manutenivel["resultados"]
    }

    if len(valores_finais) == 1:
        valor_final = next(iter(valores_finais))

        st.success(
            f"""
            Todos os componentes calcularam o mesmo valor final:
            **{formatar_moeda(valor_final)}**.
            """
        )

    st.info(
        resultado_manutenivel["mensagem"]
    )


st.divider()


# =========================================================
# TESTES AUTOMATIZADOS
# =========================================================
st.header("Testabilidade")

st.write(
    """
    Um código manutenível deve permitir que suas regras sejam testadas
    de forma isolada.

    Os testes abaixo verificam o cálculo, valores de limite, entradas
    inválidas e a consistência entre os componentes.
    """
)

if st.button(
    "🧪 Executar testes automatizados",
    key="executar_testes_manutenibilidade",
    use_container_width=True,
):
    with st.spinner("Executando os testes..."):
        time.sleep(0.5)

        st.session_state.testes_manutenibilidade = (
            executar_testes_automatizados()
        )

    st.rerun()


resultado_testes = (
    st.session_state.testes_manutenibilidade
)

if resultado_testes is not None:
    colunas_teste = st.columns(4)

    with colunas_teste[0]:
        st.metric(
            label="Testes executados",
            value=str(resultado_testes["total"]),
        )

    with colunas_teste[1]:
        st.metric(
            label="Testes aprovados",
            value=str(resultado_testes["aprovados"]),
        )

    with colunas_teste[2]:
        st.metric(
            label="Testes reprovados",
            value=str(resultado_testes["reprovados"]),
        )

    with colunas_teste[3]:
        st.metric(
            label="Tempo de execução",
            value=formatar_tempo(
                resultado_testes["tempo"]
            ),
        )

    st.dataframe(
        resultado_testes["testes"],
        use_container_width=True,
        hide_index=True,
    )

    if resultado_testes["sucesso"]:
        st.success(
            """
            Todos os testes foram aprovados. A alteração pode ser
            validada antes de ser disponibilizada aos usuários.
            """
        )
    else:
        st.error(
            """
            Existem testes reprovados. A alteração precisa ser
            corrigida antes da publicação.
            """
        )


st.divider()


# =========================================================
# COMPARAÇÃO
# =========================================================
st.header("Comparação das implementações")

comparacao = [
    {
        "Critério": "Localização da regra",
        "Código difícil": "Duplicada em vários locais",
        "Código manutenível": "Centralizada em um módulo",
    },
    {
        "Critério": "Quantidade de alterações",
        "Código difícil": "Várias alterações",
        "Código manutenível": "Uma alteração",
    },
    {
        "Critério": "Risco de esquecimento",
        "Código difícil": "Alto",
        "Código manutenível": "Baixo",
    },
    {
        "Critério": "Consistência",
        "Código difícil": "Pode gerar valores diferentes",
        "Código manutenível": "Todos utilizam a mesma regra",
    },
    {
        "Critério": "Reutilização",
        "Código difícil": "Código repetido",
        "Código manutenível": "Componente reutilizável",
    },
    {
        "Critério": "Testabilidade",
        "Código difícil": "Regra acoplada às telas",
        "Código manutenível": "Regra testada isoladamente",
    },
    {
        "Critério": "Impacto da mudança",
        "Código difícil": "Difícil de identificar",
        "Código manutenível": "Mais previsível",
    },
]

st.dataframe(
    comparacao,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# ASPECTOS DE MANUTENIBILIDADE
# =========================================================
st.header("Aspectos de Manutenibilidade demonstrados")

coluna_1, coluna_2, coluna_3 = st.columns(3)

with coluna_1:
    with st.container(border=True):
        st.subheader("Modularidade")

        st.write(
            """
            O sistema deve ser dividido em componentes bem definidos.

            Uma alteração em um módulo deve causar o menor impacto
            possível nos demais componentes.
            """
        )

    with st.container(border=True):
        st.subheader("Reutilização")

        st.write(
            """
            Componentes e funções devem poder ser reutilizados em
            diferentes partes do sistema sem duplicação de código.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("Analisabilidade")

        st.write(
            """
            Deve ser possível localizar uma regra, identificar a causa
            de uma falha e avaliar o impacto de uma alteração.
            """
        )

    with st.container(border=True):
        st.subheader("Modificabilidade")

        st.write(
            """
            O sistema deve permitir alterações sem introduzir defeitos
            ou exigir esforço desnecessário.
            """
        )

with coluna_3:
    with st.container(border=True):
        st.subheader("Testabilidade")

        st.write(
            """
            As regras devem ser estruturadas de maneira que possam ser
            testadas isoladamente e de forma automatizada.
            """
        )

    with st.container(border=True):
        st.subheader("Consistência")

        st.write(
            """
            A mesma regra de negócio deve produzir resultados
            equivalentes em todos os componentes que a utilizam.
            """
        )


st.divider()


# =========================================================
# CÓDIGO COM BAIXA MANUTENIBILIDADE
# =========================================================
st.header("Código com baixa manutenibilidade")

with st.expander(
    "Visualizar implementação com duplicação",
    expanded=True,
):
    st.code(
        """
def calcular_total_tela(valor):
    desconto = valor * 0.15
    return valor - desconto


def calcular_total_relatorio(valor):
    desconto = valor * 0.10
    return valor - desconto


def calcular_total_email(valor):
    desconto = valor * 0.10
    return valor - desconto
        """.strip(),
        language="python",
    )

st.error(
    """
    Problemas desta implementação:

    - a mesma regra aparece em vários locais;
    - não existe uma fonte única de verdade;
    - uma alteração precisa ser repetida;
    - é fácil esquecer uma das funções;
    - a lógica está acoplada aos componentes;
    - o risco de regressão é elevado.
    """
)


# =========================================================
# CÓDIGO MANUTENÍVEL
# =========================================================
st.header("Código com boa manutenibilidade")

with st.expander(
    "Visualizar implementação modular",
    expanded=True,
):
    st.code(
        """
from dataclasses import dataclass


@dataclass
class ResultadoDesconto:
    valor_original: float
    percentual: float
    valor_desconto: float
    valor_final: float


class PoliticaDesconto:
    def __init__(self, percentual: float):
        if percentual < 0 or percentual > 1:
            raise ValueError(
                "Percentual inválido."
            )

        self.percentual = percentual

    def calcular(
        self,
        valor: float,
    ) -> ResultadoDesconto:
        if valor < 0:
            raise ValueError(
                "O valor não pode ser negativo."
            )

        valor_desconto = (
            valor * self.percentual
        )

        return ResultadoDesconto(
            valor_original=valor,
            percentual=self.percentual,
            valor_desconto=valor_desconto,
            valor_final=valor - valor_desconto,
        )


politica = PoliticaDesconto(
    percentual=0.15
)

resultado_tela = politica.calcular(1000)
resultado_relatorio = politica.calcular(1000)
resultado_email = politica.calcular(1000)
        """.strip(),
        language="python",
    )

st.success(
    """
    A implementação modular possui uma única política de desconto.

    Quando o percentual muda, todos os componentes passam a utilizar
    automaticamente a nova regra.
    """
)


st.divider()


# =========================================================
# EXEMPLO DE TESTE
# =========================================================
st.header("Exemplo de teste unitário")

with st.expander(
    "Visualizar teste com pytest",
    expanded=False,
):
    st.code(
        """
import pytest

from desconto import PoliticaDesconto


def test_deve_aplicar_desconto_de_15_porcento():
    politica = PoliticaDesconto(
        percentual=0.15
    )

    resultado = politica.calcular(1000)

    assert resultado.valor_desconto == 150
    assert resultado.valor_final == 850


def test_deve_rejeitar_valor_negativo():
    politica = PoliticaDesconto(
        percentual=0.15
    )

    with pytest.raises(ValueError):
        politica.calcular(-100)
        """.strip(),
        language="python",
    )


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Manutenibilidade?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Duplicação de código",
        value="Percentual",
    )

with metrica_2:
    st.metric(
        label="Cobertura de testes",
        value="Percentual",
    )

with metrica_3:
    st.metric(
        label="Complexidade",
        value="Ciclomática",
    )

with metrica_4:
    st.metric(
        label="Tempo de alteração",
        value="Horas ou dias",
    )

st.info(
    """
    Algumas métricas que podem ser utilizadas:

    - percentual de código duplicado;
    - complexidade ciclomática;
    - quantidade de dependências entre módulos;
    - cobertura de testes automatizados;
    - tempo médio para localizar uma falha;
    - tempo médio para implementar uma alteração;
    - quantidade de arquivos modificados por mudança;
    - taxa de defeitos introduzidos após alterações;
    - quantidade de regressões;
    - percentual de componentes reutilizáveis;
    - quantidade de métodos ou funções muito extensas;
    - frequência de alterações no mesmo arquivo.
    """
)


st.divider()


# =========================================================
# OUTROS EXEMPLOS
# =========================================================
st.header("Outros exemplos de baixa manutenibilidade")

exemplo_1, exemplo_2, exemplo_3 = st.columns(3)

with exemplo_1:
    with st.container(border=True):
        st.subheader("Função muito extensa")

        st.write(
            """
            Uma única função realiza validação, cálculo, acesso ao banco,
            envio de e-mail e geração de relatório.
            """
        )

with exemplo_2:
    with st.container(border=True):
        st.subheader("Nomes pouco claros")

        st.write(
            """
            Variáveis como `x`, `tmp`, `valor2` e `dados_final_novo`
            dificultam a compreensão do código.
            """
        )

with exemplo_3:
    with st.container(border=True):
        st.subheader("Alto acoplamento")

        st.write(
            """
            Uma pequena alteração em um módulo exige mudanças em várias
            partes não relacionadas do sistema.
            """
        )


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de um sistema difícil de manter")

coluna_usuario, coluna_empresa = st.columns(2)

with coluna_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - resultados inconsistentes;
            - erros após atualizações;
            - demora na correção de problemas;
            - funcionalidades indisponíveis;
            - comportamento diferente entre telas;
            - perda de confiança no sistema.
            """
        )

with coluna_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - maior custo de desenvolvimento;
            - alterações mais demoradas;
            - aumento de defeitos;
            - risco de regressões;
            - dificuldade de evolução;
            - dependência de determinados desenvolvedores;
            - atraso na entrega de novas funcionalidades;
            - aumento da dívida técnica.
            """
        )


st.divider()


# =========================================================
# BOAS PRÁTICAS
# =========================================================
st.header("Boas práticas de Manutenibilidade")

st.markdown(
    """
    - centralizar regras de negócio;
    - evitar duplicação de código;
    - criar funções com responsabilidades bem definidas;
    - utilizar nomes claros;
    - separar interface, regra de negócio e acesso a dados;
    - limitar o acoplamento entre módulos;
    - utilizar testes automatizados;
    - documentar decisões importantes;
    - aplicar padrões de projeto quando necessários;
    - realizar revisão de código;
    - utilizar análise estática;
    - remover código não utilizado;
    - refatorar continuamente;
    - manter dependências atualizadas;
    - controlar alterações com Git.
    """
)

st.warning(
    """
    Manutenibilidade não significa criar uma grande quantidade de
    classes ou abstrações.

    Abstrações desnecessárias também tornam o sistema difícil de
    compreender. A estrutura deve ser simples e proporcional ao
    problema resolvido.
    """
)


st.divider()


# =========================================================
# REINICIAR
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_manutenibilidade",
    use_container_width=True,
):
    reiniciar_demonstracao()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema manutenível permite localizar, alterar e testar uma
    regra com menor esforço e menor risco.

    Na implementação com código duplicado, a alteração de 10% para 15%
    foi aplicada somente na tela de vendas. O relatório e o e-mail
    permaneceram com a regra antiga, gerando resultados inconsistentes.

    Na implementação modular, a política de desconto foi modificada em
    um único local. Todos os componentes utilizaram automaticamente a
    nova regra e puderam ser validados por testes automatizados.
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