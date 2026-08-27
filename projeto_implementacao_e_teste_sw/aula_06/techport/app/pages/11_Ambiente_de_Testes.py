import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.utils.test_runner import PROJECT_ROOT, python_command, run_command, show_tool_result

st.set_page_config(page_title="TechPort | Ambiente", page_icon="🧰", layout="wide")
st.title("🧰 1. Ambiente de testes")
st.write("Antes de testar, verificamos se estamos usando o Python correto e se as dependências estão instaladas.")

c1, c2 = st.columns(2)
with c1:
    st.metric("Python em uso", Path(sys.executable).name)
    st.code(sys.executable, language="text")
with c2:
    venv_ok = ".venv" in str(sys.executable).lower()
    if venv_ok:
        st.success("✅ O Streamlit está usando a .venv do projeto.")
    else:
        st.error("❌ O Streamlit NÃO parece estar usando a .venv.")
    st.code(str(PROJECT_ROOT), language="text")

st.subheader("Instalação completa")
st.code("python -m pip install -r requirements.txt", language="powershell")
st.caption("O botão abaixo executa exatamente esse comando usando o mesmo Python que está executando o Streamlit.")

if st.button("📦 Instalar / atualizar requirements", type="primary", use_container_width=True):
    result = run_command(python_command("-m", "pip", "install", "-r", "requirements.txt"), "requirements")
    show_tool_result(result, "✅ Dependências instaladas/atualizadas.", "❌ A instalação encontrou um problema.")

st.subheader("Bibliotecas instaladas")
if st.button("🔎 Executar pip list", use_container_width=True):
    result = run_command(python_command("-m", "pip", "list"), "pip list")
    show_tool_result(result, "✅ Ambiente consultado com sucesso.", "❌ Não foi possível consultar o ambiente.")
