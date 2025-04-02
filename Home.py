import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🏦 BR Bank | Dashboard Geral", layout="wide")

st.title("📊 Visão Geral – BR Bank")
st.markdown("Bem-vindo ao painel estratégico da fintech BR Bank. Aqui você poderá acompanhar a jornada completa do lead à conversão, além de avaliar performance comercial e resultados financeiros.")

st.markdown("---")

# 🔹 Dados principais (simulados)
visitantes = 1421300
leads = 2158
clientes = 499
receita_total = 9735383.85
lucro_liquido = 8342569.75
ticket_medio = 19509.79
ltv = 19509.79

# ✅ KPIs de negócio
col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {receita_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col2.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

col4, col5 = st.columns(2)
col4.metric("Leads Captados", f"{leads:,}".replace(",", "."))
col5.metric("Clientes Convertidos", f"{clientes:,}".replace(",", "."))

st.markdown("---")

# 🔄 Funil de Conversão
st.subheader("🔄 Funil de Conversão: Visitantes → Leads → Clientes")

df_funnel = pd.DataFrame({
    "Etapa": ["Visitantes", "Leads", "Clientes"],
    "Quantidade": [visitantes, leads, clientes]
})

fig = px.funnel(df_funnel, x="Quantidade", y="Etapa", color="Etapa", color_discrete_sequence=["#4E79A7", "#F28E2B", "#76B7B2"])
fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font=dict(color="#FFFFFF"))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("➡️ Use o menu lateral para navegar entre os dashboards: **Aquisição, Retenção, Monetização, Performance e Exploração Analítica**.")
