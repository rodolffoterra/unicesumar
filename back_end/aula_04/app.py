import streamlit as st
import logging
import time
from pathlib import Path

st.set_page_config(page_title="Laboratório de Logs", layout="wide")

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "aplicacao.log"

logger = logging.getLogger("lab_logs")
logger.setLevel(logging.DEBUG)
logger.handlers.clear()

handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(message)s",
    "%d/%m/%Y %H:%M:%S"
))
logger.addHandler(handler)

def limpar():
    LOG_FILE.write_text("", encoding="utf-8")

def mostrar_logs(area):
    if LOG_FILE.exists():
        area.code(LOG_FILE.read_text(encoding="utf-8"), language="text")

def executar(etapas, front):
    log_area = st.session_state["log_area"]
    telas=[]
    limpar()
    for nivel,msg,tela in etapas:
        getattr(logger,nivel.lower())(msg)
        telas.append(tela)
        front.markdown("## Front-End\n\n" + "\n\n".join(telas))
        mostrar_logs(log_area)
        time.sleep(0.8)

st.sidebar.title("📚 Laboratório de Logs")
op = st.sidebar.radio(
    "Escolha uma demonstração",
    ["🏠 Introdução","🐞 Bug","🔵 INFO","🟣 DEBUG","🟡 WARNING",
     "🔴 ERROR","🚨 CRITICAL","🎬 Demonstração Completa"]
)

st.title(op)

col1,col2 = st.columns(2)
front = col1.empty()
log = col2.empty()
st.session_state["log_area"] = log

def intro():
    st.markdown("""
### Objetivo

Nesta aplicação cada tela demonstra um nível de log.

À esquerda ocorre uma ação do usuário.

À direita você acompanha os logs sendo gerados em tempo real.

No final existe uma demonstração completa semelhante a uma aplicação real.
""")

def bug():
    st.subheader("O que é um Bug?")
    st.write("Um bug é um comportamento inesperado da aplicação.")
    if st.button("Executar exemplo do Bug"):
        executar([
            ("INFO","Usuário clicou em Salvar","📝 Usuário preenche formulário"),
            ("DEBUG","Validando idade","🔎 Validando dados"),
            ("ERROR","Campo idade inválido","❌ Idade = abc"),
            ("INFO","Mensagem apresentada ao usuário","⚠️ Erro exibido")
        ],front)

def info():
    st.write("INFO registra acontecimentos normais.")
    if st.button("Executar INFO"):
        executar([
            ("INFO","Usuário autenticado","🔐 Login"),
            ("INFO","Token JWT criado","🔑 Token criado"),
            ("INFO","Dashboard carregado","🏠 Dashboard")
        ],front)

def debug():
    st.write("DEBUG auxilia o desenvolvedor.")
    if st.button("Executar DEBUG"):
        executar([
            ("DEBUG","Conectando MySQL","💾 Abrindo conexão"),
            ("DEBUG","Executando SELECT","📄 SELECT * FROM clientes"),
            ("DEBUG","120 registros encontrados","📊 Retornando dados")
        ],front)

def warning():
    st.write("WARNING indica atenção.")
    if st.button("Executar WARNING"):
        executar([
            ("INFO","Consulta iniciada","🔍 Buscando clientes"),
            ("WARNING","Consulta demorou 820 ms","⏳ Sistema lento"),
            ("INFO","Resposta enviada","✅ Clientes carregados")
        ],front)

def error():
    st.write("ERROR representa uma falha tratada.")
    if st.button("Executar ERROR"):
        executar([
            ("INFO","Consultando serviço CEP","🌎 Chamando API"),
            ("ERROR","Timeout serviço externo","❌ Serviço indisponível"),
            ("INFO","Mensagem amigável enviada","🙂 Tente novamente")
        ],front)

def critical():
    st.write("CRITICAL exige ação imediata.")
    if st.button("Executar CRITICAL"):
        executar([
            ("CRITICAL","Espaço em disco abaixo de 5%","💽 Disco cheio"),
            ("CRITICAL","Banco indisponível","🛑 Sistema parado")
        ],front)

def completo():
    if st.button("Executar demonstração completa"):
        executar([
            ("INFO","Aplicação iniciada","🟢 Inicializando aplicação..."),
            ("INFO","Usuário autenticado","🔐 Login realizado"),
            ("INFO","GET /clientes","📥 Consultando clientes"),
            ("DEBUG","Executando consulta SQL","💾 Consultando banco"),
            ("WARNING","Consulta demorou 820 ms","⚠️ Resposta mais lenta"),
            ("ERROR","Falha temporária ao consultar serviço externo","🌐 Tentando integração"),
            ("INFO","Retry executado com sucesso","🔁 Nova tentativa"),
            ("CRITICAL","Espaço em disco abaixo de 5%","💽 Alerta crítico"),
            ("INFO","Resposta enviada ao cliente","✅ Finalizado")
        ],front)
        st.divider()
        st.subheader("Log completo")
        st.code(LOG_FILE.read_text(encoding="utf-8"), language="text")
        st.download_button("Baixar log",
            LOG_FILE.read_bytes(),
            file_name="aplicacao.log",
            mime="text/plain")

{
"🏠 Introdução":intro,
"🐞 Bug":bug,
"🔵 INFO":info,
"🟣 DEBUG":debug,
"🟡 WARNING":warning,
"🔴 ERROR":error,
"🚨 CRITICAL":critical,
"🎬 Demonstração Completa":completo
}[op]()