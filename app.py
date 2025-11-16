import streamlit as st
from src.components import mostrar_header

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Interactivo de Tienda Aurelion",
    layout="wide",
    page_icon="📊"
)

# Estado inicial: ningún sprint seleccionado
if "sprint_seleccionado" not in st.session_state:
    st.session_state["sprint_seleccionado"] = None

# Header
mostrar_header()

# --------- Roadmap de Sprints / Demos ----------
st.markdown("### 🧭 Roadmap de Sprints / Demos")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🤖 1° Sprint Inteligencia Artificial", use_container_width=True):
        st.session_state["sprint_seleccionado"] = "sprint1"

with col2:
    if st.button("🐍 2° Sprint Python (EDA)", use_container_width=True):
        st.session_state["sprint_seleccionado"] = "sprint2"

with col3:
    if st.button("🚀 3° Sprint Machine Learning", use_container_width=True):
        st.session_state["sprint_seleccionado"] = "sprint3"

with col4:
    if st.button("📊 4° Sprint Power BI", use_container_width=True):
        st.session_state["sprint_seleccionado"] = "sprint4"

st.markdown("---")

sprint = st.session_state["sprint_seleccionado"]

# ===================== HOME (sin sprint seleccionado) =====================
if sprint is None:
    st.info("👆 Selecciona uno de los **Sprints** de arriba para comenzar.")

# ===================== 1° SPRINT =====================
elif sprint == "sprint1":
    from src.pages.sprint1_main import mostrar_pagina_sprint1
    mostrar_pagina_sprint1()

# ===================== 2° SPRINT =====================
elif sprint == "sprint2":
    from src.pages.eda_sprint2 import mostrar_pagina_eda
    mostrar_pagina_eda()

# ===================== 3° SPRINT =====================
elif sprint == "sprint3":
    from src.pages.sprint3_ml import mostrar_pagina_sprint3
    mostrar_pagina_sprint3()

# ===================== 4° SPRINT =====================
elif sprint == "sprint4":
    from src.pages.sprint4_powerbi import mostrar_pagina_sprint4
    mostrar_pagina_sprint4()
