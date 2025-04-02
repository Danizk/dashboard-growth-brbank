import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Aquisição", layout="wide")

# Título
st.title("📈 Dashboard: Aquisição de Leads")

# Dados simulados para exemplo
dados = {
    "Fonte": ["Google Ads", "Meta Ads", "Orgânico", "Referência"],
    "Visitantes": [850000, 570000, 200000, 100000],
    "Leads": [208, 138, 72, 34],
    "Conversões": [52, 41, 19, 9],
}

df = pd.DataFrame(dados)
df["Taxa de Conversão (%)"] = (df["Conversões"] / df["Leads"] * 100).round(2)
df["CAC (R$)"] = [5303.51, 2099.16, 0, 0]

# Layout
col1, col2, col3 = st.columns(3)
col1.metric("🔎 Visitantes Totais", f"{df['Visitantes'].sum():,}".replace(",", "."))
col2.metric("📥 Leads Captados", df["Leads"].sum())
col3.metric("✅ Conversões", df["Conversões"].sum())

# Gráfico de Leads por Fonte
st.markdown("### 📊 Leads por Fonte de Aquisição")
fig1 = px.bar(
    df,
    x="Fonte",
    y="Leads",
    color="Fonte",
    text="Leads",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig1.update_layout(
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de Taxa de Conversão por Fonte
st.markdown("### 📉 Taxa de Conversão por Fonte")
fig2 = px.bar(
    df,
    x="Fonte",
    y="Taxa de Conversão (%)",
    color="Fonte",
    text="Taxa de Conversão (%)",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig2.update_layout(
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
st.plotly_chart(fig2, use_container_width=True)

# CAC
st.markdown("### 💸 Custo de Aquisição por Cliente (CAC)")
st.dataframe(
    df[["Fonte", "CAC (R$)"]],
    hide_index=True,
    use_container_width=True,
)

# Expander com explicações
with st.expander("ℹ️ Interpretação dos dados"):
    st.markdown("""
    - **Google Ads** possui o maior volume de visitantes e leads, mas também o CAC mais alto.
    - **Meta Ads** tem um bom equilíbrio entre CAC e taxa de conversão.
    - **Tráfego orgânico** e **referência** têm CAC zero, mas menor volume.
    """)

