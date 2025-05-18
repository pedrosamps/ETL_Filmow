import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Python-projetos\\ETL_Filmow\\arquivoFilmes\\filmesExtraidos_V0.xlsx')

st.title('🎬 Análise Visual dos Filmes Assistidos')
st.markdown("<hr style='border:1px solid #f63366'>", unsafe_allow_html=True)

st.subheader('📊 Análise Geral')
col1, col2 = st.columns(2)
total_filmes = df.shape[0]
col1.metric(label="🎬 Total de Filmes", value=total_filmes)
diretores_unicos = df['Diretor'].nunique()
col2.metric(label="🎥 Diretores Únicos", value=diretores_unicos)


                            ### GÊNEROS ###
st.subheader('🎭 Gêneros mais assistidos')
df_generos = df.copy()
df_generos['Gênero'] = df_generos['Gênero'].fillna('')  
df_generos = df_generos.assign(Gênero=df_generos['Gênero'].str.split(','))  
df_generos = df_generos.explode('Gênero')  
df_generos['Gênero'] = df_generos['Gênero'].str.strip()  

genero_counts = df_generos['Gênero'].value_counts().sort_values(ascending=False)

st.bar_chart(genero_counts)

genero_selecionado = st.selectbox(
    "Selecione um gênero para ver os filmes assistidos:",
    genero_counts.index
)


filmes_genero = df_generos[df_generos['Gênero'] == genero_selecionado]['Nome'].unique()
with st.expander(f"Filmes do gênero {genero_selecionado} ({len(filmes_genero)})"):
    st.write(filmes_genero)

                            ### DIRETORES ###

df_diretores = df.copy()
df_diretores['Diretor'] = df_diretores['Diretor'].fillna('')
df_diretores = df_diretores.assign(Diretor=df_diretores['Diretor'].str.split(','))
df_diretores = df_diretores.explode('Diretor')
df_diretores['Diretor'] = df_diretores['Diretor'].str.strip()
diretor_counts = df_diretores['Diretor'].value_counts().sort_values(ascending=False)

st.subheader('🏆 Ranking de Diretores que mais assisti filmes')


top_diretores = diretor_counts.head(20).sort_values()
df_top_diretores = top_diretores.reset_index()
df_top_diretores.columns = ['Diretor', 'Quantidade de Filmes']

fig = px.bar(
    df_top_diretores,
    x='Quantidade de Filmes',
    y='Diretor',
    orientation='h',
    labels={'Quantidade de Filmes': 'Quantidade de Filmes'},
    title='Top 20 Diretores mais assistidos'
)
fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=600)
st.plotly_chart(fig)

diretor_selecionado = st.selectbox(
    "Selecione um diretor para ver os filmes assistidos: (lista completa de diretores)",
    diretor_counts.index
)

# Filtra e exibe os filmes do diretor selecionado
filmes_diretor = df_diretores[df_diretores['Diretor'] == diretor_selecionado]['Nome'].unique()
with st.expander(f"Filmes assistidos dirigidos por **{diretor_selecionado}** ({len(filmes_diretor)})"):
    st.write(filmes_diretor)




