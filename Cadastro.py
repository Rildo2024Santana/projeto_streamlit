import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome,sexo,end,dt_cadas,tipo):
    if nome and dt_cadas <= date.today():
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
                      key="nome_cliente",
                      max_chars=20)

sexo = st.radio("Escolha o Sexo",
                 ["Masculino","Femenino","Gênero não-binário","Agênero","Gênero-fluido","Bigênero","Mulher transexual","Homem transexual","Poligênero","Neutro"],
               index=2)

end = st.text_input("Endereço",
                         key="input_end",
                         max_chars=25)

dt_cadas = st.date_input("Data do Cadastro", format="DD/MM/YYYY")

tipo =st.selectbox("Tipo do cliente",
                   [" ","Pessoa jurídica", "Pessoa física"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados,
                          args=[nome,sexo,end,dt_cadas,tipo])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro!",
                icon="❌")
