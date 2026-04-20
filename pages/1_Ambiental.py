# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:52:39 2026

@author: adh_r
"""

import streamlit as st

st.title("🌱 Práticas Ambientais")

perguntas = [
    "Emissão de CO2",
    "Consumo de energia por fonte",
    "Quantidade de resíduos",
    "Participa de índices ambientais",
    "Resíduos reciclados",
    "Investimento ambiental",
    "Metas ambientais"
]

respostas = []

for p in perguntas:
    val = st.slider(p, 0, 5, 3)
    respostas.append(val)

if st.button("Salvar Ambiental"):
    st.session_state.ambiental = respostas
    st.success("Dados ambientais salvos!")