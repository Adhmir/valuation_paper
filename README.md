# 📊 Valuation com ESG (FCFF) – Aplicação em Streamlit

## 📌 Descrição

Este projeto apresenta uma aplicação interativa desenvolvida em Python com Streamlit para avaliação de empresas (com foco em cooperativas), incorporando práticas ESG (Environmental, Social and Governance) no cálculo do valuation.

O modelo integra indicadores qualitativos (via checklist ESG) com um modelo quantitativo de fluxo de caixa descontado (FCFF), ajustando a taxa de crescimento da firma com base no desempenho ESG estimado econometricamente.

## 🎯 Objetivo

Permitir que o usuário:

- Avalie práticas ESG por meio de um questionário estruturado
- Gere automaticamente um índice ESG (iESG)
- Incorpore esse índice na taxa de crescimento da empresa
- Calcule o valor da firma considerando diferentes cenários

## 🧠 Modelo Teórico

O modelo de crescimento ajustado por ESG é dado por:

```
g = g₀ + θ · ln(1 + ESG)
```

Onde:
- `g₀` = crescimento base
- `θ` = coeficiente estimado empiricamente
- `ESG` = índice derivado das práticas informadas

O valuation segue o modelo de fluxo de caixa descontado:

```
V = Σₜⁿ FCFFₜ / (1 + WACC)ᵗ + [FCFFₙ₊₁ / (WACC - g)]
```

## 🏗️ Estrutura da Aplicação

A aplicação é organizada em múltiplas páginas:

```
/pages
│
├── 1_Ambiental.py       → Indicadores ambientais
├── 2_Social.py          → Indicadores sociais
├── 3_Governanca.py      → Indicadores de governança
├── 4_Parametros.py      → Inputs do modelo financeiro
└── 5_Resultados.py      → Valuation e visualizações
└── 6_Sobre.py           → Informações sobre o aplicativo.
```

## 📊 Funcionalidades

- ✔ Coleta de dados ESG via escala Likert (1 a 5)
- ✔ Normalização automática do índice ESG
- ✔ Transformação logarítmica `ln(1 + ESG)`
- ✔ Integração com modelo de crescimento
- ✔ Projeção do FCFF
- ✔ Cálculo do valuation
- ✔ Análise de cenários (pessimista, médio, otimista)
- ✔ Gráficos interativos

## ⚙️ Tecnologias Utilizadas

- Python
- Streamlit
- NumPy
