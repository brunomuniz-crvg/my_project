import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da página ---
st.set_page_config(page_title="Análise de Veículos", page_icon="🚗", layout="wide")

# --- Leitura do dataset ---
@st.cache_data
def load_data():
    return pd.read_csv(r"\bruno\envs\meus_projetos\vehicles.csv")

car_data = load_data()

# --- Cabeçalho do app ---
st.title("🚗 Análise Exploratória de Veículos")
st.markdown("""
Bem-vindo ao painel interativo de análise de veículos!  
Aqui você pode explorar o conjunto de dados e gerar visualizações dinâmicas com apenas alguns cliques.
""")

st.divider()

# --- Seção: Informações básicas ---
with st.expander("📋 Informações do Dataset"):
    st.write(f"**Número de registros:** {len(car_data)}")
    st.write(f"**Colunas disponíveis:** {', '.join(car_data.columns)}")
    st.dataframe(car_data.head())

st.divider()

# --- Seção: Histograma interativo ---
st.subheader("📊 Distribuição de Valores")
st.write("Escolha uma coluna numérica para visualizar sua distribuição.")

# Escolher a coluna
numeric_cols = car_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
selected_col = st.selectbox("Selecione a coluna para o histograma:", numeric_cols, index=numeric_cols.index("odometer") if "odometer" in numeric_cols else 0)

# Botão para criar histograma
if st.button("Gerar Histograma"):
    st.write(f"Criando histograma para a coluna **{selected_col}**...")
    fig = px.histogram(car_data, x=selected_col, nbins=50,
                       title=f"Distribuição de {selected_col.capitalize()}",
                       color_discrete_sequence=["#00BFFF"])
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- Seção: Gráfico de Dispersão ---
st.subheader("📈 Relação entre Preço e Quilometragem")
st.write("Explore como o preço se relaciona com o odômetro e o tipo de veículo.")

if "price" in car_data.columns and "odometer" in car_data.columns:
    scatter_fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="type" if "type" in car_data.columns else None,
        hover_data=["model", "model_year"] if all(c in car_data.columns for c in ["model", "model_year"]) else None,
        title="Preço vs Quilometragem por Tipo de Veículo",
    )
    st.plotly_chart(scatter_fig, use_container_width=True)
else:
    st.warning("As colunas necessárias ('price', 'odometer') não foram encontradas no dataset.")

st.markdown("---")
st.caption("Desenvolvido com ❤️ em Streamlit e Plotly")

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')


if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')

