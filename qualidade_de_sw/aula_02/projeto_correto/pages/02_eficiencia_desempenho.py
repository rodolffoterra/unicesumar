import time
from datetime import datetime
from typing import Dict, List

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Eficiência de Desempenho",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
TEMPO_SISTEMA_LENTO = 10.0
TEMPO_SISTEMA_OTIMIZADO = 0.5
QUANTIDADE_ETAPAS = 10


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_lento" not in st.session_state:
    st.session_state.resultado_lento = None

if "resultado_otimizado" not in st.session_state:
    st.session_state.resultado_otimizado = None


# =========================================================
# FUNÇÕES DE NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página principal.
    """

    st.switch_page("app.py")


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


def formatar_tempo(segundos: float) -> str:
    """
    Formata o tempo de execução.
    """

    if segundos >= 1:
        return f"{segundos:.2f} segundos"

    milissegundos = segundos * 1000

    return f"{milissegundos:.0f} milissegundos"


def criar_barra_textual(percentual: int) -> str:
    """
    Cria uma barra textual com dez posições.

    Exemplo:
    ███░░░░░░░ 30%
    """

    quantidade_preenchida = percentual // 10
    quantidade_vazia = 10 - quantidade_preenchida

    barra = (
        "█" * quantidade_preenchida
        + "░" * quantidade_vazia
    )

    return f"{barra} {percentual}%"


def gerar_dados_relatorio() -> List[Dict[str, object]]:
    """
    Gera dados fictícios para o relatório.

    As duas implementações utilizam os mesmos dados para que
    o resultado final seja exatamente igual.
    """

    return [
        {
            "Produto": "Notebook Corporativo",
            "Quantidade": 18,
            "Valor unitário": 4250.00,
            "Total": 76500.00,
        },
        {
            "Produto": "Monitor 27 polegadas",
            "Quantidade": 32,
            "Valor unitário": 1650.00,
            "Total": 52800.00,
        },
        {
            "Produto": "Teclado sem fio",
            "Quantidade": 75,
            "Valor unitário": 280.00,
            "Total": 21000.00,
        },
        {
            "Produto": "Mouse ergonômico",
            "Quantidade": 90,
            "Valor unitário": 190.00,
            "Total": 17100.00,
        },
        {
            "Produto": "Cadeira de escritório",
            "Quantidade": 24,
            "Valor unitário": 1850.00,
            "Total": 44400.00,
        },
    ]


def calcular_resumo(
    dados: List[Dict[str, object]],
) -> Dict[str, object]:
    """
    Calcula as métricas apresentadas no relatório.
    """

    quantidade_total = sum(
        int(item["Quantidade"])
        for item in dados
    )

    valor_total = sum(
        float(item["Total"])
        for item in dados
    )

    quantidade_produtos = len(dados)

    ticket_medio = (
        valor_total / quantidade_total
        if quantidade_total > 0
        else 0
    )

    return {
        "quantidade_produtos": quantidade_produtos,
        "quantidade_total": quantidade_total,
        "valor_total": valor_total,
        "ticket_medio": ticket_medio,
    }


def executar_processamento(
    tempo_total: float,
    titulo: str,
    mensagem_final: str,
) -> Dict[str, object]:
    """
    Executa uma simulação visual de processamento.

    A barra é atualizada em dez etapas.
    """

    espaco_status = st.empty()
    barra_progresso = st.progress(0)
    espaco_barra_textual = st.empty()
    espaco_etapa = st.empty()

    tempo_por_etapa = tempo_total / QUANTIDADE_ETAPAS

    inicio = time.perf_counter()

    etapas = [
        "Conectando ao banco de dados",
        "Consultando registros de vendas",
        "Carregando informações dos produtos",
        "Validando registros",
        "Calculando valores unitários",
        "Calculando valores totais",
        "Agrupando informações",
        "Gerando indicadores",
        "Formatando o relatório",
        "Finalizando processamento",
    ]

    espaco_status.info(f"⏳ {titulo}")

    for indice, etapa in enumerate(etapas, start=1):
        percentual = indice * 10

        espaco_etapa.write(
            f"**Etapa {indice} de {QUANTIDADE_ETAPAS}:** {etapa}"
        )

        espaco_barra_textual.code(
            criar_barra_textual(percentual),
            language=None,
        )

        barra_progresso.progress(
            percentual,
            text=f"Processamento: {percentual}%",
        )

        time.sleep(tempo_por_etapa)

    tempo_execucao = time.perf_counter() - inicio

    dados = gerar_dados_relatorio()
    resumo = calcular_resumo(dados)

    espaco_status.success(f"✅ {mensagem_final}")
    espaco_etapa.empty()

    return {
        "tempo": tempo_execucao,
        "dados": dados,
        "resumo": resumo,
        "data_execucao": datetime.now().strftime(
            "%d/%m/%Y às %H:%M:%S"
        ),
    }


def exibir_relatorio(
    resultado: Dict[str, object],
    titulo: str,
) -> None:
    """
    Exibe o relatório gerado pelo processamento.
    """

    st.subheader(titulo)

    resumo = resultado["resumo"]

    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

    with coluna_1:
        st.metric(
            label="Produtos",
            value=str(resumo["quantidade_produtos"]),
        )

    with coluna_2:
        st.metric(
            label="Itens vendidos",
            value=str(resumo["quantidade_total"]),
        )

    with coluna_3:
        st.metric(
            label="Valor total",
            value=formatar_moeda(resumo["valor_total"]),
        )

    with coluna_4:
        st.metric(
            label="Valor médio por item",
            value=formatar_moeda(resumo["ticket_medio"]),
        )

    dados_formatados = []

    for item in resultado["dados"]:
        dados_formatados.append(
            {
                "Produto": item["Produto"],
                "Quantidade": item["Quantidade"],
                "Valor unitário": formatar_moeda(
                    item["Valor unitário"]
                ),
                "Total": formatar_moeda(item["Total"]),
            }
        )

    st.dataframe(
        dados_formatados,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        f"Relatório gerado em {resultado['data_execucao']}."
    )


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("⚡ Eficiência")

    st.markdown(
        """
        Esta página demonstra como o tempo de resposta influencia
        a qualidade de um software.
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

    st.subheader("Demonstrações")

    st.markdown(
        """
        **Sistema com falha**

        Demora aproximadamente 10 segundos para gerar o relatório.

        **Sistema otimizado**

        Gera o mesmo relatório em aproximadamente 0,5 segundo.
        """
    )

    st.warning(
        """
        Os atrasos desta demonstração são propositais e possuem
        finalidade didática.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("⚡ Falha de Eficiência de Desempenho")

st.markdown(
    """
    Nesta demonstração, dois sistemas executam a mesma função e
    entregam exatamente o mesmo relatório.

    A diferença está no tempo necessário para responder ao usuário.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Eficiência de Desempenho?

    Eficiência de Desempenho avalia se o sistema utiliza adequadamente
    tempo, memória, processamento e outros recursos disponíveis.

    Um software pode produzir o resultado correto e ainda apresentar
    baixa qualidade quando demora excessivamente para responder.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Um funcionário precisa gerar um relatório de vendas.

    O requisito estabelece que o relatório deve ficar disponível em
    até **2 segundos**.
    """
)

st.success(
    """
    ### Requisito de desempenho

    O relatório deve ser gerado corretamente e apresentado ao usuário
    em no máximo **2 segundos**.
    """
)

st.warning(
    """
    ### Falha apresentada

    A primeira implementação demora aproximadamente **10 segundos**.

    Mesmo entregando o relatório correto, ela não atende ao requisito
    de tempo de resposta.
    """
)


st.divider()


# =========================================================
# DEMONSTRAÇÕES
# =========================================================
st.header("Execute as demonstrações")

coluna_lenta, coluna_otimizada = st.columns(2)


# =========================================================
# SISTEMA LENTO
# =========================================================
with coluna_lenta:
    with st.container(border=True):
        st.subheader("❌ Sistema com falha")

        st.write(
            """
            Esta versão simula uma implementação com consultas lentas,
            processamento repetido e operações desnecessárias.
            """
        )

        st.metric(
            label="Tempo previsto",
            value="10 segundos",
            delta="8 segundos acima do requisito",
            delta_color="inverse",
        )

        executar_lento = st.button(
            "Gerar relatório — versão lenta",
            key="executar_sistema_lento",
            type="primary",
            use_container_width=True,
        )

        if executar_lento:
            st.session_state.resultado_lento = (
                executar_processamento(
                    tempo_total=TEMPO_SISTEMA_LENTO,
                    titulo=(
                        "O sistema lento está gerando o relatório..."
                    ),
                    mensagem_final=(
                        "Relatório gerado pela versão lenta."
                    ),
                )
            )


# =========================================================
# SISTEMA OTIMIZADO
# =========================================================
with coluna_otimizada:
    with st.container(border=True):
        st.subheader("✅ Sistema otimizado")

        st.write(
            """
            Esta versão simula uma implementação com consultas
            otimizadas, reaproveitamento de resultados e menos
            processamento.
            """
        )

        st.metric(
            label="Tempo previsto",
            value="0,5 segundo",
            delta="Dentro do requisito",
            delta_color="normal",
        )

        executar_otimizado = st.button(
            "Gerar relatório — versão otimizada",
            key="executar_sistema_otimizado",
            use_container_width=True,
        )

        if executar_otimizado:
            st.session_state.resultado_otimizado = (
                executar_processamento(
                    tempo_total=TEMPO_SISTEMA_OTIMIZADO,
                    titulo=(
                        "O sistema otimizado está gerando o relatório..."
                    ),
                    mensagem_final=(
                        "Relatório gerado pela versão otimizada."
                    ),
                )
            )


# =========================================================
# RESULTADO DO SISTEMA LENTO
# =========================================================
if st.session_state.resultado_lento is not None:
    st.divider()

    exibir_relatorio(
        resultado=st.session_state.resultado_lento,
        titulo="Relatório da versão lenta",
    )


# =========================================================
# RESULTADO DO SISTEMA OTIMIZADO
# =========================================================
if st.session_state.resultado_otimizado is not None:
    st.divider()

    exibir_relatorio(
        resultado=st.session_state.resultado_otimizado,
        titulo="Relatório da versão otimizada",
    )


# =========================================================
# COMPARAÇÃO
# =========================================================
if (
    st.session_state.resultado_lento is not None
    and st.session_state.resultado_otimizado is not None
):
    st.divider()

    st.header("Comparação de desempenho")

    tempo_lento = st.session_state.resultado_lento["tempo"]
    tempo_otimizado = (
        st.session_state.resultado_otimizado["tempo"]
    )

    economia_tempo = tempo_lento - tempo_otimizado

    percentual_melhoria = (
        (economia_tempo / tempo_lento) * 100
        if tempo_lento > 0
        else 0
    )

    quantidade_vezes = (
        tempo_lento / tempo_otimizado
        if tempo_otimizado > 0
        else 0
    )

    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

    with coluna_1:
        st.metric(
            label="Versão lenta",
            value=formatar_tempo(tempo_lento),
        )

    with coluna_2:
        st.metric(
            label="Versão otimizada",
            value=formatar_tempo(tempo_otimizado),
        )

    with coluna_3:
        st.metric(
            label="Tempo economizado",
            value=formatar_tempo(economia_tempo),
        )

    with coluna_4:
        st.metric(
            label="Melhoria aproximada",
            value=f"{percentual_melhoria:.1f}%",
        )

    st.success(
        f"""
        A versão otimizada foi aproximadamente
        **{quantidade_vezes:.1f} vezes mais rápida**.

        As duas versões geraram exatamente o mesmo relatório, mas somente
        a versão otimizada atendeu ao requisito máximo de 2 segundos.
        """
    )

    st.subheader("Resultado funcional")

    resultado_lento = (
        st.session_state.resultado_lento["resumo"]["valor_total"]
    )

    resultado_otimizado = (
        st.session_state.resultado_otimizado["resumo"]["valor_total"]
    )

    comparacao_resultados = [
        {
            "Implementação": "Sistema com falha",
            "Valor total": formatar_moeda(resultado_lento),
            "Tempo": formatar_tempo(tempo_lento),
            "Atende ao requisito": "❌ Não",
        },
        {
            "Implementação": "Sistema otimizado",
            "Valor total": formatar_moeda(resultado_otimizado),
            "Tempo": formatar_tempo(tempo_otimizado),
            "Atende ao requisito": "✅ Sim",
        },
    ]

    st.dataframe(
        comparacao_resultados,
        use_container_width=True,
        hide_index=True,
    )


st.divider()


# =========================================================
# EXPLICAÇÃO DA FALHA
# =========================================================
st.header(
    "Por que essa é uma falha de Eficiência de Desempenho?"
)

st.write(
    """
    O sistema lento não apresenta erro de sintaxe e não gera um
    resultado incorreto.

    O relatório é produzido normalmente.

    Entretanto, o usuário precisa esperar aproximadamente 10 segundos
    por uma operação que deveria ser concluída em até 2 segundos.

    Portanto, a função está correta, mas o desempenho não atende ao
    requisito de qualidade.
    """
)

coluna_falha, coluna_correta = st.columns(2)

with coluna_falha:
    with st.container(border=True):
        st.subheader("❌ Implementação com falha")

        st.markdown(
            """
            Possíveis causas:

            - consultas ao banco sem índices;
            - processamento repetido;
            - várias chamadas desnecessárias;
            - carregamento de dados em excesso;
            - ausência de cache;
            - algoritmos ineficientes;
            - comunicação lenta com serviços externos.
            """
        )

with coluna_correta:
    with st.container(border=True):
        st.subheader("✅ Implementação otimizada")

        st.markdown(
            """
            Possíveis melhorias:

            - criação de índices no banco;
            - redução da quantidade de consultas;
            - processamento em lote;
            - utilização de cache;
            - paginação de resultados;
            - consultas assíncronas;
            - escolha de algoritmos mais eficientes.
            """
        )


st.divider()


# =========================================================
# CÓDIGO DIDÁTICO
# =========================================================
st.header("Código utilizado na demonstração")

coluna_codigo_lento, coluna_codigo_rapido = st.columns(2)

with coluna_codigo_lento:
    with st.container(border=True):
        st.subheader("❌ Sistema lento")

        st.code(
            """
for etapa in range(10):
    processar_dados()

    # Simula uma operação lenta
    time.sleep(1)

    progresso = (etapa + 1) * 10
    barra.progress(progresso)
            """.strip(),
            language="python",
        )

        st.error(
            """
            Tempo total aproximado: 10 segundos.
            """
        )

with coluna_codigo_rapido:
    with st.container(border=True):
        st.subheader("✅ Sistema otimizado")

        st.code(
            """
for etapa in range(10):
    processar_dados_otimizados()

    # Simula uma operação otimizada
    time.sleep(0.05)

    progresso = (etapa + 1) * 10
    barra.progress(progresso)
            """.strip(),
            language="python",
        )

        st.success(
            """
            Tempo total aproximado: 0,5 segundo.
            """
        )


st.info(
    """
    O `time.sleep()` é utilizado apenas para simular o tempo de resposta.

    Em um sistema real, a demora poderia ocorrer devido a consultas
    ineficientes, processamento excessivo, chamadas externas ou falta
    de otimização.
    """
)


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Eficiência de Desempenho?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Tempo de resposta",
        value="Segundos",
    )

with metrica_2:
    st.metric(
        label="Uso de memória",
        value="MB ou GB",
    )

with metrica_3:
    st.metric(
        label="Uso de CPU",
        value="Percentual",
    )

with metrica_4:
    st.metric(
        label="Vazão",
        value="Operações/s",
    )

st.markdown(
    """
    Algumas métricas utilizadas para avaliar o desempenho são:

    - tempo médio de resposta;
    - tempo máximo de resposta;
    - percentual de requisições concluídas dentro do limite;
    - quantidade de operações processadas por segundo;
    - consumo de memória;
    - utilização de CPU;
    - quantidade de usuários simultâneos;
    - tempo de execução de consultas ao banco de dados.
    """
)


st.divider()


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de um sistema lento")

impactos_usuario, impactos_empresa = st.columns(2)

with impactos_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - sensação de travamento;
            - perda de produtividade;
            - abandono da operação;
            - repetição de cliques;
            - insatisfação;
            - perda de confiança no sistema.
            """
        )

with impactos_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - aumento dos chamados de suporte;
            - maior custo de infraestrutura;
            - redução da capacidade do sistema;
            - perda de clientes;
            - dificuldade de crescimento;
            - prejuízo à reputação.
            """
        )


st.divider()


# =========================================================
# REINICIAR DEMONSTRAÇÃO
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados",
    use_container_width=True,
):
    st.session_state.resultado_lento = None
    st.session_state.resultado_otimizado = None
    st.rerun()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema não possui boa qualidade apenas porque entrega um
    resultado correto.

    Ele também precisa responder dentro de um tempo aceitável e utilizar
    adequadamente os recursos disponíveis.

    Nesta demonstração, as duas versões geram o mesmo relatório, mas
    apenas a versão otimizada atende ao requisito de desempenho.
    """
)


if st.button(
    "🏠 Voltar para a página inicial",
    key="voltar_inicio_final",
    use_container_width=True,
):
    voltar_para_inicio()