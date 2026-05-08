import streamlit as st
import os
import requests

st.set_page_config(page_title="Biblioteca de Livros")

API_URL = os.getenv('API_URL')

st.title('Gestor de Livros')

with st.sidebar:
    st.header('Novo livro')
    titulo = st.text_input('Digite o Livro')
    autor = st.text_input('Autor')
    if st.button('Cadastrar'):
        if titulo and autor:
            res = requests.post(API_URL, json = {'titulo': titulo,'autor':autor})
            if res.status_code == 200:
                st.success('Livro Salvo')
            else:
                st.error('Ocorreu um Erro')

st.subheader('Livros Dispooniveis')
if st.button('Livros Disponiveis'):
    try:
        livros = requests.get(API_URL)
        for l in livros:
            st.info(f'{l[titulo]} : {l[autor]}')
    except:
        st.error('Não foi possivel conectar a API - verifique... o servidor')

