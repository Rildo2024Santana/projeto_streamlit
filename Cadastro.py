import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome,endereco,data_cadas,tipo):
    if nome and data_cadas <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{endereco}{data_cadas},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False   
    

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🗃️"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Nome do cliente",
                      key="nome_cliente")

endereco = st.text_input("Endereço")
                     

dt_cadas = st.date_input("Data Cadastro", format="DD/MM/YYYY")

tipo =st.selectbox("Tipo do cliente",
                   ["","Pessoa jurídica", "Pessoa física"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome, dt_cadas, tipo])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                icon="❌")
    
 
