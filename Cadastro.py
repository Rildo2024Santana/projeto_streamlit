import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    if nome and data_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{data_nasc},{tipo}\n, {endereco},{numero},{ponto},{Tel},{celular}")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False   
    

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🗃️"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Nome do Cliente",
                      key="nome_cliente")

endereco = st.text_input("Endereço")
                 
numero = st.text_input("Número da Casa")

ponto_ref = st.text_input("Ponto de Referência")

tel = st.text_input("Telefone Contato")

celular = st.text_input("Celular")

dt_nasc = st.date_input("Dat. do Cadastro", format="DD/MM/YYYY")

tipo =st.selectbox("Tipo do cliente",
                   [" ", "Pessoa jurídica", "Pessoa física"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome, dt_nasc, tipo, endereco, numero, ponto_ref, tel, celular,])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                icon="❌")
    
 
