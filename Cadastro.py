import streamlit as st
import pandas as pd
from datetime import date


def grava_dados(nome, endereco,data_cadas, tipo):
    if nome and data_cadas <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{endereco},{data_cadas},{tipo}")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.st_page_config(
    page_title="Cadastro de Cliente",
    page_icon="📕"
)


st.title("Cadastro de Cliente")
st.divider()


nome = st.text_input("Nome do Cliente",
                     key="nome_cliente")

endereco = st.text_input("Endereço",
                         key="endereco")

dt_cadas = st.date_input ("Dta do Cadastro", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo do Cliente",
                    [" ", "Pessoa jurídica", "Pessoa física"])

btn_cadastrar = st.buttom("Cadastrar", 
                          om_click= grava_dados,
                          args=[nome,endereco,dt_cadas,tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌") 
    
 
