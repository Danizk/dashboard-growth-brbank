import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Retenção", layout="wide")
st.title("⏳ Dashboard: Retenção de Leads")

# Dados simulados
dados = {
    "Status": ["Convertido", "Perdido", "Ativo (Follow-up)"],
    "Leads": [499, 1659, 1530],
}

df = pd.DataFrame(dados)
tempo_medio = 9  # dias

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("🧑‍💼 Leads Ativos para Follow-up", dados["Leads"][2])
col2.metric("❌ Leads Perdidos", dados["Leads"][1])
col3.metric("⏱️ Tempo médio de conversão", f"{tempo_medio} dias")

# Gráfico de distribuição de leads
st.markdown("### 🧭 Situação Atual dos Leads")
fig = px.pie(
    df,
    names="Status",
    values="Leads",
    color_discrete_sequence=px.colors.qualitative.Safe,
    hole=0.4,
)
fig.update_layout(
    showlegend=True,
    legend_title_text="Status",
    margin=dict(t=0, b=0),
)
st.plotly_chart(fig, use_container_width=True)

# Gargalos
st.markdown("### 🚨 Principais Motivos de Perda de Leads")
motivos = {
    "Motivo": ["Não retornou contato", "Preço alto", "Vai deixar para depois", "Sem interesse", "Outros"],
    "Leads Perdidos": [1304, 136, 90, 81, 38],
}
df_motivos = pd.DataFrame(motivos)

fig2 = px.bar(
    df_motivos,
    x="Leads Perdidos",
    y="Motivo",
    orientation="h",
    text="Leads Perdidos",
    color="Motivo",
    color_discrete_sequence=px.colors.qualitative.Safe,
)
fig2.update_layout(
    yaxis_title="",
    xaxis_title="Quantidade",
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
st.plotly_chart(fig2, use_container_width=True)

# Expander com estratégia
with st.expander("📌 Ações sugeridas para melhorar a retenção"):
    st.markdown("""
    - Priorizar contato com os **leads ativos** (1530) usando automações.
    - Realizar campanhas específicas para os que alegaram **preço alto**.
    - Criar urgência para leads que disseram **"vai deixar para depois"**.
    - Padronizar a abordagem de vendedores e reforçar treinamentos.
    """)
