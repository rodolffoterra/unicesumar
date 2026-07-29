import csv
import os
import platform
import shutil
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st


# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Portabilidade",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CONSTANTES
# =========================================================
PAGINA_INICIAL = "app.py"

ARQUIVO_CLIENTES = "clientes.csv"

CAMINHO_FIXO_WINDOWS = (
    r"C:\sistema_loja\dados\clientes.csv"
)

CLIENTES_DEMONSTRACAO = [
    {
        "id": 1,
        "nome": "Ana Souza",
        "cidade": "Maringá",
        "estado": "PR",
    },
    {
        "id": 2,
        "nome": "Bruno Lima",
        "cidade": "Londrina",
        "estado": "PR",
    },
    {
        "id": 3,
        "nome": "Carla Mendes",
        "cidade": "Curitiba",
        "estado": "PR",
    },
    {
        "id": 4,
        "nome": "Daniel Silva",
        "cidade": "São Paulo",
        "estado": "SP",
    },
    {
        "id": 5,
        "nome": "Eduarda Costa",
        "cidade": "Florianópolis",
        "estado": "SC",
    },
]


# =========================================================
# ESTADO DA APLICAÇÃO
# =========================================================
if "resultado_nao_portavel" not in st.session_state:
    st.session_state.resultado_nao_portavel = None

if "resultado_portavel" not in st.session_state:
    st.session_state.resultado_portavel = None

if "diretorio_portabilidade" not in st.session_state:
    st.session_state.diretorio_portabilidade = None


# =========================================================
# NAVEGAÇÃO
# =========================================================
def voltar_para_inicio() -> None:
    """
    Retorna para a página inicial da aplicação.
    """

    st.switch_page(PAGINA_INICIAL)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def formatar_tempo(segundos: float) -> str:
    """
    Formata o tempo de execução.
    """

    if segundos >= 1:
        return f"{segundos:.2f} segundos"

    return f"{segundos * 1000:.2f} ms"


def identificar_sistema_operacional() -> str:
    """
    Retorna uma descrição do sistema operacional atual.
    """

    sistema = platform.system()
    versao = platform.release()

    return f"{sistema} {versao}"


def identificar_separador() -> str:
    """
    Retorna o separador de diretórios utilizado pelo sistema.
    """

    return os.sep


def criar_diretorio_demonstracao() -> Path:
    """
    Cria um diretório temporário para a demonstração portável.
    """

    diretorio_existente = (
        st.session_state.diretorio_portabilidade
    )

    if diretorio_existente:
        caminho_existente = Path(diretorio_existente)

        if caminho_existente.exists():
            return caminho_existente

    diretorio = Path(
        tempfile.mkdtemp(
            prefix="demonstracao_portabilidade_"
        )
    )

    st.session_state.diretorio_portabilidade = str(
        diretorio
    )

    return diretorio


def criar_arquivo_clientes(
    caminho_arquivo: Path,
) -> None:
    """
    Cria um arquivo CSV para a demonstração.
    """

    caminho_arquivo.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with caminho_arquivo.open(
        mode="w",
        newline="",
        encoding="utf-8",
    ) as arquivo:
        campos = [
            "id",
            "nome",
            "cidade",
            "estado",
        ]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos,
        )

        escritor.writeheader()
        escritor.writerows(CLIENTES_DEMONSTRACAO)


def ler_arquivo_clientes(
    caminho_arquivo: Path,
) -> List[Dict[str, str]]:
    """
    Lê o arquivo CSV utilizando configuração portável.
    """

    with caminho_arquivo.open(
        mode="r",
        newline="",
        encoding="utf-8",
    ) as arquivo:
        leitor = csv.DictReader(arquivo)

        return list(leitor)


def caminho_compativel_com_sistema(
    caminho: str,
) -> bool:
    """
    Verifica se o formato do caminho é compatível com o sistema atual.

    A função é utilizada apenas para fins didáticos.
    """

    sistema = platform.system()

    caminho_windows = (
        len(caminho) >= 3
        and caminho[1:3] == ":\\"
    )

    if sistema == "Windows":
        return caminho_windows

    return not caminho_windows


# =========================================================
# SISTEMA NÃO PORTÁVEL
# =========================================================
def executar_sistema_nao_portavel() -> Dict[str, Any]:
    """
    Simula uma aplicação dependente de um ambiente específico.

    O código presume que:

    - o sistema operacional é Windows;
    - o disco utilizado é C:;
    - o diretório sistema_loja existe;
    - o arquivo está em um caminho fixo;
    - a estrutura nunca será modificada.
    """

    inicio = time.perf_counter()

    barra = st.progress(0)
    status = st.empty()

    etapas = [
        "Carregando configuração fixa...",
        "Verificando o caminho absoluto...",
        "Tentando localizar o arquivo...",
        "Tentando realizar a leitura...",
    ]

    for indice, etapa in enumerate(etapas, start=1):
        percentual = int(
            (indice / len(etapas)) * 100
        )

        status.info(f"⏳ {etapa}")

        barra.progress(
            percentual,
            text=f"Execução: {percentual}%",
        )

        time.sleep(0.3)

    sistema_atual = identificar_sistema_operacional()

    caminho_compativel = caminho_compativel_com_sistema(
        CAMINHO_FIXO_WINDOWS
    )

    caminho_existe = Path(
        CAMINHO_FIXO_WINDOWS
    ).exists()

    if not caminho_compativel:
        tempo_total = time.perf_counter() - inicio

        status.error(
            "❌ O caminho utilizado não é compatível com "
            "o sistema operacional atual."
        )

        return {
            "sucesso": False,
            "sistema": sistema_atual,
            "caminho": CAMINHO_FIXO_WINDOWS,
            "caminho_compativel": False,
            "arquivo_existe": False,
            "registros": [],
            "tempo": tempo_total,
            "erro": (
                "A aplicação utiliza um caminho absoluto do Windows, "
                "mas está sendo executada em outro sistema operacional."
            ),
        }

    if not caminho_existe:
        tempo_total = time.perf_counter() - inicio

        status.error(
            "❌ O caminho é compatível com o sistema, mas o "
            "arquivo não foi encontrado."
        )

        return {
            "sucesso": False,
            "sistema": sistema_atual,
            "caminho": CAMINHO_FIXO_WINDOWS,
            "caminho_compativel": True,
            "arquivo_existe": False,
            "registros": [],
            "tempo": tempo_total,
            "erro": (
                "O sistema depende de um diretório específico que "
                "não existe neste ambiente."
            ),
        }

    try:
        with open(
            CAMINHO_FIXO_WINDOWS,
            mode="r",
            encoding="utf-8",
        ) as arquivo:
            leitor = csv.DictReader(arquivo)
            registros = list(leitor)

        tempo_total = time.perf_counter() - inicio

        status.success(
            "✅ O arquivo foi localizado e lido."
        )

        return {
            "sucesso": True,
            "sistema": sistema_atual,
            "caminho": CAMINHO_FIXO_WINDOWS,
            "caminho_compativel": True,
            "arquivo_existe": True,
            "registros": registros,
            "tempo": tempo_total,
            "erro": None,
        }

    except Exception as erro:
        tempo_total = time.perf_counter() - inicio

        status.error(
            "❌ Ocorreu um erro durante a leitura."
        )

        return {
            "sucesso": False,
            "sistema": sistema_atual,
            "caminho": CAMINHO_FIXO_WINDOWS,
            "caminho_compativel": caminho_compativel,
            "arquivo_existe": caminho_existe,
            "registros": [],
            "tempo": tempo_total,
            "erro": str(erro),
        }


# =========================================================
# SISTEMA PORTÁVEL
# =========================================================
def executar_sistema_portavel() -> Dict[str, Any]:
    """
    Executa uma implementação independente de caminho absoluto.

    A aplicação utiliza:

    - pathlib;
    - diretório configurável;
    - diretório temporário como alternativa;
    - codificação explícita;
    - criação automática de diretórios.
    """

    inicio = time.perf_counter()

    barra = st.progress(0)
    status = st.empty()

    etapas = [
        "Identificando o sistema operacional...",
        "Carregando a configuração externa...",
        "Criando a estrutura de diretórios...",
        "Criando o arquivo de demonstração...",
        "Lendo os registros...",
        "Validando o resultado...",
    ]

    for indice, etapa in enumerate(etapas, start=1):
        percentual = int(
            (indice / len(etapas)) * 100
        )

        status.info(f"⏳ {etapa}")

        barra.progress(
            percentual,
            text=f"Execução: {percentual}%",
        )

        time.sleep(0.25)

    try:
        diretorio_configurado = os.getenv(
            "DIRETORIO_DADOS"
        )

        if diretorio_configurado:
            diretorio_base = Path(
                diretorio_configurado
            ).expanduser().resolve()

            origem_configuracao = (
                "Variável de ambiente DIRETORIO_DADOS"
            )

        else:
            diretorio_base = (
                criar_diretorio_demonstracao()
            )

            origem_configuracao = (
                "Diretório temporário do sistema"
            )

        caminho_arquivo = (
            diretorio_base
            / "dados"
            / ARQUIVO_CLIENTES
        )

        criar_arquivo_clientes(caminho_arquivo)

        registros = ler_arquivo_clientes(
            caminho_arquivo
        )

        tempo_total = time.perf_counter() - inicio

        status.success(
            "✅ O arquivo foi criado e lido utilizando "
            "recursos portáveis."
        )

        return {
            "sucesso": True,
            "sistema": identificar_sistema_operacional(),
            "separador": identificar_separador(),
            "diretorio_base": str(diretorio_base),
            "caminho": str(caminho_arquivo),
            "origem_configuracao": origem_configuracao,
            "registros": registros,
            "quantidade": len(registros),
            "tempo": tempo_total,
            "erro": None,
        }

    except Exception as erro:
        tempo_total = time.perf_counter() - inicio

        status.error(
            "❌ Não foi possível executar a implementação "
            "portável."
        )

        return {
            "sucesso": False,
            "sistema": identificar_sistema_operacional(),
            "separador": identificar_separador(),
            "diretorio_base": None,
            "caminho": None,
            "origem_configuracao": None,
            "registros": [],
            "quantidade": 0,
            "tempo": tempo_total,
            "erro": str(erro),
        }


def remover_diretorio_temporario() -> None:
    """
    Remove o diretório temporário criado pela demonstração.
    """

    diretorio = (
        st.session_state.diretorio_portabilidade
    )

    if not diretorio:
        return

    caminho = Path(diretorio)

    if caminho.exists():
        shutil.rmtree(
            caminho,
            ignore_errors=True,
        )

    st.session_state.diretorio_portabilidade = None


def reiniciar_demonstracao() -> None:
    """
    Limpa os resultados da demonstração.
    """

    remover_diretorio_temporario()

    st.session_state.resultado_nao_portavel = None
    st.session_state.resultado_portavel = None

    st.rerun()


# =========================================================
# BARRA LATERAL
# =========================================================
with st.sidebar:
    st.title("📦 Portabilidade")

    st.write(
        """
        Esta página demonstra como decisões de implementação
        podem impedir a execução de uma aplicação em outros
        ambientes.
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

    st.subheader("Ambiente atual")

    st.code(
        f"""
Sistema: {identificar_sistema_operacional()}
Separador: {repr(identificar_separador())}
Python: {platform.python_version()}
        """.strip(),
        language="text",
    )

    st.subheader("Aspectos avaliados")

    st.markdown(
        """
        - adaptabilidade;
        - instalabilidade;
        - substituibilidade;
        - independência de plataforma;
        - configuração externa;
        - dependência do ambiente.
        """
    )

    st.warning(
        """
        A falha do sistema não portável é proposital e faz
        parte da demonstração.
        """
    )

    st.caption(
        "Medição e Avaliação da Qualidade de Software"
    )


# =========================================================
# CABEÇALHO
# =========================================================
st.title("📦 Falha de Portabilidade")

st.write(
    """
    Nesta demonstração, dois sistemas precisam ler o mesmo
    arquivo de clientes.

    O primeiro foi desenvolvido considerando somente um computador
    Windows específico.

    O segundo utiliza recursos que permitem sua execução em Windows,
    Linux, macOS, contêineres e serviços de nuvem.
    """
)


# =========================================================
# CONCEITO
# =========================================================
st.info(
    """
    ### O que é Portabilidade?

    Portabilidade avalia o quanto um sistema pode ser transferido,
    instalado, adaptado ou substituído em diferentes ambientes.

    Uma aplicação pode funcionar corretamente no computador do
    desenvolvedor e falhar quando é executada em outro sistema
    operacional, servidor ou contêiner.
    """
)


# =========================================================
# CENÁRIO
# =========================================================
st.header("Cenário da demonstração")

st.write(
    """
    Uma aplicação precisa carregar o arquivo `clientes.csv`.

    Inicialmente, ela foi desenvolvida em um computador Windows e
    utiliza o seguinte caminho:
    """
)

st.code(
    CAMINHO_FIXO_WINDOWS,
    language="text",
)

st.write(
    """
    Posteriormente, a aplicação precisa ser executada em um servidor
    Linux ou dentro de um contêiner.
    """
)

st.success(
    """
    ### Requisito de portabilidade

    A aplicação deve funcionar em diferentes ambientes sem exigir
    alteração no código-fonte.
    """
)


st.divider()


# =========================================================
# EXECUÇÃO
# =========================================================
st.header("Execute as demonstrações")

coluna_nao_portavel, coluna_portavel = st.columns(2)


# =========================================================
# SISTEMA NÃO PORTÁVEL
# =========================================================
with coluna_nao_portavel:
    with st.container(border=True):
        st.subheader("❌ Sistema não portável")

        st.write(
            """
            Esta implementação utiliza:

            - caminho absoluto;
            - unidade de disco fixa;
            - separador específico do Windows;
            - configuração dentro do código;
            - dependência de uma estrutura local.
            """
        )

        st.code(
            r"""
caminho = (
    "C:\\sistema_loja\\dados\\clientes.csv"
)

with open(caminho, "r") as arquivo:
    dados = arquivo.read()
            """.strip(),
            language="python",
        )

        executar_nao_portavel = st.button(
            "Executar sistema não portável",
            key="executar_nao_portavel",
            type="primary",
            use_container_width=True,
        )

        if executar_nao_portavel:
            st.session_state.resultado_portavel = None

            st.session_state.resultado_nao_portavel = (
                executar_sistema_nao_portavel()
            )

            st.rerun()


# =========================================================
# SISTEMA PORTÁVEL
# =========================================================
with coluna_portavel:
    with st.container(border=True):
        st.subheader("✅ Sistema portável")

        st.write(
            """
            Esta implementação utiliza:

            - `pathlib`;
            - configuração externa;
            - caminhos relativos;
            - diretório temporário;
            - codificação explícita;
            - criação automática da estrutura.
            """
        )

        st.code(
            """
from pathlib import Path
import os


diretorio = Path(
    os.getenv(
        "DIRETORIO_DADOS",
        "./dados"
    )
)

caminho = diretorio / "clientes.csv"

with caminho.open(
    "r",
    encoding="utf-8",
) as arquivo:
    dados = arquivo.read()
            """.strip(),
            language="python",
        )

        executar_portavel = st.button(
            "Executar sistema portável",
            key="executar_portavel",
            use_container_width=True,
        )

        if executar_portavel:
            st.session_state.resultado_nao_portavel = None

            st.session_state.resultado_portavel = (
                executar_sistema_portavel()
            )

            st.rerun()


# =========================================================
# RESULTADO NÃO PORTÁVEL
# =========================================================
resultado_nao_portavel = (
    st.session_state.resultado_nao_portavel
)

if resultado_nao_portavel is not None:
    st.divider()

    st.header("Resultado do sistema não portável")

    if resultado_nao_portavel["sucesso"]:
        st.success(
            "O arquivo foi encontrado no caminho fixo."
        )

        st.dataframe(
            resultado_nao_portavel["registros"],
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.error(
            """
            ### Execução interrompida

            A aplicação não conseguiu acessar o arquivo porque
            depende de uma configuração específica de outro ambiente.
            """
        )

    metricas = st.columns(4)

    with metricas[0]:
        st.metric(
            label="Sistema operacional",
            value=resultado_nao_portavel["sistema"],
        )

    with metricas[1]:
        st.metric(
            label="Caminho compatível",
            value=(
                "Sim"
                if resultado_nao_portavel[
                    "caminho_compativel"
                ]
                else "Não"
            ),
        )

    with metricas[2]:
        st.metric(
            label="Arquivo localizado",
            value=(
                "Sim"
                if resultado_nao_portavel[
                    "arquivo_existe"
                ]
                else "Não"
            ),
        )

    with metricas[3]:
        st.metric(
            label="Tempo de execução",
            value=formatar_tempo(
                resultado_nao_portavel["tempo"]
            ),
        )

    st.subheader("Caminho utilizado")

    st.code(
        resultado_nao_portavel["caminho"],
        language="text",
    )

    if resultado_nao_portavel["erro"]:
        st.error(
            resultado_nao_portavel["erro"]
        )

    st.warning(
        """
        Para executar essa aplicação em outro ambiente, seria
        necessário alterar diretamente o código-fonte.
        """
    )


# =========================================================
# RESULTADO PORTÁVEL
# =========================================================
resultado_portavel = (
    st.session_state.resultado_portavel
)

if resultado_portavel is not None:
    st.divider()

    st.header("Resultado do sistema portável")

    if resultado_portavel["sucesso"]:
        st.success(
            """
            ### Execução concluída

            A aplicação identificou o ambiente, criou a estrutura
            necessária e leu o arquivo corretamente.
            """
        )

        metricas = st.columns(4)

        with metricas[0]:
            st.metric(
                label="Sistema operacional",
                value=resultado_portavel["sistema"],
            )

        with metricas[1]:
            st.metric(
                label="Separador utilizado",
                value=repr(
                    resultado_portavel["separador"]
                ),
            )

        with metricas[2]:
            st.metric(
                label="Registros carregados",
                value=str(
                    resultado_portavel["quantidade"]
                ),
            )

        with metricas[3]:
            st.metric(
                label="Tempo de execução",
                value=formatar_tempo(
                    resultado_portavel["tempo"]
                ),
            )

        st.subheader("Configuração utilizada")

        st.write(
            f"""
            **Origem da configuração:**
            {resultado_portavel["origem_configuracao"]}
            """
        )

        st.code(
            resultado_portavel["caminho"],
            language="text",
        )

        st.subheader("Clientes carregados")

        st.dataframe(
            resultado_portavel["registros"],
            use_container_width=True,
            hide_index=True,
        )

        st.info(
            """
            O `pathlib` selecionou automaticamente o separador
            adequado para o sistema operacional atual.
            """
        )

    else:
        st.error(
            """
            Não foi possível executar a implementação portável.
            """
        )

        st.code(
            resultado_portavel["erro"],
            language="text",
        )


st.divider()


# =========================================================
# TESTE DE CAMINHOS
# =========================================================
st.header("Comparação de caminhos")

sistema_atual = platform.system()

caminhos = [
    {
        "Ambiente": "Windows",
        "Caminho fixo": (
            r"C:\sistema_loja\dados\clientes.csv"
        ),
        "Portável no ambiente atual": (
            "Sim"
            if sistema_atual == "Windows"
            else "Não"
        ),
    },
    {
        "Ambiente": "Linux",
        "Caminho fixo": (
            "/opt/sistema_loja/dados/clientes.csv"
        ),
        "Portável no ambiente atual": (
            "Sim"
            if sistema_atual == "Linux"
            else "Não"
        ),
    },
    {
        "Ambiente": "macOS",
        "Caminho fixo": (
            "/Users/usuario/sistema_loja/dados/clientes.csv"
        ),
        "Portável no ambiente atual": (
            "Sim"
            if sistema_atual == "Darwin"
            else "Não"
        ),
    },
    {
        "Ambiente": "Implementação com pathlib",
        "Caminho fixo": "Não utiliza",
        "Portável no ambiente atual": "Sim",
    },
]

st.dataframe(
    caminhos,
    use_container_width=True,
    hide_index=True,
)


st.divider()


# =========================================================
# COMPARAÇÃO DAS IMPLEMENTAÇÕES
# =========================================================
st.header("Comparação das implementações")

comparacao = [
    {
        "Critério": "Caminho de arquivo",
        "Sistema não portável": "Absoluto e fixo",
        "Sistema portável": "Configurável e montado com pathlib",
    },
    {
        "Critério": "Sistema operacional",
        "Sistema não portável": "Dependente do Windows",
        "Sistema portável": "Windows, Linux e macOS",
    },
    {
        "Critério": "Separador",
        "Sistema não portável": "Definido manualmente",
        "Sistema portável": "Selecionado automaticamente",
    },
    {
        "Critério": "Configuração",
        "Sistema não portável": "Dentro do código",
        "Sistema portável": "Variável de ambiente",
    },
    {
        "Critério": "Diretórios",
        "Sistema não portável": "Precisam existir previamente",
        "Sistema portável": "Criados quando necessário",
    },
    {
        "Critério": "Codificação",
        "Sistema não portável": "Pode depender do ambiente",
        "Sistema portável": "UTF-8 explícito",
    },
    {
        "Critério": "Migração",
        "Sistema não portável": "Exige alteração no código",
        "Sistema portável": "Exige somente configuração",
    },
    {
        "Critério": "Contêiner",
        "Sistema não portável": "Difícil adaptação",
        "Sistema portável": "Pode utilizar volume configurável",
    },
]

st.dataframe(
    comparacao,
    use_container_width=True,
    hide_index=True,
)


# =========================================================
# ASPECTOS DE PORTABILIDADE
# =========================================================
st.header("Aspectos de Portabilidade demonstrados")

coluna_1, coluna_2, coluna_3 = st.columns(3)

with coluna_1:
    with st.container(border=True):
        st.subheader("Adaptabilidade")

        st.write(
            """
            Capacidade do sistema de adaptar-se a diferentes
            ambientes sem exigir alterações significativas.
            """
        )

    with st.container(border=True):
        st.subheader("Independência de ambiente")

        st.write(
            """
            Configurações específicas do ambiente não devem ficar
            gravadas diretamente no código-fonte.
            """
        )

with coluna_2:
    with st.container(border=True):
        st.subheader("Instalabilidade")

        st.write(
            """
            Capacidade de instalar e remover o sistema com eficiência
            em diferentes plataformas.
            """
        )

    with st.container(border=True):
        st.subheader("Configuração externa")

        st.write(
            """
            Caminhos, endereços e credenciais devem ser fornecidos
            pelo ambiente de execução.
            """
        )

with coluna_3:
    with st.container(border=True):
        st.subheader("Substituibilidade")

        st.write(
            """
            Capacidade de substituir outro produto ou componente
            com finalidade equivalente.
            """
        )

    with st.container(border=True):
        st.subheader("Empacotamento")

        st.write(
            """
            Dependências e configurações devem permitir uma instalação
            previsível em novos ambientes.
            """
        )


st.divider()


# =========================================================
# CÓDIGO NÃO PORTÁVEL
# =========================================================
st.header("Código com baixa portabilidade")

with st.expander(
    "Visualizar implementação não portável",
    expanded=True,
):
    st.code(
        r"""
import csv


CAMINHO = (
    "C:\\sistema_loja\\dados\\clientes.csv"
)


def carregar_clientes():
    with open(
        CAMINHO,
        mode="r",
    ) as arquivo:
        return list(
            csv.DictReader(arquivo)
        )
        """.strip(),
        language="python",
    )

st.error(
    """
    Problemas dessa implementação:

    - depende da unidade `C:`;
    - depende de uma pasta específica;
    - utiliza um formato de caminho do Windows;
    - exige alteração no código para mudar o diretório;
    - não define explicitamente a codificação;
    - pressupõe que o arquivo já existe.
    """
)


# =========================================================
# CÓDIGO PORTÁVEL
# =========================================================
st.header("Código com boa portabilidade")

with st.expander(
    "Visualizar implementação portável",
    expanded=True,
):
    st.code(
        """
import csv
import os
from pathlib import Path


def obter_diretorio_dados() -> Path:
    diretorio_configurado = os.getenv(
        "DIRETORIO_DADOS",
        "./dados",
    )

    diretorio = Path(
        diretorio_configurado
    ).expanduser().resolve()

    diretorio.mkdir(
        parents=True,
        exist_ok=True,
    )

    return diretorio


def carregar_clientes():
    caminho = (
        obter_diretorio_dados()
        / "clientes.csv"
    )

    with caminho.open(
        mode="r",
        newline="",
        encoding="utf-8",
    ) as arquivo:
        return list(
            csv.DictReader(arquivo)
        )
        """.strip(),
        language="python",
    )

st.success(
    """
    A implementação utiliza a biblioteca `pathlib`, que constrói
    caminhos compatíveis com o sistema operacional atual.
    """
)


st.divider()


# =========================================================
# CONFIGURAÇÃO POR AMBIENTE
# =========================================================
st.header("Configuração em diferentes ambientes")

aba_linux, aba_windows, aba_docker = st.tabs(
    [
        "Linux/macOS",
        "Windows",
        "Docker",
    ]
)

with aba_linux:
    st.code(
        """
export DIRETORIO_DADOS=/opt/sistema_loja/dados

streamlit run app.py
        """.strip(),
        language="bash",
    )

with aba_windows:
    st.code(
        r"""
$env:DIRETORIO_DADOS = "C:\sistema_loja\dados"

streamlit run app.py
        """.strip(),
        language="powershell",
    )

with aba_docker:
    st.code(
        """
docker run \\
  -p 8501:8501 \\
  -e DIRETORIO_DADOS=/app/dados \\
  -v ./dados:/app/dados \\
  sistema-loja
        """.strip(),
        language="bash",
    )

st.info(
    """
    O código da aplicação permanece igual. Somente a configuração
    fornecida pelo ambiente é modificada.
    """
)


st.divider()


# =========================================================
# EXEMPLO DOCKERFILE
# =========================================================
st.header("Exemplo de empacotamento com Docker")

with st.expander(
    "Visualizar Dockerfile",
    expanded=False,
):
    st.code(
        """
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install \\
    --no-cache-dir \\
    -r requirements.txt

COPY . .

ENV DIRETORIO_DADOS=/app/dados

RUN mkdir -p /app/dados

EXPOSE 8501

CMD [
    "streamlit",
    "run",
    "app.py",
    "--server.address=0.0.0.0"
]
        """.strip(),
        language="dockerfile",
    )


# =========================================================
# MÉTRICAS
# =========================================================
st.header("Como medir a Portabilidade?")

metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

with metrica_1:
    st.metric(
        label="Ambientes suportados",
        value="Quantidade",
    )

with metrica_2:
    st.metric(
        label="Alterações para migração",
        value="Arquivos alterados",
    )

with metrica_3:
    st.metric(
        label="Tempo de instalação",
        value="Minutos",
    )

with metrica_4:
    st.metric(
        label="Sucesso da instalação",
        value="Percentual",
    )

st.info(
    """
    Algumas métricas que podem ser utilizadas:

    - quantidade de sistemas operacionais suportados;
    - percentual de instalações concluídas;
    - tempo necessário para instalar o sistema;
    - quantidade de alterações exigidas para uma migração;
    - número de configurações gravadas no código;
    - quantidade de dependências específicas de plataforma;
    - percentual de testes aprovados em diferentes ambientes;
    - tempo necessário para criar um novo ambiente;
    - quantidade de erros durante a instalação;
    - tamanho e complexidade do pacote de distribuição.
    """
)


st.divider()


# =========================================================
# OUTROS EXEMPLOS
# =========================================================
st.header("Outros exemplos de baixa portabilidade")

exemplo_1, exemplo_2, exemplo_3 = st.columns(3)

with exemplo_1:
    with st.container(border=True):
        st.subheader("Banco de dados fixo")

        st.write(
            """
            Endereço, porta e credenciais do banco são escritos
            diretamente no código.
            """
        )

with exemplo_2:
    with st.container(border=True):
        st.subheader("Dependência do sistema")

        st.write(
            """
            A aplicação executa comandos disponíveis somente em
            um sistema operacional.
            """
        )

with exemplo_3:
    with st.container(border=True):
        st.subheader("Dependências ausentes")

        st.write(
            """
            O projeto não possui arquivo de dependências nem informa
            as versões necessárias.
            """
        )


# =========================================================
# IMPACTOS
# =========================================================
st.header("Impactos de um sistema não portável")

coluna_usuario, coluna_empresa = st.columns(2)

with coluna_usuario:
    with st.container(border=True):
        st.subheader("Impactos para o usuário")

        st.markdown(
            """
            - dificuldade de instalação;
            - erros de configuração;
            - incompatibilidade com o dispositivo;
            - necessidade de procedimentos manuais;
            - comportamento diferente entre ambientes;
            - indisponibilidade da aplicação.
            """
        )

with coluna_empresa:
    with st.container(border=True):
        st.subheader("Impactos para a empresa")

        st.markdown(
            """
            - migrações mais demoradas;
            - dependência de infraestrutura específica;
            - aumento dos custos operacionais;
            - dificuldade de adoção da nuvem;
            - dificuldade de conteinerização;
            - maior esforço de suporte;
            - risco de indisponibilidade;
            - limitação na escolha de fornecedores.
            """
        )


st.divider()


# =========================================================
# BOAS PRÁTICAS
# =========================================================
st.header("Boas práticas de Portabilidade")

st.markdown(
    """
    - utilizar `pathlib` para manipular caminhos;
    - evitar caminhos absolutos;
    - utilizar variáveis de ambiente;
    - não manter credenciais no código;
    - definir explicitamente a codificação dos arquivos;
    - manter um arquivo de dependências;
    - fixar versões quando necessário;
    - testar em diferentes sistemas operacionais;
    - utilizar contêineres quando apropriado;
    - evitar comandos específicos de plataforma;
    - separar configuração e código;
    - automatizar a instalação;
    - documentar os requisitos do ambiente;
    - utilizar formatos de dados padronizados;
    - disponibilizar scripts de inicialização.
    """
)

st.warning(
    """
    Portabilidade não significa que todo sistema precisa funcionar
    em todas as plataformas existentes.

    O projeto deve definir os ambientes suportados e reduzir o esforço
    necessário para transferir a aplicação entre eles.
    """
)


st.divider()


# =========================================================
# REINICIAR
# =========================================================
st.header("Reiniciar a demonstração")

if st.button(
    "🗑️ Limpar resultados",
    key="limpar_resultados_portabilidade",
    use_container_width=True,
):
    reiniciar_demonstracao()


# =========================================================
# CONCLUSÃO
# =========================================================
st.success(
    """
    ### Conclusão

    Um sistema portátil não depende de caminhos, configurações ou
    recursos exclusivos do computador em que foi desenvolvido.

    Na implementação não portável, o caminho absoluto do Windows
    impede a execução em outros ambientes ou exige alteração no código.

    Na implementação portável, o caminho é construído com `pathlib`
    e o diretório pode ser fornecido por uma variável de ambiente.

    Dessa forma, a mesma aplicação pode ser executada em Windows,
    Linux, macOS, contêineres ou serviços de nuvem com menor esforço.
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