import streamlit as st

# Todos arquivos estão vindo da pasta app.py, foi criado um dicionario.
st.set_page_config(
    page_title="Dados do Usuário",
    page_icon="♟️")

st.markdown("""
# Contrato de Trabalho

Nos termos descritos acima, se você marcar como aceito,
poderá realizar o seu cadastro.

""")
aceito = st.sheckbox(Eu aceito os Termos")

if aceito:
    nome = st.text_input("Digite o seu nome:")
    idade = st.number_input("Digite a sua idade:")
    data = st.date_input("Data de contratação", format="DD/MM/YYY")

