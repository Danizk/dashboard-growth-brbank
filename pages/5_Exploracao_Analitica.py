import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Exploração Analítica", layout="wide")
st.title("🧠 Exploração Analítica")

st.markdown("Utilize os filtros abaixo para explorar os dados de conversão, receita e tempo médio por vendedor.")

# Base simulada com granularidade para análise
df = pd.DataFrame({
    "Vendedor": ["A", "B", "C", "D", "E"] * 10,
    "Status": ["Convertido"] * 50 + ["Perdido"] * 0,
    "Receita (R$)": [19400, 19900, 19300, 19800, 19000] * 10,
    "Tempo Conversão (dias)": [11, 11, 10, 6, 8] * 10,
    "Data": pd.date_range("2024-01-01", periods=50, freq="D")
})

# Filtros
with st.sidebar:
    st.markdown("### 🎛️ Filtros")
    vendedor_sel = st.multiselect("Filtrar por Vendedor", options=df["Vendedor"].unique(), default=df["Vendedor"].unique())
    data_range = st.date_input("Período", value=(df["Data"].min(), df["Data"].max()))

# Aplicar filtros
df_filtrado = df[
    (df["Vendedor"].isin(vendedor_sel)) &
    (df["Data"] >= pd.to_datetime(data_range[0])) &
    (df["Data"] <= pd.to_datetime(data_range[1]))
]

# Exibição dos dados filtrados
st.markdown("### 📋 Resultados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Gráfico de Receita
st.markdown("### 📊 Receita por Vendedor")
fig_receita = px.bar(
    df_filtrado.groupby("Vendedor")["Receita (R$)"].sum().reset_index(),
    x="Vendedor",
    y="Receita (R$)",
    text="Receita (R$)",
    color="Vendedor",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig_receita.update_traces(texttemplate="R$ %{y:,.0f}", textposition="outside")
st.plotly_chart(fig_receita, use_container_width=True)

# Gráfico de tempo médio
st.markdown("### ⏱️ Tempo Médio de Conversão por Vendedor")
fig_tempo = px.bar(
    df_filtrado.groupby("Vendedor")["Tempo Conversão (dias)"].mean().reset_index(),
    x="Vendedor",
    y="Tempo Conversão (dias)",
    text="Tempo Conversão (dias)",
    color="Vendedor",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig_tempo.update_traces(textposition="outside")
st.plotly_chart(fig_tempo, use_container_width=True)

# Exportar CSV
st.download_button(
    label="⬇️ Exportar dados filtrados",
    data=df_filtrado.to_csv(index=False).encode("utf-8"),
    file_name="exploracao_analitica.csv",
    mime="text/csv"
)
