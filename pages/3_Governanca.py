# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:53:24 2026

@author: adh_r
"""

import streamlit as st

st.title("🏛️ Governança")

perguntas = [
    "Patentes",
    "Investimento em P&D",
    "Testes tecnológicos",
    "Reconhecimento da marca",
    "Novos produtos",
    "Mudanças organizacionais",
    "Sistemas internos",
    "Vendas de inovação",
    "Separação CEO/Presidente",
    "Presença feminina",
    "Conselheiro independente",
    "Voto delegado",
    "Diretor não associado",
    "Participação nos resultados",
    "Direito de voto",
    "Reembolso de quotas",
    "Comitê ambiental",
    "Remuneração ESG"
]

respostas = [st.slider(p, 0, 5, 3) for p in perguntas]

if st.button("Salvar Governança"):
    st.session_state.governanca = respostas
    st.success("Dados de governança salvos!")