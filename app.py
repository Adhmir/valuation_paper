# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:51:02 2026

@author: adh_r
"""

import streamlit as st

st.set_page_config(
    page_title="Valuation ESG (Cooperativas)",
    layout="centered"
)

st.title("📊 Valuation ESG para Cooperativas")

st.markdown("""
Este sistema avalia práticas ESG e incorpora os resultados no valuation da cooperativa.

Utilize o menu lateral para navegar entre as etapas:
- Ambiental
- Social
- Governança
- Valuation
- Resultados
""")

# Inicialização de estados
if "ambiental" not in st.session_state:
    st.session_state.ambiental = []

if "social" not in st.session_state:
    st.session_state.social = []

if "governanca" not in st.session_state:
    st.session_state.governanca = []

if "iesg" not in st.session_state:
    st.session_state.iesg = 0