import streamlit as st
import plotly.graph_objects as go

# ----------------------------
# CONFIGURAÇÃO DA PÁGINA
# ----------------------------
st.set_page_config(
    page_title="Dashboard BR Bank",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# CABEÇALHO E INTRODUÇÃO
# ----------------------------
st.title("📊 Dashboard Tático – BR Bank")
st.markdown(
    """
    Este painel central resume os principais indicadores da jornada do cliente:
    **Visitantes → Leads → Clientes**, com foco em aquisição, conversão e crescimento sustentável.

    Acompanhe o funil completo, entenda gargalos e tome decisões com base em dados.
    """
)

st.divider()

# ----------------------------
# GRÁFICO DE FUNIL DE CONVERSÃO
# ----------------------------
st.subheader("🎯 Funil de Conversão: Etapas da Jornada do Cliente")

# Dados representando a jornada
etapas = ["Visitantes no site", "Leads cadastrados", "Clientes convertidos"]
valores = [1421300, 2158, 499]

# Criação do gráfico de funil
fig = go.Figure(go.Funnel(
    y=etapas,
    x=valores,
    textinfo="value+percent previous+percent initial",
    marker={
        "color": ["#1f77b4", "#ff7f0e", "#2ca02c"]
    },
    connector={"line": {"color": "gray", "dash": "dot"}}
))

# Ajustes visuais do layout
fig.update_layout(
    height=500,
    margin=dict(t=40, l=80, r=80, b=40),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# ORIENTAÇÃO PARA O USUÁRIO
# ----------------------------
st.info(
    "📌 Utilize o menu lateral esquerdo para navegar entre as seções: "
    "**Aquisição**, **Retenção**, **Monetização**, **Performance** e **Exploração Analítica**."
)

st.caption("Projeto de Estudo • Fintech BR Bank • Desenvolvido por Daniele Kaloi – 2025")
