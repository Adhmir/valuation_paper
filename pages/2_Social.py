# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:53:03 2026

@author: adh_r
"""

import streamlit as st

st.title("👥 Práticas Sociais")

perguntas = [
    "Número de funcionários",
    "Diversidade",
    "Treinamento",
    "E-learning",
    "Idade média",
    "Dias de treinamento",
    "Pesquisa com funcionários",
    "Acidentes",
    "Absenteísmo",
    "Demissão",
    "Salário mínimo",
    "Ranking GPTW",
    "Voluntários",
    "Processos trabalhistas",
    "Ações sociais",
    "Projetos culturais",
    "Satisfação do cliente",
    "Provisão social",
    "Investimento social"
]

respostas = [st.slider(p, 0, 5, 3) for p in perguntas]

if st.button("Salvar Social"):
    st.session_state.social = respostas
    st.success("Dados sociais salvos!")