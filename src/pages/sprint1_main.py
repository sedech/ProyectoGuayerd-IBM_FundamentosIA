import streamlit as st
from src.components import mostrar_menu_principal
from src.pages.datos_originales import mostrar_pagina_datos_originales
from src.pages.dashboard_filtros import mostrar_pagina_dashboard


def mostrar_pagina_sprint1():
    """Página completa del 1° Sprint: menú + datos originales + dashboard."""
    st.subheader("🟢 1° Sprint – Demo de Inteligencia Artificial (Visor Interactivo)")

    # Menú original de Sprint 1 (Datos Originales / Dashboard con Filtros)
    mostrar_menu_principal()

    if st.session_state.get('menu_seleccionado') == 'datos_originales':
        mostrar_pagina_datos_originales()
        
    elif st.session_state.get('menu_seleccionado') == 'dashboard_filtros':
        mostrar_pagina_dashboard()

    else:
        # Página de inicio del Sprint 1
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📁 Datos Originales")
            st.markdown("""
            - Visualización de datasets crudos  
            - Sin procesamiento ni filtros  
            - Ideal para revisión de datos fuente
            """)
        
        with col2:
            st.markdown("### 🔍 Dashboard con Filtros")
            st.markdown("""
            - Visualización interactiva  
            - Filtros avanzados  
            - Gráficos y KPIs dinámicos
            """)
        
        st.info("👆 **Selecciona una opción del menú superior para comenzar (Sprint 1)**")
