import os
from typing import Dict, List

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv


# =========================================================
# CONFIGURAÇÃO
# =========================================================

load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000",
)


st.set_page_config(
    page_title="Sakila - Gerenciamento de Atores",
    page_icon="🎬",
    layout="wide",
)


# =========================================================
# FUNÇÕES DE COMUNICAÇÃO COM A API
# =========================================================

def tratar_resposta(resposta: requests.Response):
    """
    Verifica a resposta retornada pela API.

    Se a resposta for válida, retorna o JSON.
    Caso contrário, apresenta o detalhe do erro.
    """

    if resposta.ok:
        return resposta.json()

    try:
        conteudo = resposta.json()
        detalhe = conteudo.get(
            "detail",
            "Ocorreu um erro na API.",
        )
    except ValueError:
        detalhe = resposta.text or "Ocorreu um erro na API."

    raise RuntimeError(detalhe)


def verificar_api() -> Dict:
    """
    Verifica se a API e o banco de dados estão disponíveis.
    """

    resposta = requests.get(
        f"{API_URL}/health",
        timeout=10,
    )

    return tratar_resposta(resposta)


def listar_atores() -> List[Dict]:
    """
    Consulta todos os atores cadastrados.
    """

    resposta = requests.get(
        f"{API_URL}/atores",
        timeout=10,
    )

    return tratar_resposta(resposta)


def buscar_ator(actor_id: int) -> Dict:
    """
    Busca um ator específico pelo ID.
    """

    resposta = requests.get(
        f"{API_URL}/atores/{actor_id}",
        timeout=10,
    )

    return tratar_resposta(resposta)


def cadastrar_ator(
    primeiro_nome: str,
    sobrenome: str,
) -> Dict:
    """
    Cadastra um novo ator.
    """

    dados = {
        "first_name": primeiro_nome,
        "last_name": sobrenome,
    }

    resposta = requests.post(
        f"{API_URL}/atores",
        json=dados,
        timeout=10,
    )

    return tratar_resposta(resposta)


def atualizar_ator(
    actor_id: int,
    primeiro_nome: str,
    sobrenome: str,
) -> Dict:
    """
    Atualiza os dados de um ator.
    """

    dados = {
        "first_name": primeiro_nome,
        "last_name": sobrenome,
    }

    resposta = requests.put(
        f"{API_URL}/atores/{actor_id}",
        json=dados,
        timeout=10,
    )

    return tratar_resposta(resposta)


def excluir_ator(actor_id: int) -> Dict:
    """
    Exclui um ator pelo ID.
    """

    resposta = requests.delete(
        f"{API_URL}/atores/{actor_id}",
        timeout=10,
    )

    return tratar_resposta(resposta)


def carregar_atores() -> List[Dict]:
    """
    Carrega os atores tratando possíveis falhas na API.
    """

    try:
        return listar_atores()

    except requests.ConnectionError:
        st.error(
            "Não foi possível acessar a API. "
            "Execute primeiro o servidor FastAPI."
        )

    except requests.Timeout:
        st.error(
            "A API demorou muito para responder."
        )

    except requests.RequestException as erro:
        st.error(
            f"Erro ao acessar a API: {erro}"
        )

    except RuntimeError as erro:
        st.error(str(erro))

    return []


# =========================================================
# CABEÇALHO
# =========================================================

st.title("🎬 Gerenciamento de Atores")

st.caption(
    "Aplicação Streamlit consumindo uma API FastAPI "
    "conectada ao banco MySQL Sakila."
)


# =========================================================
# STATUS DA API
# =========================================================

try:
    status_api = verificar_api()

    st.success(
        f'API conectada ao banco "{status_api["banco"]}".'
    )

except requests.RequestException:
    st.error(
        "A API não está disponível. "
        "Execute no terminal: "
        "python -m uvicorn app.main:app --reload"
    )

    st.stop()

except RuntimeError as erro:
    st.error(str(erro))
    st.stop()


# =========================================================
# CARREGAMENTO DOS DADOS
# =========================================================

atores = carregar_atores()


# =========================================================
# MÉTRICAS
# =========================================================

coluna_total, coluna_api, coluna_banco = st.columns(3)

coluna_total.metric(
    "Total de atores",
    len(atores),
)

coluna_api.metric(
    "API",
    "Online",
)

coluna_banco.metric(
    "Banco",
    "Sakila",
)


# =========================================================
# ABAS
# =========================================================

aba_listar, aba_consultar, aba_cadastrar, aba_atualizar, aba_excluir = st.tabs(
    [
        "📋 Listar",
        "🔎 Consultar",
        "➕ Cadastrar",
        "✏️ Atualizar",
        "🗑️ Excluir",
    ]
)


# =========================================================
# LISTAR
# =========================================================

with aba_listar:
    st.subheader("Lista de atores")

    if st.button(
        "Atualizar lista",
        use_container_width=True,
        key="botao_atualizar_lista",
    ):
        st.rerun()

    if atores:
        tabela = pd.DataFrame(atores)

        tabela = tabela[
            [
                "actor_id",
                "first_name",
                "last_name",
                "last_update",
            ]
        ]

        tabela = tabela.rename(
            columns={
                "actor_id": "ID",
                "first_name": "Primeiro nome",
                "last_name": "Sobrenome",
                "last_update": "Última atualização",
            }
        )

        st.dataframe(
            tabela,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.info("Nenhum ator encontrado.")


# =========================================================
# CONSULTAR
# =========================================================

with aba_consultar:
    st.subheader("Consultar ator por ID")

    id_consulta = st.number_input(
        "Informe o ID do ator",
        min_value=1,
        step=1,
        key="id_consulta",
    )

    if st.button(
        "Consultar ator",
        use_container_width=True,
        key="botao_consultar",
    ):
        try:
            ator = buscar_ator(
                int(id_consulta)
            )

            st.success("Ator encontrado.")

            coluna1, coluna2 = st.columns(2)

            coluna1.metric(
                "ID",
                ator["actor_id"],
            )

            coluna1.text_input(
                "Primeiro nome",
                value=ator["first_name"],
                disabled=True,
            )

            coluna2.text_input(
                "Sobrenome",
                value=ator["last_name"],
                disabled=True,
            )

            coluna2.text_input(
                "Última atualização",
                value=str(ator["last_update"]),
                disabled=True,
            )

        except requests.RequestException as erro:
            st.error(
                f"Erro ao acessar a API: {erro}"
            )

        except RuntimeError as erro:
            st.error(str(erro))


# =========================================================
# CADASTRAR
# =========================================================

with aba_cadastrar:
    st.subheader("Cadastrar novo ator")

    with st.form(
        "formulario_cadastrar",
        clear_on_submit=True,
    ):
        primeiro_nome = st.text_input(
            "Primeiro nome"
        )

        sobrenome = st.text_input(
            "Sobrenome"
        )

        cadastrar = st.form_submit_button(
            "Cadastrar ator",
            use_container_width=True,
        )

    if cadastrar:
        if not primeiro_nome.strip():
            st.warning(
                "Informe o primeiro nome."
            )

        elif not sobrenome.strip():
            st.warning(
                "Informe o sobrenome."
            )

        else:
            try:
                novo_ator = cadastrar_ator(
                    primeiro_nome=primeiro_nome,
                    sobrenome=sobrenome,
                )

                st.success(
                    "Ator cadastrado com sucesso."
                )

                st.json(novo_ator)

            except requests.RequestException as erro:
                st.error(
                    f"Erro ao acessar a API: {erro}"
                )

            except RuntimeError as erro:
                st.error(str(erro))


# =========================================================
# ATUALIZAR
# =========================================================

with aba_atualizar:
    st.subheader("Atualizar ator")

    if atores:
        opcoes_atualizacao = {
            (
                f'{ator["actor_id"]} — '
                f'{ator["first_name"]} '
                f'{ator["last_name"]}'
            ): ator
            for ator in atores
        }

        ator_escolhido = st.selectbox(
            "Selecione o ator",
            options=list(
                opcoes_atualizacao.keys()
            ),
            key="ator_atualizacao",
        )

        ator_selecionado = opcoes_atualizacao[
            ator_escolhido
        ]

        with st.form(
            "formulario_atualizar"
        ):
            primeiro_nome_atualizado = st.text_input(
                "Primeiro nome",
                value=ator_selecionado[
                    "first_name"
                ],
            )

            sobrenome_atualizado = st.text_input(
                "Sobrenome",
                value=ator_selecionado[
                    "last_name"
                ],
            )

            atualizar = st.form_submit_button(
                "Salvar alterações",
                use_container_width=True,
            )

        if atualizar:
            if not primeiro_nome_atualizado.strip():
                st.warning(
                    "Informe o primeiro nome."
                )

            elif not sobrenome_atualizado.strip():
                st.warning(
                    "Informe o sobrenome."
                )

            else:
                try:
                    ator_atualizado = atualizar_ator(
                        actor_id=ator_selecionado[
                            "actor_id"
                        ],
                        primeiro_nome=primeiro_nome_atualizado,
                        sobrenome=sobrenome_atualizado,
                    )

                    st.success(
                        "Ator atualizado com sucesso."
                    )

                    st.json(ator_atualizado)

                except requests.RequestException as erro:
                    st.error(
                        f"Erro ao acessar a API: {erro}"
                    )

                except RuntimeError as erro:
                    st.error(str(erro))

    else:
        st.info(
            "Não existem atores para atualizar."
        )


# =========================================================
# EXCLUIR
# =========================================================

with aba_excluir:
    st.subheader("Excluir ator")

    if atores:
        opcoes_exclusao = {
            (
                f'{ator["actor_id"]} — '
                f'{ator["first_name"]} '
                f'{ator["last_name"]}'
            ): ator
            for ator in atores
        }

        ator_escolhido_exclusao = st.selectbox(
            "Selecione o ator",
            options=list(
                opcoes_exclusao.keys()
            ),
            key="ator_exclusao",
        )

        ator_exclusao = opcoes_exclusao[
            ator_escolhido_exclusao
        ]

        st.warning(
            "Você está prestes a excluir: "
            f'{ator_exclusao["first_name"]} '
            f'{ator_exclusao["last_name"]}.'
        )

        st.info(
            "Atores relacionados a filmes não podem "
            "ser excluídos por causa das regras de "
            "integridade do banco Sakila."
        )

        confirmar_exclusao = st.checkbox(
            "Confirmo que desejo excluir este ator.",
            key="confirmar_exclusao",
        )

        if st.button(
            "Excluir ator",
            type="primary",
            disabled=not confirmar_exclusao,
            use_container_width=True,
            key="botao_excluir",
        ):
            try:
                resultado = excluir_ator(
                    ator_exclusao["actor_id"]
                )

                st.success(
                    resultado["mensagem"]
                )

                st.json(resultado)

            except requests.RequestException as erro:
                st.error(
                    f"Erro ao acessar a API: {erro}"
                )

            except RuntimeError as erro:
                st.error(str(erro))

    else:
        st.info(
            "Não existem atores para excluir."
        )


# =========================================================
# RODAPÉ
# =========================================================

st.divider()

st.caption(
    f"API utilizada: {API_URL}"
)