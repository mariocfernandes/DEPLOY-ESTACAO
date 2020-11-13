import pandas as pd
import streamlit as st

# Titulo
st.title('Consulta Estoque ESTACAO')
st.header('Estoques em 13-11-2020')


arquivo = 'est13112020.csv'

@st.cache
def get_data():
    return pd.read_csv(arquivo)

df = get_data()

estoque_total = df['Estoque atual'].sum()
            

st.write('Quantidade total de peças...: '+str(estoque_total))

consulta_estoque = df.groupby('Colecao')['Estoque atual'].agg(['sum']).sort_values(by='sum',ascending = False)

st.table(consulta_estoque)

st.sidebar.subheader("Visualize os Produtos da Coleção...:")

lista_colecao = df.Colecao.unique().tolist()

escolha_selecao = st.sidebar.selectbox("Escolha a Coleção para visualizar os Produtos",
                                     lista_colecao)

df_filtro = df.Colecao == escolha_selecao

cols = ['Produto','Desc Produto','Desc Cor Produto','Grade','Estoque atual']

st.sidebar.dataframe(df[df_filtro][cols])
