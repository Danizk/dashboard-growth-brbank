import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Performance", layout="wide")
st.title("📊 Dashboard: Performance Geral")

# Dados simulados de performance geral
dados = {
    "Visitantes": 1421300,
    "Leads Captados": 2158,
    "Clientes Convertidos": 499,
    "Receita Total": 9735383.85,
    "Lucro Líquido": 8342569.75,
    "ROAS (%)": 698.97,
    "Margem Líquida (%)": 85.69,
    "CAC (R$)": 4025.47,
    "LTV (R$)": 19509.79
}

# KPIs principais
col1, col2, col3 = st.columns(3)
col1.metric("💰 Receita Total", f"R$ {dados['Receita Total']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col2.metric("📉 CAC Médio", f"R$ {dados['CAC (R$)']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col3.metric("📈 LTV", f"R$ {dados['LTV (R$)']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

col4, col5, col6 = st.columns(3)
col4.metric("🏆 Lucro Líquido", f"R$ {dados['Lucro Líquido']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col5.metric("📊 ROAS", f"{dados['ROAS (%)']:.2f}%")
col6.metric("💼 Margem Líquida", f"{dados['Margem Líquida (%)']:.2f}%")

st.divider()

# Funil de conversão
st.markdown("### 🔁 Funil de Conversão")

funil_df = pd.DataFrame({
    "Etapas": ["Visitantes", "Leads", "Clientes"],
    "Quantidade": [dados["Visitantes"], dados["Leads Captados"], dados["Clientes Convertidos"]],
})

fig = px.funnel(
    funil_df,
    x="Quantidade",
    y="Etapas",
    text="Quantidade",
    color="Etapas",
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig.update_traces(textposition="inside", texttemplate="%{text:,.0f}")
fig.update_layout(yaxis_title="", xaxis_title="", showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# Taxas de conversão
st.markdown("### 📌 Taxas de Conversão")

taxa_visitantes_leads = (dados["Leads Captados"] / dados["Visitantes"]) * 100
taxa_leads_clientes = (dados["Clientes Convertidos"] / dados["Leads Captados"]) * 100
taxa_visitantes_clientes = (dados["Clientes Convertidos"] / dados["Visitantes"]) * 100

colA, colB, colC = st.columns(3)
colA.metric("👥 Visitantes → Leads", f"{taxa_visitantes_leads:.2f}%")
colB.metric("🧲 Leads → Clientes", f"{taxa_leads_clientes:.2f}%")
colC.metric("🔄 Visitantes → Clientes", f"{taxa_visitantes_clientes:.2f}%")

# Exportar dados
st.download_button(
    label="⬇️ Baixar dados em CSV",
    data=pd.DataFrame(dados.items(), columns=["Métrica", "Valor"]).to_csv(index=False).encode("utf-8"),
    file_name="dados_performance_geral.csv",
    mime="text/csv"
)
