import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Monetização", layout="wide")
st.title("💰 Dashboard: Monetização")

# Simulando dados dos vendedores
vendedores = ["A", "B", "C", "D", "E"]
receita = [2023026.9, 2068453.65, 1797927.3, 1880748.0, 1965228.0]
conversao = [104, 104, 93, 95, 103]
ticket_medio = [19452.18, 19888.98, 19332.55, 19797.35, 19079.88]
tempo = [11, 11, 10, 6, 8]

df = pd.DataFrame({
    "Vendedor": vendedores,
    "Receita (R$)": receita,
    "Conversões": conversao,
    "Ticket Médio (R$)": ticket_medio,
    "Tempo Médio (dias)": tempo,
})

# Métricas gerais
col1, col2, col3 = st.columns(3)
col1.metric("📈 Receita Total", f"R$ {sum(receita):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col2.metric("🧍‍♂️ Total de Vendedores", len(vendedores))
col3.metric("🎯 Ticket Médio Geral", f"R$ {df['Ticket Médio (R$)'].mean():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Gráfico de barras - Receita por vendedor
st.markdown("### 💼 Receita por Vendedor")
fig1 = px.bar(
    df,
    x="Vendedor",
    y="Receita (R$)",
    text="Receita (R$)",
    color="Vendedor",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig1.update_traces(texttemplate="R$ %{y:,.0f}", textposition="outside")
fig1.update_layout(
    yaxis_title=None,
    xaxis_title=None,
    showlegend=False,
    margin=dict(t=30, b=0)
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico - Tempo médio de conversão
st.markdown("### ⏱️ Tempo médio de conversão por vendedor")
fig2 = px.bar(
    df,
    x="Vendedor",
    y="Tempo Médio (dias)",
    text="Tempo Médio (dias)",
    color="Vendedor",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig2.update_traces(textposition="outside")
fig2.update_layout(showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

# Insights rápidos
st.markdown("### 📌 Mini-Insights")
melhor = df.loc[df["Ticket Médio (R$)"].idxmax()]
pior = df.loc[df["Ticket Médio (R$)"].idxmin()]

with st.expander("🎯 Quem tem o melhor desempenho?"):
    st.success(f"**Vendedor {melhor['Vendedor']}** tem o maior Ticket Médio: **R$ {melhor['Ticket Médio (R$)']:,.2f}**.")

with st.expander("⚠️ Quem precisa de suporte?"):
    st.warning(f"**Vendedor {pior['Vendedor']}** tem o menor Ticket Médio: **R$ {pior['Ticket Médio (R$)']:,.2f}**.")

# Exportar dados
st.download_button(
    label="⬇️ Baixar dados em CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="dados_monetizacao.csv",
    mime="text/csv"
)
