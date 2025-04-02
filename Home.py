import plotly.graph_objects as go
import streamlit as st

# Dados simulados
st.subheader("📉 Funil de Conversão Completo")

labels = ["Visitantes", "Leads", "Clientes"]
values = [1421300, 2158, 499]

fig = go.Figure(go.Funnel(
    y = labels,
    x = values,
    textinfo = "value+percent previous+percent initial",
    marker = {
        "color": ["#4682B4", "#FFA500", "#20B2AA"]
    },
    connector = {"line": {"color": "gray", "dash": "dot"}}
))

fig.update_layout(
    height=500,
    margin=dict(t=40, l=100, r=100, b=40),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)
