# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:53:36 2026

@author: adh_r
"""

import streamlit as st
import numpy as np

st.title("📈 Parâmetros do Valuation")

FCL0 = st.number_input("Fluxo de Caixa Inicial", value=1000.0)
g0 = st.number_input("Crescimento base (g0)", value=0.03)
theta = st.number_input("Impacto ESG (θ)", value=0.02)
WACC = st.number_input("WACC", value=0.10)
g_terminal = st.number_input("Crescimento terminal", value=0.02)
N = st.slider("Períodos", 1, 20, 5)

# cálculo do iESG
dados = (
    st.session_state.ambiental +
    st.session_state.social +
    st.session_state.governanca
)

if len(dados) > 0:
    iesg = np.mean(dados) / 5
    st.session_state.iesg = iesg
    st.write(f"iESG calculado: {iesg:.2f}")
else:
    st.warning("Preencha os dados ESG primeiro.")

if st.button("Calcular Valuation"):
    st.session_state.params = {
        "FCL0": FCL0,
        "g0": g0,
        "theta": theta,
        "WACC": WACC,
        "g_terminal": g_terminal,
        "N": N
    }
    st.switch_page("pages/5_Resultados.py")