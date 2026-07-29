
import random
from datetime import datetime, timedelta
from typing import Dict, List

import pandas as pd
import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Dashboard de Qualidade de Software",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"

CARACTERISTICAS = [
    "Adequação Funcional",
    "Eficiência de Desempenho",
    "Compatibilidade",
    "Usabilidade",
    "Confiabilidade",
    "Segurança",
    "Manutenibilidade",
    "Portabilidade",
]

ICONS = {
    "Adequação Funcional": "🎯",
    "Eficiência de Desempenho": "⚡",
    "Compatibilidade": "🔌",
    "Usabilidade": "👩‍💻",
    "Confiabilidade": "🛡️",
    "Segurança": "🔐",
    "Manutenibilidade": "🛠️",
    "Portabilidade": "📦",
}

METAS = {
    "Adequação Funcional": 95.0,
    "Eficiência de Desempenho": 90.0,
    "Compatibilidade": 92.0,
    "Usabilidade": 88.0,
    "Confiabilidade": 99.0,
    "Segurança": 95.0,
    "Manutenibilidade": 85.0,
    "Portabilidade": 90.0,
}


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "dados_dashboard_qualidade" not in st.session_state:
    st.session_state.dados_dashboard_qualidade = None

if "ultima_atualizacao_dashboard" not in st.session_state:
    st.session_state.ultima_atualizacao_dashboard = datetime.now()


# =========================================================
# FUNÇÕES DE NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    st.switch_page(PAGINA_INICIAL)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def formatar_percentual(valor: float) -> str:
    return f"{valor:.1f}%".replace(".", ",")


def formatar_decimal(valor: float, casas: int = 2) -> str:
    return f"{valor:.{casas}f}".replace(".", ",")


def formatar_inteiro(valor: float) -> str:
    return f"{int(valor):,}".replace(",", ".")


def obter_status(indice: float, meta: float) -> str:
    if indice >= meta:
        return "Saudável"

    if indice >= meta - 5:
        return "Atenção"

    return "Crítico"


def obter_criticidade(falhas: int) -> str:
    if falhas >= 20:
        return "Crítica"

    if falhas >= 10:
        return "Alta"

    if falhas >= 5:
        return "Média"

    return "Baixa"


def criar_barra_textual(valor: float) -> str:
    percentual = max(0, min(100, int(valor)))
    preenchido = percentual // 10
    vazio = 10 - preenchido

    return (
        "█" * preenchido
        + "░" * vazio
        + f" {percentual}%"
    )


# =========================================================
# GERAÇÃO DOS DADOS DEMONSTRATIVOS
# =========================================================
def gerar_dados_demonstrativos() -> Dict[str, pd.DataFrame]:
    random.seed(42)

    resumo = pd.DataFrame(
        [
            {
                "Característica": "Adequação Funcional",
                "Índice": 96.8,
                "Meta": 95.0,
                "Falhas": 4,
                "Incidentes críticos": 0,
                "Tendência": 1.8,
                "Cobertura": 98.0,
                "Tempo médio": 1.2,
                "Disponibilidade": 99.7,
                "Conformidade": 97.0,
            },
            {
                "Característica": "Eficiência de Desempenho",
                "Índice": 87.4,
                "Meta": 90.0,
                "Falhas": 15,
                "Incidentes críticos": 2,
                "Tendência": -2.6,
                "Cobertura": 91.0,
                "Tempo médio": 3.8,
                "Disponibilidade": 98.9,
                "Conformidade": 86.0,
            },
            {
                "Característica": "Compatibilidade",
                "Índice": 93.2,
                "Meta": 92.0,
                "Falhas": 7,
                "Incidentes críticos": 1,
                "Tendência": 0.9,
                "Cobertura": 94.0,
                "Tempo médio": 2.1,
                "Disponibilidade": 99.1,
                "Conformidade": 93.0,
            },
            {
                "Característica": "Usabilidade",
                "Índice": 84.6,
                "Meta": 88.0,
                "Falhas": 18,
                "Incidentes críticos": 1,
                "Tendência": -1.4,
                "Cobertura": 88.0,
                "Tempo médio": 4.5,
                "Disponibilidade": 99.5,
                "Conformidade": 84.0,
            },
            {
                "Característica": "Confiabilidade",
                "Índice": 98.7,
                "Meta": 99.0,
                "Falhas": 9,
                "Incidentes críticos": 2,
                "Tendência": 0.4,
                "Cobertura": 96.0,
                "Tempo médio": 0.8,
                "Disponibilidade": 99.4,
                "Conformidade": 98.0,
            },
            {
                "Característica": "Segurança",
                "Índice": 91.5,
                "Meta": 95.0,
                "Falhas": 22,
                "Incidentes críticos": 3,
                "Tendência": -3.2,
                "Cobertura": 93.0,
                "Tempo médio": 6.2,
                "Disponibilidade": 99.6,
                "Conformidade": 91.0,
            },
            {
                "Característica": "Manutenibilidade",
                "Índice": 82.9,
                "Meta": 85.0,
                "Falhas": 13,
                "Incidentes críticos": 1,
                "Tendência": 2.1,
                "Cobertura": 78.0,
                "Tempo médio": 8.4,
                "Disponibilidade": 99.2,
                "Conformidade": 83.0,
            },
            {
                "Característica": "Portabilidade",
                "Índice": 89.6,
                "Meta": 90.0,
                "Falhas": 6,
                "Incidentes críticos": 0,
                "Tendência": 1.2,
                "Cobertura": 90.0,
                "Tempo médio": 3.0,
                "Disponibilidade": 99.3,
                "Conformidade": 90.0,
            },
        ]
    )

    resumo["Status"] = resumo.apply(
        lambda linha: obter_status(
            linha["Índice"],
            linha["Meta"],
        ),
        axis=1,
    )

    resumo["Criticidade"] = resumo["Falhas"].apply(
        obter_criticidade
    )

    meses = pd.date_range(
        end=pd.Timestamp.today().normalize(),
        periods=12,
        freq="MS",
    )

    historico_registros: List[Dict[str, object]] = []

    for caracteristica in CARACTERISTICAS:
        indice_final = float(
            resumo.loc[
                resumo["Característica"] == caracteristica,
                "Índice",
            ].iloc[0]
        )

        valor_inicial = indice_final - random.uniform(-2, 8)

        for posicao, mes in enumerate(meses):
            progresso = posicao / max(1, len(meses) - 1)

            valor = (
                valor_inicial
                + (indice_final - valor_inicial) * progresso
                + random.uniform(-1.5, 1.5)
            )

            falhas_base = int(
                resumo.loc[
                    resumo["Característica"] == caracteristica,
                    "Falhas",
                ].iloc[0]
            )

            falhas_mes = max(
                0,
                int(
                    falhas_base / 3
                    + random.uniform(-3, 4)
                ),
            )

            historico_registros.append(
                {
                    "Mês": mes,
                    "Característica": caracteristica,
                    "Índice de qualidade": round(
                        max(60, min(100, valor)),
                        1,
                    ),
                    "Falhas registradas": falhas_mes,
                }
            )

    historico = pd.DataFrame(historico_registros)

    eventos = pd.DataFrame(
        [
            {
                "Data": datetime.now() - timedelta(hours=2),
                "Característica": "Segurança",
                "Evento": "Múltiplas tentativas de autenticação inválidas",
                "Severidade": "Crítica",
                "Status": "Em investigação",
                "Responsável": "Equipe de Segurança",
            },
            {
                "Data": datetime.now() - timedelta(hours=5),
                "Característica": "Eficiência de Desempenho",
                "Evento": "Tempo de resposta acima de 5 segundos",
                "Severidade": "Alta",
                "Status": "Em correção",
                "Responsável": "Equipe Back-End",
            },
            {
                "Data": datetime.now() - timedelta(days=1),
                "Característica": "Usabilidade",
                "Evento": "Taxa de abandono elevada no formulário",
                "Severidade": "Alta",
                "Status": "Planejado",
                "Responsável": "Equipe UX",
            },
            {
                "Data": datetime.now() - timedelta(days=1, hours=4),
                "Característica": "Confiabilidade",
                "Evento": "Falha temporária na integração de pagamentos",
                "Severidade": "Crítica",
                "Status": "Resolvido",
                "Responsável": "Equipe de Plataforma",
            },
            {
                "Data": datetime.now() - timedelta(days=2),
                "Característica": "Manutenibilidade",
                "Evento": "Duplicação de regra de negócio identificada",
                "Severidade": "Média",
                "Status": "Em correção",
                "Responsável": "Equipe de Desenvolvimento",
            },
            {
                "Data": datetime.now() - timedelta(days=3),
                "Característica": "Compatibilidade",
                "Evento": "Falha na leitura de arquivo em formato legado",
                "Severidade": "Média",
                "Status": "Resolvido",
                "Responsável": "Equipe de Integração",
            },
            {
                "Data": datetime.now() - timedelta(days=4),
                "Característica": "Portabilidade",
                "Evento": "Caminho absoluto incompatível com Linux",
                "Severidade": "Alta",
                "Status": "Resolvido",
                "Responsável": "Equipe DevOps",
            },
            {
                "Data": datetime.now() - timedelta(days=5),
                "Característica": "Adequação Funcional",
                "Evento": "Regra de desconto divergente do requisito",
                "Severidade": "Média",
                "Status": "Resolvido",
                "Responsável": "Equipe de Produto",
            },
        ]
    )

    testes = pd.DataFrame(
        [
            {
                "Característica": "Adequação Funcional",
                "Executados": 180,
                "Aprovados": 176,
                "Reprovados": 4,
                "Cobertura": 98.0,
            },
            {
                "Característica": "Eficiência de Desempenho",
                "Executados": 120,
                "Aprovados": 105,
                "Reprovados": 15,
                "Cobertura": 91.0,
            },
            {
                "Característica": "Compatibilidade",
                "Executados": 96,
                "Aprovados": 89,
                "Reprovados": 7,
                "Cobertura": 94.0,
            },
            {
                "Característica": "Usabilidade",
                "Executados": 85,
                "Aprovados": 67,
                "Reprovados": 18,
                "Cobertura": 88.0,
            },
            {
                "Característica": "Confiabilidade",
                "Executados": 140,
                "Aprovados": 131,
                "Reprovados": 9,
                "Cobertura": 96.0,
            },
            {
                "Característica": "Segurança",
                "Executados": 160,
                "Aprovados": 138,
                "Reprovados": 22,
                "Cobertura": 93.0,
            },
            {
                "Característica": "Manutenibilidade",
                "Executados": 110,
                "Aprovados": 97,
                "Reprovados": 13,
                "Cobertura": 78.0,
            },
            {
                "Característica": "Portabilidade",
                "Executados": 75,
                "Aprovados": 69,
                "Reprovados": 6,
                "Cobertura": 90.0,
            },
        ]
    )

    return {
        "resumo": resumo,
        "historico": historico,
        "eventos": eventos,
        "testes": testes,
    }


def obter_dados() -> Dict[str, pd.DataFrame]:
    if st.session_state.dados_dashboard_qualidade is None:
        st.session_state.dados_dashboard_qualidade = (
            gerar_dados_demonstrativos()
        )

    return st.session_state.dados_dashboard_qualidade


def atualizar_dados() -> None:
    st.session_state.dados_dashboard_qualidade = (
        gerar_dados_demonstrativos()
    )

    st.session_state.ultima_atualizacao_dashboard = (
        datetime.now()
    )

    st.rerun()


# =========================================================
# CARREGAMENTO DOS DADOS
# =========================================================
dados = obter_dados()

resumo = dados["resumo"].copy()
historico = dados["historico"].copy()
eventos = dados["eventos"].copy()
testes = dados["testes"].copy()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("📊 Dashboard de Qualidade")

    st.write(
        """
        Monitoramento consolidado das oito características de
        qualidade demonstradas no laboratório.
        """
    )

    st.divider()

    if st.button(
        "🏠 Voltar para a página inicial",
        key="voltar_inicio_dashboard",
        use_container_width=True,
    ):
        voltar_para_inicio()

    st.divider()

    st.subheader("Filtros")

    caracteristicas_selecionadas = st.multiselect(
        "Características",
        options=CARACTERISTICAS,
        default=CARACTERISTICAS,
        key="filtro_caracteristicas_dashboard",
    )

    status_selecionados = st.multiselect(
        "Status",
        options=["Saudável", "Atenção", "Crítico"],
        default=["Saudável", "Atenção", "Crítico"],
        key="filtro_status_dashboard",
    )

    severidades_selecionadas = st.multiselect(
        "Severidade dos eventos",
        options=["Crítica", "Alta", "Média", "Baixa"],
        default=["Crítica", "Alta", "Média", "Baixa"],
        key="filtro_severidade_dashboard",
    )

    st.divider()

    if st.button(
        "🔄 Atualizar dados simulados",
        key="atualizar_dashboard",
        use_container_width=True,
    ):
        atualizar_dados()

    st.caption(
        "Última atualização: "
        + st.session_state.ultima_atualizacao_dashboard.strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    )

    st.info(
        """
        Os valores apresentados são pré-modelados e possuem
        finalidade exclusivamente didática.
        """
    )


# =========================================================
# FILTROS
# =========================================================
resumo_filtrado = resumo[
    resumo["Característica"].isin(
        caracteristicas_selecionadas
    )
    & resumo["Status"].isin(status_selecionados)
].copy()

historico_filtrado = historico[
    historico["Característica"].isin(
        caracteristicas_selecionadas
    )
].copy()

eventos_filtrados = eventos[
    eventos["Característica"].isin(
        caracteristicas_selecionadas
    )
    & eventos["Severidade"].isin(
        severidades_selecionadas
    )
].copy()

testes_filtrados = testes[
    testes["Característica"].isin(
        caracteristicas_selecionadas
    )
].copy()


# =========================================================
# CABEÇALHO
# =========================================================
st.title("📊 Dashboard de Monitoramento da Qualidade")

st.write(
    """
    Visão executiva dos indicadores, falhas, testes e tendências
    relacionadas às oito características de qualidade de software.
    """
)

st.warning(
    """
    Este painel utiliza dados simulados para demonstrar como uma
    organização pode acompanhar a qualidade de seus sistemas.
    """
)


# =========================================================
# KPIs EXECUTIVOS
# =========================================================
if resumo_filtrado.empty:
    st.error(
        """
        Nenhum indicador corresponde aos filtros selecionados.

        Ajuste os filtros da barra lateral.
        """
    )

    st.stop()


indice_geral = resumo_filtrado["Índice"].mean()
meta_geral = resumo_filtrado["Meta"].mean()
total_falhas = int(resumo_filtrado["Falhas"].sum())
incidentes_criticos = int(
    resumo_filtrado["Incidentes críticos"].sum()
)
disponibilidade_media = (
    resumo_filtrado["Disponibilidade"].mean()
)
caracteristicas_na_meta = int(
    (
        resumo_filtrado["Índice"]
        >= resumo_filtrado["Meta"]
    ).sum()
)

st.header("Visão executiva")

kpi_1, kpi_2, kpi_3, kpi_4, kpi_5, kpi_6 = st.columns(6)

with kpi_1:
    st.metric(
        label="Índice geral",
        value=formatar_percentual(indice_geral),
        delta=formatar_percentual(
            indice_geral - meta_geral
        ),
    )

with kpi_2:
    st.metric(
        label="Meta média",
        value=formatar_percentual(meta_geral),
    )

with kpi_3:
    st.metric(
        label="Falhas abertas",
        value=formatar_inteiro(total_falhas),
        delta="-6 no período",
        delta_color="inverse",
    )

with kpi_4:
    st.metric(
        label="Incidentes críticos",
        value=formatar_inteiro(incidentes_criticos),
        delta="+1 no período",
        delta_color="inverse",
    )

with kpi_5:
    st.metric(
        label="Disponibilidade",
        value=formatar_percentual(
            disponibilidade_media
        ),
    )

with kpi_6:
    st.metric(
        label="Características na meta",
        value=(
            f"{caracteristicas_na_meta}/"
            f"{len(resumo_filtrado)}"
        ),
    )


# =========================================================
# SAÚDE GERAL
# =========================================================
st.subheader("Saúde geral do produto")

coluna_saude, coluna_distribuicao = st.columns([1, 2])

with coluna_saude:
    with st.container(border=True):
        st.metric(
            label="Pontuação consolidada",
            value=formatar_percentual(indice_geral),
        )

        st.code(
            criar_barra_textual(indice_geral),
            language=None,
        )

        if indice_geral >= meta_geral:
            st.success(
                "O produto está acima da meta consolidada."
            )

        elif indice_geral >= meta_geral - 3:
            st.warning(
                "O produto está próximo da meta, mas exige atenção."
            )

        else:
            st.error(
                "O produto está abaixo da meta consolidada."
            )

with coluna_distribuicao:
    distribuicao_status = (
        resumo_filtrado["Status"]
        .value_counts()
        .rename_axis("Status")
        .reset_index(name="Quantidade")
    )

    st.write("**Distribuição por status**")

    st.bar_chart(
        distribuicao_status.set_index("Status"),
        use_container_width=True,
    )


st.divider()


# =========================================================
# CARDS POR CARACTERÍSTICA
# =========================================================
st.header("Indicadores por característica")

for inicio in range(0, len(resumo_filtrado), 4):
    colunas = st.columns(4)
    grupo = resumo_filtrado.iloc[inicio:inicio + 4]

    for coluna, (_, linha) in zip(
        colunas,
        grupo.iterrows(),
    ):
        with coluna:
            with st.container(border=True):
                nome = linha["Característica"]

                st.subheader(
                    f"{ICONS[nome]} {nome}"
                )

                st.metric(
                    label="Índice de qualidade",
                    value=formatar_percentual(
                        linha["Índice"]
                    ),
                    delta=formatar_percentual(
                        linha["Tendência"]
                    ),
                )

                st.progress(
                    int(linha["Índice"]),
                    text=(
                        f'Meta: '
                        f'{formatar_percentual(linha["Meta"])}'
                    ),
                )

                st.write(
                    f'**Status:** {linha["Status"]}'
                )

                st.write(
                    f'**Falhas:** {int(linha["Falhas"])}'
                )

                st.write(
                    "**Incidentes críticos:** "
                    f'{int(linha["Incidentes críticos"])}'
                )

                st.write(
                    "**Cobertura:** "
                    f'{formatar_percentual(linha["Cobertura"])}'
                )

                if linha["Status"] == "Saudável":
                    st.success(
                        "Indicador dentro da meta."
                    )

                elif linha["Status"] == "Atenção":
                    st.warning(
                        "Indicador próximo da meta."
                    )

                else:
                    st.error(
                        "Indicador abaixo da meta."
                    )


st.divider()


# =========================================================
# COMPARAÇÃO ÍNDICE X META
# =========================================================
st.header("Índice atual × meta")

grafico_indice_meta = resumo_filtrado[
    [
        "Característica",
        "Índice",
        "Meta",
    ]
].set_index("Característica")

st.bar_chart(
    grafico_indice_meta,
    use_container_width=True,
)


# =========================================================
# TENDÊNCIA HISTÓRICA
# =========================================================
st.header("Evolução histórica da qualidade")

historico_pivot = historico_filtrado.pivot_table(
    index="Mês",
    columns="Característica",
    values="Índice de qualidade",
    aggfunc="mean",
)

st.line_chart(
    historico_pivot,
    use_container_width=True,
)

st.caption(
    """
    O gráfico representa a evolução simulada do índice de qualidade
    durante os últimos doze meses.
    """
)


# =========================================================
# FALHAS POR CARACTERÍSTICA
# =========================================================
st.header("Falhas registradas")

coluna_falhas, coluna_criticidade = st.columns(2)

with coluna_falhas:
    falhas_por_caracteristica = resumo_filtrado[
        [
            "Característica",
            "Falhas",
        ]
    ].set_index("Característica")

    st.subheader("Quantidade por característica")

    st.bar_chart(
        falhas_por_caracteristica,
        use_container_width=True,
    )

with coluna_criticidade:
    criticidade = (
        resumo_filtrado["Criticidade"]
        .value_counts()
        .rename_axis("Criticidade")
        .reset_index(name="Quantidade")
    )

    st.subheader("Distribuição por criticidade")

    st.bar_chart(
        criticidade.set_index("Criticidade"),
        use_container_width=True,
    )


# =========================================================
# TABELA CONSOLIDADA
# =========================================================
st.header("Painel consolidado dos indicadores")

tabela_resumo = resumo_filtrado.copy()

tabela_resumo["Índice"] = tabela_resumo[
    "Índice"
].apply(formatar_percentual)

tabela_resumo["Meta"] = tabela_resumo[
    "Meta"
].apply(formatar_percentual)

tabela_resumo["Tendência"] = tabela_resumo[
    "Tendência"
].apply(
    lambda valor: (
        f"+{formatar_percentual(valor)}"
        if valor > 0
        else formatar_percentual(valor)
    )
)

tabela_resumo["Cobertura"] = tabela_resumo[
    "Cobertura"
].apply(formatar_percentual)

tabela_resumo["Disponibilidade"] = tabela_resumo[
    "Disponibilidade"
].apply(formatar_percentual)

tabela_resumo["Conformidade"] = tabela_resumo[
    "Conformidade"
].apply(formatar_percentual)

tabela_resumo = tabela_resumo[
    [
        "Característica",
        "Índice",
        "Meta",
        "Status",
        "Falhas",
        "Incidentes críticos",
        "Tendência",
        "Cobertura",
        "Disponibilidade",
        "Conformidade",
    ]
]

st.dataframe(
    tabela_resumo,
    use_container_width=True,
    hide_index=True,
)


st.divider()


# =========================================================
# MONITORAMENTO DOS TESTES
# =========================================================
st.header("Monitoramento dos testes")

total_testes = int(testes_filtrados["Executados"].sum())
testes_aprovados = int(testes_filtrados["Aprovados"].sum())
testes_reprovados = int(testes_filtrados["Reprovados"].sum())

taxa_aprovacao = (
    testes_aprovados / total_testes * 100
    if total_testes > 0
    else 0
)

cobertura_media = (
    testes_filtrados["Cobertura"].mean()
    if not testes_filtrados.empty
    else 0
)

teste_1, teste_2, teste_3, teste_4 = st.columns(4)

with teste_1:
    st.metric(
        label="Testes executados",
        value=formatar_inteiro(total_testes),
    )

with teste_2:
    st.metric(
        label="Testes aprovados",
        value=formatar_inteiro(testes_aprovados),
    )

with teste_3:
    st.metric(
        label="Testes reprovados",
        value=formatar_inteiro(testes_reprovados),
    )

with teste_4:
    st.metric(
        label="Taxa de aprovação",
        value=formatar_percentual(taxa_aprovacao),
    )

coluna_resultado_testes, coluna_cobertura = st.columns(2)

with coluna_resultado_testes:
    dados_resultado = pd.DataFrame(
        {
            "Resultado": [
                "Aprovados",
                "Reprovados",
            ],
            "Quantidade": [
                testes_aprovados,
                testes_reprovados,
            ],
        }
    ).set_index("Resultado")

    st.subheader("Resultado geral")

    st.bar_chart(
        dados_resultado,
        use_container_width=True,
    )

with coluna_cobertura:
    cobertura_por_item = testes_filtrados[
        [
            "Característica",
            "Cobertura",
        ]
    ].set_index("Característica")

    st.subheader(
        "Cobertura por característica"
    )

    st.bar_chart(
        cobertura_por_item,
        use_container_width=True,
    )

st.info(
    f"""
    Cobertura média dos testes:
    **{formatar_percentual(cobertura_media)}**.
    """
)


# =========================================================
# EVENTOS E INCIDENTES
# =========================================================
st.header("Eventos e incidentes recentes")

if eventos_filtrados.empty:
    st.info(
        "Nenhum evento corresponde aos filtros selecionados."
    )

else:
    eventos_exibicao = eventos_filtrados.copy()

    eventos_exibicao["Data"] = eventos_exibicao[
        "Data"
    ].dt.strftime("%d/%m/%Y %H:%M")

    st.dataframe(
        eventos_exibicao.sort_values(
            "Data",
            ascending=False,
        ),
        use_container_width=True,
        hide_index=True,
    )

    eventos_criticos_abertos = eventos_filtrados[
        (eventos_filtrados["Severidade"] == "Crítica")
        & (eventos_filtrados["Status"] != "Resolvido")
    ]

    if not eventos_criticos_abertos.empty:
        st.error(
            f"""
            Existem **{len(eventos_criticos_abertos)}**
            eventos críticos ainda não resolvidos.
            """
        )

    else:
        st.success(
            "Não existem eventos críticos abertos nos filtros atuais."
        )


st.divider()


# =========================================================
# ANÁLISE DE RISCO
# =========================================================
st.header("Mapa de risco")

mapa_risco = resumo_filtrado.copy()

mapa_risco["Risco"] = (
    (100 - mapa_risco["Índice"])
    * 0.5
    + mapa_risco["Falhas"]
    * 1.5
    + mapa_risco["Incidentes críticos"]
    * 10
)

mapa_risco["Prioridade"] = pd.cut(
    mapa_risco["Risco"],
    bins=[-1, 20, 40, 60, 1000],
    labels=[
        "Baixa",
        "Média",
        "Alta",
        "Crítica",
    ],
)

mapa_risco = mapa_risco.sort_values(
    "Risco",
    ascending=False,
)

tabela_risco = mapa_risco[
    [
        "Característica",
        "Índice",
        "Falhas",
        "Incidentes críticos",
        "Risco",
        "Prioridade",
    ]
].copy()

tabela_risco["Índice"] = tabela_risco[
    "Índice"
].apply(formatar_percentual)

tabela_risco["Risco"] = tabela_risco[
    "Risco"
].apply(
    lambda valor: formatar_decimal(valor, 1)
)

st.dataframe(
    tabela_risco,
    use_container_width=True,
    hide_index=True,
)

caracteristica_maior_risco = (
    mapa_risco.iloc[0]["Característica"]
)

st.warning(
    f"""
    A característica com maior prioridade de atuação é
    **{caracteristica_maior_risco}**.
    """
)


# =========================================================
# PLANO DE AÇÃO
# =========================================================
st.header("Plano de ação sugerido")

planos = []

for _, linha in mapa_risco.iterrows():
    nome = linha["Característica"]

    if linha["Status"] == "Saudável":
        acao = (
            "Manter o monitoramento e revisar os indicadores "
            "na próxima avaliação."
        )

    elif nome == "Segurança":
        acao = (
            "Corrigir vulnerabilidades críticas, revisar controles "
            "de acesso e ampliar os testes de segurança."
        )

    elif nome == "Eficiência de Desempenho":
        acao = (
            "Analisar consultas lentas, consumo de recursos e "
            "tempo de resposta das operações críticas."
        )

    elif nome == "Usabilidade":
        acao = (
            "Revisar fluxos, mensagens, formulários e realizar "
            "testes com usuários."
        )

    elif nome == "Confiabilidade":
        acao = (
            "Revisar mecanismos de retry, contingência, logs e "
            "recuperação automática."
        )

    elif nome == "Manutenibilidade":
        acao = (
            "Reduzir duplicações, aumentar cobertura de testes e "
            "refatorar módulos com alto acoplamento."
        )

    elif nome == "Portabilidade":
        acao = (
            "Remover configurações fixas e validar a aplicação em "
            "Windows, Linux e contêineres."
        )

    elif nome == "Compatibilidade":
        acao = (
            "Ampliar testes de integração e validar formatos e "
            "versões suportadas."
        )

    else:
        acao = (
            "Revisar requisitos e ampliar os testes funcionais."
        )

    planos.append(
        {
            "Prioridade": str(linha["Prioridade"]),
            "Característica": nome,
            "Status atual": linha["Status"],
            "Responsável sugerido": {
                "Adequação Funcional": "Produto e QA",
                "Eficiência de Desempenho": "Back-End e Infraestrutura",
                "Compatibilidade": "Integração",
                "Usabilidade": "UX e Produto",
                "Confiabilidade": "Plataforma e SRE",
                "Segurança": "Segurança da Informação",
                "Manutenibilidade": "Desenvolvimento",
                "Portabilidade": "DevOps",
            }[nome],
            "Ação recomendada": acao,
        }
    )

st.dataframe(
    pd.DataFrame(planos),
    use_container_width=True,
    hide_index=True,
)


st.divider()


# =========================================================
# DEFINIÇÃO DOS KPIs
# =========================================================
st.header("Definição dos principais KPIs")

kpis = [
    {
        "Característica": "Adequação Funcional",
        "KPI principal": "Percentual de requisitos atendidos",
        "Meta": "≥ 95%",
        "Interpretação": (
            "Mede quantas funções entregues atendem corretamente "
            "aos requisitos definidos."
        ),
    },
    {
        "Característica": "Eficiência de Desempenho",
        "KPI principal": "Operações dentro do tempo esperado",
        "Meta": "≥ 90%",
        "Interpretação": (
            "Mede a proporção de operações concluídas dentro do "
            "tempo máximo definido."
        ),
    },
    {
        "Característica": "Compatibilidade",
        "KPI principal": "Taxa de sucesso das integrações",
        "Meta": "≥ 92%",
        "Interpretação": (
            "Mede a quantidade de integrações concluídas sem "
            "falhas de formato ou comunicação."
        ),
    },
    {
        "Característica": "Usabilidade",
        "KPI principal": "Taxa de conclusão das tarefas",
        "Meta": "≥ 88%",
        "Interpretação": (
            "Mede a proporção de usuários que concluem as tarefas "
            "sem ajuda ou abandono."
        ),
    },
    {
        "Característica": "Confiabilidade",
        "KPI principal": "Disponibilidade do serviço",
        "Meta": "≥ 99%",
        "Interpretação": (
            "Mede o percentual de tempo em que o sistema permanece "
            "disponível e operacional."
        ),
    },
    {
        "Característica": "Segurança",
        "KPI principal": "Controles de segurança conformes",
        "Meta": "≥ 95%",
        "Interpretação": (
            "Mede a conformidade dos controles, vulnerabilidades "
            "e incidentes registrados."
        ),
    },
    {
        "Característica": "Manutenibilidade",
        "KPI principal": "Índice de código manutenível",
        "Meta": "≥ 85%",
        "Interpretação": (
            "Considera cobertura de testes, duplicação, "
            "complexidade e tempo de alteração."
        ),
    },
    {
        "Característica": "Portabilidade",
        "KPI principal": "Ambientes homologados com sucesso",
        "Meta": "≥ 90%",
        "Interpretação": (
            "Mede a capacidade de instalar e executar o sistema "
            "nos ambientes definidos."
        ),
    },
]

st.dataframe(
    pd.DataFrame(kpis),
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# EXPORTAÇÃO DOS DADOS
# =========================================================
st.header("Exportar relatório")

csv_resumo = resumo_filtrado.to_csv(
    index=False,
    sep=";",
    decimal=",",
).encode("utf-8-sig")

csv_eventos = eventos_filtrados.to_csv(
    index=False,
    sep=";",
).encode("utf-8-sig")

coluna_exportar_1, coluna_exportar_2 = st.columns(2)

with coluna_exportar_1:
    st.download_button(
        label="⬇️ Baixar indicadores em CSV",
        data=csv_resumo,
        file_name="indicadores_qualidade.csv",
        mime="text/csv",
        use_container_width=True,
    )

with coluna_exportar_2:
    st.download_button(
        label="⬇️ Baixar eventos em CSV",
        data=csv_eventos,
        file_name="eventos_qualidade.csv",
        mime="text/csv",
        use_container_width=True,
    )


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    O dashboard consolida indicadores das oito características de
    qualidade e permite acompanhar metas, tendências, falhas, testes,
    riscos e eventos críticos.

    Em um ambiente real, os valores poderiam ser coletados de ferramentas
    de testes, logs, monitoramento, pipelines de CI/CD, sistemas de chamados,
    scanners de segurança e plataformas de observabilidade.
    """
)


# =========================================================
# BOTÃO FINAL
# =========================================================
if st.button(
    "🏠 Voltar para a página inicial",
    key="voltar_inicio_final_dashboard",
    use_container_width=True,
):
    voltar_para_inicio()
