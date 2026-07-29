import time
from datetime import datetime
from typing import Any, Dict, List

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Confiabilidade",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"

TOTAL_PEDIDOS = 8
PEDIDO_COM_FALHA = 3

TEMPO_PROCESSAMENTO = 0.35
TEMPO_RECUPERACAO = 0.7
MAXIMO_TENTATIVAS = 3


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_nao_confiavel" not in st.session_state:
    st.session_state.resultado_nao_confiavel = None

if "resultado_confiavel" not in st.session_state:
    st.session_state.resultado_confiavel = None


# =========================================================
# NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página principal da aplicação.
    """

    st.switch_page(PAGINA_INICIAL)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def criar_pedidos() -> List[Dict[str, Any]]:
    """
    Cria uma pequena lista de pedidos fictícios.
    """

    return [
        {
            "id": 1,
            "cliente": "Ana Souza",
            "produto": "Notebook",
            "valor": 4250.00,
        },
        {
            "id": 2,
            "cliente": "Bruno Lima",
            "produto": "Monitor",
            "valor": 1680.00,
        },
        {
            "id": 3,
            "cliente": "Carla Mendes",
            "produto": "Teclado",
            "valor": 320.00,
        },
        {
            "id": 4,
            "cliente": "Daniel Silva",
            "produto": "Mouse",
            "valor": 210.00,
        },
        {
            "id": 5,
            "cliente": "Eduarda Costa",
            "produto": "Cadeira",
            "valor": 1890.00,
        },
        {
            "id": 6,
            "cliente": "Felipe Rocha",
            "produto": "Headset",
            "valor": 580.00,
        },
        {
            "id": 7,
            "cliente": "Gabriela Alves",
            "produto": "Webcam",
            "valor": 450.00,
        },
        {
            "id": 8,
            "cliente": "Henrique Martins",
            "produto": "Impressora",
            "valor": 1350.00,
        },
    ]


def formatar_moeda(valor: float) -> str:
    """
    Formata valores monetários no padrão brasileiro.
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
    Formata um tempo em segundos.
    """

    if segundos >= 1:
        return f"{segundos:.2f} segundos"

    return f"{segundos * 1000:.0f} ms"


def criar_barra_textual(
    atual: int,
    total: int,
) -> str:
    """
    Cria uma barra textual com dez posições.

    Exemplo:
    ███░░░░░░░ 30%
    """

    percentual = int((atual / total) * 100)

    quantidade_preenchida = percentual // 10
    quantidade_vazia = 10 - quantidade_preenchida

    barra = (
        "█" * quantidade_preenchida
        + "░" * quantidade_vazia
    )

    return f"{barra} {percentual}%"


def calcular_disponibilidade(
    operacoes_sucesso: int,
    operacoes_totais: int,
) -> float:
    """
    Calcula uma disponibilidade simplificada para fins didáticos.
    """

    if operacoes_totais == 0:
        return 0.0

    return (operacoes_sucesso / operacoes_totais) * 100


# =========================================================
# SISTEMA NÃO CONFIÁVEL
# =========================================================
def executar_sistema_nao_confiavel() -> Dict[str, Any]:
    """
    Simula um sistema que interrompe todo o processamento quando
    encontra uma falha.

    O progresso não é recuperado.
    """

    pedidos = criar_pedidos()

    pedidos_processados = []
    pedidos_perdidos = []
    eventos = []

    barra = st.progress(0)
    barra_textual = st.empty()
    status = st.empty()
    detalhe = st.empty()

    inicio = time.perf_counter()

    status.info(
        "⏳ O sistema não confiável iniciou o processamento."
    )

    for indice, pedido in enumerate(pedidos, start=1):
        detalhe.write(
            f"Processando pedido **#{pedido['id']}** "
            f"de **{pedido['cliente']}**..."
        )

        time.sleep(TEMPO_PROCESSAMENTO)

        if pedido["id"] == PEDIDO_COM_FALHA:
            eventos.append(
                {
                    "Horário": datetime.now().strftime("%H:%M:%S"),
                    "Evento": (
                        f"Falha no pedido #{pedido['id']}. "
                        "Processamento interrompido."
                    ),
                    "Tipo": "Falha",
                }
            )

            pedidos_perdidos = pedidos_processados.copy()
            pedidos_processados = []

            percentual = int((indice / TOTAL_PEDIDOS) * 100)

            barra.progress(
                percentual,
                text=f"Interrompido em {percentual}%",
            )

            barra_textual.code(
                criar_barra_textual(indice, TOTAL_PEDIDOS),
                language=None,
            )

            status.error(
                "❌ O serviço ficou indisponível e perdeu o progresso."
            )

            tempo_total = time.perf_counter() - inicio

            return {
                "sucesso": False,
                "tempo_total": tempo_total,
                "processados": pedidos_processados,
                "perdidos": pedidos_perdidos,
                "pendentes": pedidos[indice - 1:],
                "falhas": 1,
                "tentativas": indice,
                "recuperacoes": 0,
                "eventos": eventos,
                "mensagem": (
                    "O sistema interrompeu toda a operação e não "
                    "conseguiu recuperar os pedidos já processados."
                ),
            }

        pedidos_processados.append(pedido)

        eventos.append(
            {
                "Horário": datetime.now().strftime("%H:%M:%S"),
                "Evento": f"Pedido #{pedido['id']} processado.",
                "Tipo": "Sucesso",
            }
        )

        percentual = int((indice / TOTAL_PEDIDOS) * 100)

        barra.progress(
            percentual,
            text=f"Processamento: {percentual}%",
        )

        barra_textual.code(
            criar_barra_textual(indice, TOTAL_PEDIDOS),
            language=None,
        )

    tempo_total = time.perf_counter() - inicio

    status.success("✅ Todos os pedidos foram processados.")

    return {
        "sucesso": True,
        "tempo_total": tempo_total,
        "processados": pedidos_processados,
        "perdidos": [],
        "pendentes": [],
        "falhas": 0,
        "tentativas": TOTAL_PEDIDOS,
        "recuperacoes": 0,
        "eventos": eventos,
        "mensagem": "Todos os pedidos foram processados.",
    }


# =========================================================
# SISTEMA CONFIÁVEL
# =========================================================
def executar_sistema_confiavel() -> Dict[str, Any]:
    """
    Simula um sistema com:

    - tratamento de falhas;
    - novas tentativas;
    - checkpoint;
    - recuperação automática;
    - continuidade do processamento.
    """

    pedidos = criar_pedidos()

    pedidos_processados = []
    eventos = []

    falhas = 0
    total_tentativas = 0
    recuperacoes = 0

    barra = st.progress(0)
    barra_textual = st.empty()
    status = st.empty()
    detalhe = st.empty()
    tentativa_visual = st.empty()

    inicio = time.perf_counter()

    status.info(
        "⏳ O sistema confiável iniciou o processamento."
    )

    for indice, pedido in enumerate(pedidos, start=1):
        pedido_concluido = False

        for tentativa in range(1, MAXIMO_TENTATIVAS + 1):
            total_tentativas += 1

            detalhe.write(
                f"Processando pedido **#{pedido['id']}** "
                f"de **{pedido['cliente']}**..."
            )

            tentativa_visual.write(
                f"Tentativa **{tentativa} de "
                f"{MAXIMO_TENTATIVAS}**"
            )

            time.sleep(TEMPO_PROCESSAMENTO)

            falha_simulada = (
                pedido["id"] == PEDIDO_COM_FALHA
                and tentativa == 1
            )

            if falha_simulada:
                falhas += 1

                eventos.append(
                    {
                        "Horário": datetime.now().strftime("%H:%M:%S"),
                        "Evento": (
                            f"Falha temporária no pedido "
                            f"#{pedido['id']}."
                        ),
                        "Tipo": "Falha recuperável",
                    }
                )

                tentativa_visual.warning(
                    "⚠️ Falha temporária detectada. "
                    "Iniciando recuperação..."
                )

                time.sleep(TEMPO_RECUPERACAO)

                recuperacoes += 1

                eventos.append(
                    {
                        "Horário": datetime.now().strftime("%H:%M:%S"),
                        "Evento": (
                            f"Serviço recuperado. Nova tentativa para "
                            f"o pedido #{pedido['id']}."
                        ),
                        "Tipo": "Recuperação",
                    }
                )

                tentativa_visual.info(
                    "🔄 Serviço recuperado. Repetindo somente "
                    "o pedido que apresentou falha."
                )

                continue

            pedidos_processados.append(pedido)
            pedido_concluido = True

            eventos.append(
                {
                    "Horário": datetime.now().strftime("%H:%M:%S"),
                    "Evento": f"Pedido #{pedido['id']} processado.",
                    "Tipo": "Sucesso",
                }
            )

            break

        if not pedido_concluido:
            eventos.append(
                {
                    "Horário": datetime.now().strftime("%H:%M:%S"),
                    "Evento": (
                        f"Pedido #{pedido['id']} enviado para "
                        "tratamento manual."
                    ),
                    "Tipo": "Contingência",
                }
            )

        percentual = int(
            (len(pedidos_processados) / TOTAL_PEDIDOS) * 100
        )

        barra.progress(
            percentual,
            text=f"Processamento: {percentual}%",
        )

        barra_textual.code(
            criar_barra_textual(
                len(pedidos_processados),
                TOTAL_PEDIDOS,
            ),
            language=None,
        )

    tempo_total = time.perf_counter() - inicio

    tentativa_visual.empty()
    detalhe.empty()

    todos_processados = (
        len(pedidos_processados) == TOTAL_PEDIDOS
    )

    if todos_processados:
        status.success(
            "✅ Todos os pedidos foram processados, inclusive após "
            "a recuperação da falha."
        )
    else:
        status.warning(
            "⚠️ Alguns pedidos não puderam ser processados."
        )

    ids_processados = {
        pedido["id"]
        for pedido in pedidos_processados
    }

    pendentes = [
        pedido
        for pedido in pedidos
        if pedido["id"] not in ids_processados
    ]

    return {
        "sucesso": todos_processados,
        "tempo_total": tempo_total,
        "processados": pedidos_processados,
        "perdidos": [],
        "pendentes": pendentes,
        "falhas": falhas,
        "tentativas": total_tentativas,
        "recuperacoes": recuperacoes,
        "eventos": eventos,
        "mensagem": (
            "O sistema detectou a falha, recuperou o serviço e "
            "continuou o processamento sem perder os pedidos anteriores."
        ),
    }


def exibir_pedidos(
    pedidos: List[Dict[str, Any]],
) -> None:
    """
    Exibe os pedidos em formato tabular.
    """

    if not pedidos:
        st.info("Nenhum pedido disponível para exibição.")
        return

    dados_formatados = []

    for pedido in pedidos:
        dados_formatados.append(
            {
                "Pedido": f"#{pedido['id']}",
                "Cliente": pedido["cliente"],
                "Produto": pedido["produto"],
                "Valor": formatar_moeda(pedido["valor"]),
            }
        )

    st.dataframe(
        dados_formatados,
        use_container_width=True,
        hide_index=True,
    )


def reiniciar_demonstracao() -> None:
    """
    Limpa os resultados das duas demonstrações.
    """

    st.session_state.resultado_nao_confiavel = None
    st.session_state.resultado_confiavel = None

    st.rerun()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("🛡️ Confiabilidade")

    st.write(
        """
        Esta página demonstra como um sistema se comporta diante
        de uma falha durante o processamento.
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

    st.subheader("Aspectos avaliados")

    st.markdown(
        """
        - continuidade da operação;
        - disponibilidade;
        - tolerância a falhas;
        - recuperação;
        - preservação dos dados;
        - taxa de sucesso.
        """
    )

    st.warning(
        """
        A falha desta página é simulada propositalmente para
        fins didáticos.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("🛡️ Falha de Confiabilidade")

st.write(
    """
    Nesta demonstração, dois sistemas processam os mesmos oito pedidos.

    Durante o terceiro pedido ocorre uma falha temporária.

    A diferença está na capacidade de cada sistema de continuar
    funcionando e recuperar a operação.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Confiabilidade?

    Confiabilidade avalia a capacidade de um sistema manter seu
    funcionamento correto durante um período e sob determinadas
    condições.

    Um sistema confiável deve apresentar estabilidade, disponibilidade,
    tolerância a falhas e capacidade de recuperação.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma loja precisa processar pedidos realizados pelos clientes.

    Durante o processamento do pedido número 3, o serviço de pagamento
    apresenta uma falha temporária.
    """
)

st.success(
    """
    ### Requisito de confiabilidade

    Quando ocorrer uma falha temporária, o sistema deve:

    - preservar os pedidos já processados;
    - tentar novamente a operação;
    - recuperar-se automaticamente;
    - continuar o processamento;
    - evitar perda ou duplicação de dados.
    """
)


st.divider()


# =========================================================
# DEMONSTRAÇÕES
# =========================================================
st.header("Execute as demonstrações")

coluna_falha, coluna_confiavel = st.columns(2)


# =========================================================
# SISTEMA NÃO CONFIÁVEL
# =========================================================
with coluna_falha:
    with st.container(border=True):
        st.subheader("❌ Sistema não confiável")

        st.write(
            """
            Quando encontra uma falha, esta versão:

            - interrompe toda a operação;
            - perde o progresso;
            - não realiza nova tentativa;
            - deixa os pedidos pendentes.
            """
        )

        executar_falha = st.button(
            "Executar sistema não confiável",
            key="executar_nao_confiavel",
            type="primary",
            use_container_width=True,
        )

        if executar_falha:
            st.session_state.resultado_confiavel = None

            st.session_state.resultado_nao_confiavel = (
                executar_sistema_nao_confiavel()
            )

            st.rerun()


# =========================================================
# SISTEMA CONFIÁVEL
# =========================================================
with coluna_confiavel:
    with st.container(border=True):
        st.subheader("✅ Sistema confiável")

        st.write(
            """
            Quando encontra uma falha, esta versão:

            - mantém um checkpoint;
            - identifica a operação com problema;
            - realiza uma nova tentativa;
            - recupera o serviço;
            - continua a partir do ponto correto.
            """
        )

        executar_confiavel = st.button(
            "Executar sistema confiável",
            key="executar_confiavel",
            use_container_width=True,
        )

        if executar_confiavel:
            st.session_state.resultado_nao_confiavel = None

            st.session_state.resultado_confiavel = (
                executar_sistema_confiavel()
            )

            st.rerun()


# =========================================================
# RESULTADO NÃO CONFIÁVEL
# =========================================================
resultado_nao_confiavel = (
    st.session_state.resultado_nao_confiavel
)

if resultado_nao_confiavel is not None:
    st.divider()

    st.header("Resultado do sistema não confiável")

    st.error(
        """
        ### Processamento interrompido

        O sistema encontrou uma falha e não conseguiu continuar.
        Os pedidos que pareciam processados também foram perdidos.
        """
    )

    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

    with coluna_1:
        st.metric(
            label="Pedidos concluídos",
            value=str(
                len(resultado_nao_confiavel["processados"])
            ),
        )

    with coluna_2:
        st.metric(
            label="Pedidos perdidos",
            value=str(
                len(resultado_nao_confiavel["perdidos"])
            ),
        )

    with coluna_3:
        st.metric(
            label="Pedidos pendentes",
            value=str(
                len(resultado_nao_confiavel["pendentes"])
            ),
        )

    with coluna_4:
        st.metric(
            label="Tempo até a falha",
            value=formatar_tempo(
                resultado_nao_confiavel["tempo_total"]
            ),
        )

    taxa_sucesso = calcular_disponibilidade(
        operacoes_sucesso=len(
            resultado_nao_confiavel["processados"]
        ),
        operacoes_totais=TOTAL_PEDIDOS,
    )

    st.metric(
        label="Taxa final de sucesso",
        value=f"{taxa_sucesso:.1f}%",
    )

    st.subheader("Pedidos perdidos")

    exibir_pedidos(
        resultado_nao_confiavel["perdidos"]
    )

    st.subheader("Pedidos não concluídos")

    exibir_pedidos(
        resultado_nao_confiavel["pendentes"]
    )

    with st.expander(
        "Visualizar eventos do processamento",
        expanded=True,
    ):
        st.dataframe(
            resultado_nao_confiavel["eventos"],
            use_container_width=True,
            hide_index=True,
        )

    st.warning(
        resultado_nao_confiavel["mensagem"]
    )


# =========================================================
# RESULTADO CONFIÁVEL
# =========================================================
resultado_confiavel = (
    st.session_state.resultado_confiavel
)

if resultado_confiavel is not None:
    st.divider()

    st.header("Resultado do sistema confiável")

    if resultado_confiavel["sucesso"]:
        st.success(
            """
            ### Processamento concluído

            A falha ocorreu, mas o sistema conseguiu recuperar-se
            e concluir todos os pedidos.
            """
        )
    else:
        st.warning(
            """
            O sistema aplicou os mecanismos de recuperação, mas
            alguns pedidos permaneceram pendentes.
            """
        )

    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

    with coluna_1:
        st.metric(
            label="Pedidos concluídos",
            value=str(
                len(resultado_confiavel["processados"])
            ),
        )

    with coluna_2:
        st.metric(
            label="Falhas detectadas",
            value=str(
                resultado_confiavel["falhas"]
            ),
        )

    with coluna_3:
        st.metric(
            label="Recuperações realizadas",
            value=str(
                resultado_confiavel["recuperacoes"]
            ),
        )

    with coluna_4:
        st.metric(
            label="Tempo total",
            value=formatar_tempo(
                resultado_confiavel["tempo_total"]
            ),
        )

    taxa_sucesso = calcular_disponibilidade(
        operacoes_sucesso=len(
            resultado_confiavel["processados"]
        ),
        operacoes_totais=TOTAL_PEDIDOS,
    )

    coluna_taxa, coluna_tentativas = st.columns(2)

    with coluna_taxa:
        st.metric(
            label="Taxa final de sucesso",
            value=f"{taxa_sucesso:.1f}%",
        )

    with coluna_tentativas:
        st.metric(
            label="Total de tentativas",
            value=str(
                resultado_confiavel["tentativas"]
            ),
        )

    st.subheader("Pedidos concluídos")

    exibir_pedidos(
        resultado_confiavel["processados"]
    )

    with st.expander(
        "Visualizar eventos do processamento",
        expanded=True,
    ):
        st.dataframe(
            resultado_confiavel["eventos"],
            use_container_width=True,
            hide_index=True,
        )

    st.success(
        resultado_confiavel["mensagem"]
    )


st.divider()


# =========================================================
# COMPARAÇÃO DIDÁTICA
# =========================================================
st.header("Comparação dos sistemas")

comparacao = [
    {
        "Critério": "Comportamento ao falhar",
        "Sistema não confiável": "Interrompe toda a operação",
        "Sistema confiável": "Isola e trata a falha",
    },
    {
        "Critério": "Nova tentativa",
        "Sistema não confiável": "Não realiza",
        "Sistema confiável": "Realiza automaticamente",
    },
    {
        "Critério": "Preservação do progresso",
        "Sistema não confiável": "Perde os dados processados",
        "Sistema confiável": "Mantém checkpoint",
    },
    {
        "Critério": "Recuperação",
        "Sistema não confiável": "Depende de intervenção manual",
        "Sistema confiável": "Recuperação automática",
    },
    {
        "Critério": "Continuidade",
        "Sistema não confiável": "Pedidos ficam pendentes",
        "Sistema confiável": "Processamento continua",
    },
    {
        "Critério": "Resultado esperado",
        "Sistema não confiável": "Operação incompleta",
        "Sistema confiável": "Todos os pedidos concluídos",
    },
]

st.dataframe(
    comparacao,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# SUBCARACTERÍSTICAS
# =========================================================
st.header("Aspectos de Confiabilidade demonstrados")

coluna_1, coluna_2 = st.columns(2)

with coluna_1:
    with st.container(border=True):
        st.subheader("Maturidade")

        st.write(
            """
            Capacidade do sistema de atender às necessidades de
            confiabilidade durante sua operação normal.
            """
        )

    with st.container(border=True):
        st.subheader("Disponibilidade")

        st.write(
            """
            Capacidade do sistema de permanecer acessível e operacional
            quando sua utilização é necessária.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("Tolerância a falhas")

        st.write(
            """
            Capacidade de continuar funcionando mesmo quando ocorre
            uma falha em um componente ou serviço.
            """
        )

    with st.container(border=True):
        st.subheader("Recuperabilidade")

        st.write(
            """
            Capacidade de restabelecer o funcionamento e recuperar
            dados após uma interrupção ou falha.
            """
        )


st.divider()


# =========================================================
# CÓDIGO COM FALHA
# =========================================================
st.header("Código com baixa confiabilidade")

with st.expander(
    "Visualizar implementação não confiável",
    expanded=True,
):
    st.code(
        """
def processar_pedidos(pedidos):
    processados = []

    for pedido in pedidos:
        processar_pagamento(pedido)

        processados.append(pedido)

    return processados
        """.strip(),
        language="python",
    )

st.error(
    """
    Essa implementação não possui:

    - tratamento de exceção;
    - novas tentativas;
    - checkpoint;
    - mecanismo de recuperação;
    - fila de contingência;
    - registro dos eventos.
    """
)


# =========================================================
# CÓDIGO CONFIÁVEL
# =========================================================
st.header("Código com mecanismos de confiabilidade")

with st.expander(
    "Visualizar implementação confiável",
    expanded=True,
):
    st.code(
        """
def processar_pedido_com_retry(
    pedido,
    maximo_tentativas=3,
):
    for tentativa in range(1, maximo_tentativas + 1):
        try:
            processar_pagamento(pedido)

            salvar_checkpoint(pedido)

            return True

        except FalhaTemporaria:
            registrar_falha(
                pedido=pedido,
                tentativa=tentativa,
            )

            if tentativa < maximo_tentativas:
                aguardar_recuperacao()

            else:
                enviar_para_fila_de_contingencia(pedido)

    return False
        """.strip(),
        language="python",
    )

st.success(
    """
    A implementação confiável limita as tentativas, registra as falhas,
    preserva o progresso e possui uma alternativa quando a recuperação
    automática não é possível.
    """
)


st.divider()


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Confiabilidade?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Disponibilidade",
        value="Percentual",
    )

with metrica_2:
    st.metric(
        label="Taxa de falhas",
        value="Falhas/operação",
    )

with metrica_3:
    st.metric(
        label="Tempo de recuperação",
        value="MTTR",
    )

with metrica_4:
    st.metric(
        label="Tempo entre falhas",
        value="MTBF",
    )

st.info(
    """
    Algumas métricas utilizadas para avaliar confiabilidade:

    - disponibilidade do sistema;
    - taxa de operações concluídas;
    - quantidade de falhas por período;
    - tempo médio entre falhas — MTBF;
    - tempo médio para recuperação — MTTR;
    - percentual de recuperações automáticas;
    - quantidade de dados perdidos;
    - quantidade de operações duplicadas;
    - percentual de requisições processadas após uma falha.
    """
)


st.divider()


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de um sistema não confiável")

coluna_usuario, coluna_empresa = st.columns(2)

with coluna_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - operações interrompidas;
            - perda de dados;
            - necessidade de repetir ações;
            - pedidos duplicados;
            - indisponibilidade;
            - insegurança sobre o resultado;
            - perda de confiança no sistema.
            """
        )

with coluna_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - perda de vendas;
            - inconsistência de dados;
            - aumento dos chamados de suporte;
            - necessidade de recuperação manual;
            - descumprimento de acordos de serviço;
            - prejuízo financeiro;
            - danos à reputação.
            """
        )


st.divider()


# =========================================================
# BOAS PRÁTICAS
# =========================================================
st.header("Boas práticas para aumentar a confiabilidade")

st.markdown(
    """
    - utilizar tratamento adequado de exceções;
    - limitar a quantidade de novas tentativas;
    - implementar espera progressiva entre tentativas;
    - utilizar filas para operações assíncronas;
    - manter checkpoints;
    - garantir idempotência;
    - registrar eventos e falhas;
    - realizar backups;
    - implementar redundância;
    - monitorar disponibilidade;
    - criar mecanismos de fallback;
    - testar cenários de interrupção e recuperação.
    """
)

st.warning(
    """
    Novas tentativas sem limite também são um problema.

    O sistema deve definir uma quantidade máxima de tentativas e,
    quando necessário, encaminhar a operação para uma fila de
    contingência ou intervenção manual.
    """
)


st.divider()


# =========================================================
# REINICIAR
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_confiabilidade",
    use_container_width=True,
):
    reiniciar_demonstracao()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema confiável não é aquele que nunca apresenta falhas.

    Falhas podem ocorrer em bancos de dados, redes, serviços externos,
    servidores e outros componentes.

    A confiabilidade está relacionada à capacidade de detectar o
    problema, preservar os dados, recuperar-se e continuar funcionando
    de maneira controlada.

    Nesta demonstração, o sistema não confiável perdeu o progresso e
    interrompeu os pedidos. O sistema confiável identificou a falha,
    realizou uma nova tentativa e concluiu o processamento.
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