import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados simulados
def load_data():
    data = {
        "Receita Total (R$)": 9735383.85,
        "Lucro Líquido (R$)": 8342569.75,
        "Margem Líquida (%)": 85.69,
        "Ticket Médio (R$)": 19509.79,
        "Life Time Value (LTV) (R$)": 19509.79,
        "Vendas por Vendedor": {
            "A": 2023026.90,
            "B": 2068453.65,
            "C": 1797927.30,
            "D": 1880748.00,
            "E": 1965228.00
        },
        "Conversão por Vendedor (%)": {
            "A": 22.61,
            "B": 25.55,
            "C": 22.04,
            "D": 21.54,
            "E": 24.07
        },
        "Tempo Médio para Conversão por Vendedor (dias)": {
            "A": 11,
            "B": 11,
            "C": 10,
            "D": 6,
            "E": 8
        }
    }
    return data

def main():
    st.set_page_config(page_title="Dashboard de Monetização e Receita", layout="wide")
    st.title("📊 Dashboard de Monetização e Receita")
    st.markdown("---")
    
    # Carregar dados
    data = load_data()
    
    # KPIs Principais
    col1, col2, col3 = st.columns(3)
    col1.metric("Receita Total", f"R$ {data['Receita Total (R$)']:,.2f}")
    col2.metric("Lucro Líquido", f"R$ {data['Lucro Líquido (R$)']:,.2f}")
    col3.metric("Margem Líquida", f"{data['Margem Líquida (%)']}%")
    
    col4, col5 = st.columns(2)
    col4.metric("Ticket Médio", f"R$ {data['Ticket Médio (R$)']:,.2f}")
    col5.metric("Life Time Value (LTV)", f"R$ {data['Life Time Value (LTV) (R$)']:,.2f}")
    
    st.markdown("---")
    
    # Gráfico de Receita por Vendedor
    st.subheader("📌 Receita por Vendedor")
    df_vendas = pd.DataFrame({
        "Vendedor": list(data["Vendas por Vendedor"].keys()),
        "Receita (R$)": list(data["Vendas por Vendedor"].values())
    })
    fig_vendas = px.bar(df_vendas, x="Vendedor", y="Receita (R$)", title="Receita Total por Vendedor", color="Vendedor", text="Receita (R$)", color_discrete_sequence=["#A6CEE3"])
    st.plotly_chart(fig_vendas)
    
    # Gráfico de Conversão por Vendedor
    st.subheader("📌 Taxa de Conversão por Vendedor")
    df_conversao = pd.DataFrame({
        "Vendedor": list(data["Conversão por Vendedor (%)"].keys()),
        "Conversão (%)": list(data["Conversão por Vendedor (%)"].values())
    })
    fig_conversao = px.bar(df_conversao, x="Vendedor", y="Conversão (%)", title="Taxa de Conversão por Vendedor", color="Vendedor", text="Conversão (%)", color_discrete_sequence=["#B2DF8A"])
    st.plotly_chart(fig_conversao)
    
    # Gráfico de Tempo Médio de Conversão por Vendedor
    st.subheader("📌 Tempo Médio para Conversão por Vendedor")
    df_tempo = pd.DataFrame({
        "Vendedor": list(data["Tempo Médio para Conversão por Vendedor (dias)"].keys()),
        "Tempo Médio (dias)": list(data["Tempo Médio para Conversão por Vendedor (dias)"].values())
    })
    fig_tempo = px.bar(df_tempo, x="Vendedor", y="Tempo Médio (dias)", title="Tempo Médio para Conversão por Vendedor", color="Vendedor", text="Tempo Médio (dias)", color_discrete_sequence=["#FDBF6F"])
    st.plotly_chart(fig_tempo)
    
if __name__ == "__main__":
    main()
