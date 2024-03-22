import streamlit as st
import pandas as pd
from PIL import Image

# Configuração da página
st.set_page_config(layout="wide")

# Definindo a cor de fundo
st.markdown("""
<style>
[data-testid=stSidebar] {
    background-color: black;
}
</style>
""", unsafe_allow_html=True)

# Carregando e exibindo a imagem
foto = Image.open('logo.png')
st.sidebar.image(foto, caption='APPLE', use_column_width=True)

# Implementação simples de login
st.sidebar.title("Login")
username = st.sidebar.text_input("Nome de usuário")
password = st.sidebar.text_input("Senha", type="password")

# Verificando as credenciais
if username == "Apple" and password == "123":
    # Carregando os dados do CSV
    df = pd.read_csv("vendas_iphone.csv")

    # Selecionando as colunas relevantes
    df = df[['Modelo', 'Vendas', 'Ano']]

    # Agrupando por modelo e somando as vendas
    df = df.groupby('Modelo').sum()

    # Ordenando por vendas
    df = df.sort_values('Vendas', ascending=False)

    # Exibindo o título
    st.title("Analise de Vendas Apple :iphone:")
    st.subheader("Ano 2020 a 2023")
    
    # Exibindo o modelo mais vendido e menos vendido em duas colunas
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(df)
    with col2:
        st.title("Iphone")
        st.error(f"**Modelo mais vendido:** {df.index[0]}")
        st.error(f"**Modelo menos vendido:** {df.index[-1]}")

    # Título do gráfico
    st.title("Aparelhos disponiveis")    

    # Criando o gráfico de barras
    st.bar_chart(df['Vendas'])
