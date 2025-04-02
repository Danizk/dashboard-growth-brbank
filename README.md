# 📊 Projeto de Estudo – BR Bank

Estudo de caso fictício de análise de dados aplicada à construção de dashboards estratégicos com **Python + Streamlit**.

---

## 🎯 Objetivo Principal

Este projeto tem como objetivo acompanhar toda a jornada do lead — desde o primeiro acesso ao site até a conversão em cliente ativo — e avaliar o desempenho financeiro da fintech BR Bank.

A proposta foi consolidar dados de diferentes fontes (Google Analytics, Google Ads, Meta Ads e CRM) para gerar **insights sobre aquisição, conversão, retenção e monetização**, permitindo decisões rápidas e orientadas por dados.

---

## 📈 Link da aplicação (demo interativa)

[🔗 Acesse o Dashboard BR Bank no Streamlit Cloud](https://dashboard-growth-brbank.streamlit.app)

---

## 🚀 O que este dashboard responde?

### 📊 Métricas Gerais do Negócio

- Receita total da fintech  
- Custo de Tráfego Pago (Google Ads e Meta Ads)  
- Custo do Time de Vendas  
- CAC (Custo de Aquisição por Cliente)  
- LTV (Lifetime Value)  
- Lucro Líquido e Margem Líquida  

### 🧲 Aquisição de Clientes

- Visitantes no Site  
- Leads gerados  
- Conversão Visitantes → Leads  
- Conversão Leads → Clientes  
- Conversão Visitantes → Clientes  
- ROI por canal de mídia paga  

### 💰 Monetização e Performance Comercial

- Receita por vendedor  
- Taxa de conversão por vendedor  
- Tempo médio de conversão  
- Principais motivos de perda  
- Leads ativos para follow-up  

---

## 👥 Usuários Finais

| Perfil                | Ação Esperada                                      |
|-----------------------|----------------------------------------------------|
| **Executivos**        | Acompanhar KPIs e ROI para tomada de decisão       |
| **Marketing & Growth**| Otimizar campanhas, canais e CAC                   |
| **Time de Vendas**    | Identificar gargalos, melhorar abordagem           |
| **Produto & Operações** | Analisar churn, LTV e oportunidades de melhoria |
| **Data & BI**         | Garantir qualidade de dados e análises aprofundadas|

---

## 🧠 Insights Estratégicos

- Público quente (Remarketing) converte mais que público frio?  
- O CAC está sustentável por canal?  
- O número de vendedores é suficiente?  
- Qual vendedor converte mais? Quem precisa de suporte?  
- Onde está o gargalo no funil de conversão?  

---

## 🛠️ Ferramentas Utilizadas

- **Python**
- **Streamlit** (multi-page app)
- **Plotly Express**
- **Pandas**
- **Streamlit Cloud** (deploy gratuito)

---

## 📁 Estrutura do Projeto
📦 dashboard-growth-brbank ├── Home.py # Página inicial com visão geral ├── pages/ │ ├── 1_dashboard_aquisicao.py │ ├── 2_dashboard_retencao.py │ ├── 3_dashboard_monetizacao.py │ ├── 4_dashboard_performance.py │ └── 5_Exploracao_Analitica.py ├── .streamlit/ │ └── config.toml # Tema visual e identidade ├── requirements.txt └── README.md

---

## 🧾 Fontes de Dados Simulados

- **Google Analytics:** Tráfego do site (visitantes)  
- **Google Ads:** Campanhas pagas, cliques, custo, conversões  
- **Meta Ads:** Campanhas no Facebook e Instagram  
- **CRM:** Dados de leads, conversões, perdas e motivos  

---

## 📌 Decisões que o Dashboard Suporta

- Qual canal traz leads mais qualificados?  
- Onde otimizar o investimento em marketing?  
- Quais vendedores têm melhor desempenho?  
- Quais ações tomar com os leads ativos?  
- Como melhorar o ROI, CAC e LTV?  

---

## ⚙️ Tipo de Dashboard

| Classificação            | Objetivo                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| **TÁTICO**               | Acompanhamento semanal/mensal de performance e conversões                |
| **ANALÍTICO**            | Exploração detalhada com filtros livres e geração de hipóteses           |
| **ESTRATÉGICO** (parcial)| Resumo para executivos com visão consolidada dos principais KPIs         |

---

## 🧪 Como Executar Localmente

# 1. Clone o repositório
git clone https://github.com/seu-usuario/dashboard-growth-brbank.git
cd dashboard-growth-brbank

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode o app
streamlit run Home.py

💼 Autor
Daniele Kaloi
Data Analytics • Growth Strategy • Dashboards
🔗 LinkedIn.com/in/danikaloi
