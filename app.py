import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Ventas - Fundamentos IA", 
    layout="wide",
    page_icon="📊"
)

# Importar componentes
from src.components import mostrar_header, mostrar_menu_principal

# Mostrar header y menú
mostrar_header()
mostrar_menu_principal()

# Navegación entre páginas
if st.session_state.get('menu_seleccionado') == 'datos_originales':
    from src.pages.datos_originales import mostrar_pagina_datos_originales
    mostrar_pagina_datos_originales()
    
elif st.session_state.get('menu_seleccionado') == 'dashboard_filtros':
    from src.pages.dashboard_filtros import mostrar_pagina_dashboard
    mostrar_pagina_dashboard()

else:
    # Página de inicio
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
    
    st.info("👆 **Selecciona una opción del menú superior para comenzar**")