import streamlit as st 
import numpy as np

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Resultados ESG (FCFF)", layout="centered")

# =========================
# PARÂMETROS DA REGRESSÃO
# =========================
THETA_MEAN = 0.0145414
THETA_LOW = -0.0007664
THETA_HIGH = 0.0298491
   



# =========================
# PARÂMETROS PADRÃO
# =========================
DEFAULTS = {
    "g_base": 0.03,
    "g_terminal": 0.025,
    "wacc": 0.10
}

# =========================
# FUNÇÕES
# =========================
def estimate_growth(esg, g_base, theta):
    g_esg = theta * np.log1p(esg)
    g_total = g_base + g_esg
    return g_total, g_esg

def project_fcff(fcff_0, g, n=5):
    return [fcff_0 * (1 + g)**t for t in range(1, n+1)]

def fcff_valuation(fcff, wacc, g_terminal):
    value = 0
    for t, f in enumerate(fcff, start=1):
        value += f / ((1 + wacc)**t)

    terminal = fcff[-1] * (1 + g_terminal) / (wacc - g_terminal)
    terminal /= (1 + wacc)**len(fcff)

    return value + terminal

# =========================
# TÍTULO
# =========================
st.title("📊 Valuation com ESG e Intervalo de Confiança")

# =========================
# INPUTS
# =========================
st.subheader("Entradas")

fcff = st.number_input("FCFF₀", value=1000.0)

if "iesg" not in st.session_state:
    st.warning("Preencha as páginas ESG primeiro.")
    st.stop()

esg_score = st.session_state.iesg
st.metric("Score ESG", f"{esg_score*100:.1f}")

# =========================
# PARÂMETROS
# =========================
with st.expander("Parâmetros do Modelo"):

    wacc = st.number_input("WACC", value=DEFAULTS["wacc"])
    g_base = st.number_input("Crescimento base", value=DEFAULTS["g_base"])
    g_terminal = st.number_input("Crescimento terminal", value=DEFAULTS["g_terminal"])
    n = st.slider("Períodos", 1, 20, 5)

# =========================
# VALIDAÇÃO
# =========================
if wacc <= g_terminal:
    st.error("WACC deve ser maior que o crescimento terminal")
    st.stop()

# =========================
# CENÁRIOS DE THETA (IC)
# =========================
thetas = {
    "Pessimista (IC inf.)": THETA_LOW,
    "Médio (estimado)": THETA_MEAN,
    "Otimista (IC sup.)": THETA_HIGH
}

valores = {}
projecoes = {}

for nome, theta in thetas.items():
    g_total, g_esg = estimate_growth(esg_score, g_base, theta)
    fcff_proj = project_fcff(fcff, g_total, n)
    valor = fcff_valuation(fcff_proj, wacc, g_terminal)

    valores[nome] = valor
    projecoes[nome] = fcff_proj

# =========================
# RESULTADOS
# =========================
st.markdown("## 💰 Valor da Cooperativa (com IC)")

col1, col2, col3 = st.columns(3)

col1.metric("Pessimista", f"{valores['Pessimista (IC inf.)']:,.2f}")
col2.metric("Médio", f"{valores['Médio (estimado)']:,.2f}")
col3.metric("Otimista", f"{valores['Otimista (IC sup.)']:,.2f}")

# =========================
# GRÁFICOS
# =========================
st.subheader("Comparação dos Cenários (IC do ESG)")
st.bar_chart(valores)

st.subheader("Projeção do FCFF")
st.line_chart(projecoes)

# =========================
# DETALHES
# =========================
st.subheader("Parâmetros")

st.write(f"WACC: {wacc:.7%}")
st.write(f"θ (médio): {THETA_MEAN:.7f}")
st.write(f"IC 95%: [{THETA_LOW:.7f} ; {THETA_HIGH:.7f}]")

g_total, g_esg = estimate_growth(esg_score, g_base, THETA_MEAN)

st.write(f"Crescimento total: {g_total:.7%}")
st.write(f"Parcela ESG: {g_esg:.7%}")
st.write(f"Crescimento base: {g_base:.7%}")
st.write(f"Crescimento terminal: {g_terminal:.7%}")

# =========================
# EQUAÇÕES
# =========================
st.markdown("---")
st.subheader("Equações do Modelo")

st.markdown("### Crescimento com ESG")
st.latex(r"g = g_0 + \theta \cdot \ln(1 + ESG)")

st.markdown("### Projeção do FCFF")
st.latex(r"FCFF_t = FCFF_0 (1 + g)^t")

st.markdown("### Valuation")
st.latex(r"V = \sum_{t=1}^{n} \frac{FCFF_t}{(1 + WACC)^t} + \frac{FCFF_{n+1}}{WACC - g}")
