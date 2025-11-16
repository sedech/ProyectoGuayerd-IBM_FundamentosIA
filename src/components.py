import streamlit as st

def mostrar_header():
    """Muestra el header principal"""
    st.markdown("""
        <style>
        .main-header { font-size: 2.5rem; color: #1f77b4; text-align: center; margin-bottom: 1rem; }
        .sub-header { text-align: center; color: #666; margin-bottom: 2rem; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">📊 Dashboard Interactivo de Tienda Aurelion</h1>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">', unsafe_allow_html=True)
    st.markdown("**Curso:** Fundamentos de Inteligencia Artificial (Guayerd & IBM)")
    st.markdown("**Autor:** Melchisedech Belizaire")
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_menu_principal():
    """Muestra el menú principal de navegación"""
    st.markdown("### 🗂️ Selecciona una sección:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📁 **Datos Originales**", use_container_width=True):
            st.session_state.menu_seleccionado = "datos_originales"
        
    with col2:
        if st.button("🔍 **Dashboard con Filtros**", use_container_width=True):
            st.session_state.menu_seleccionado = "dashboard_filtros"

def mostrar_kpis(df_filtrado):
    """Muestra los KPIs principales"""
    total_ventas = df_filtrado["importe"].sum()
    cantidad_ventas = df_filtrado["id_venta"].nunique()
    clientes_unicos = df_filtrado["id_cliente"].nunique()
    avg_ticket = total_ventas / cantidad_ventas if cantidad_ventas > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Total Ventas", f"${total_ventas:,.0f}")
    with col2:
        st.metric("🧾 Transacciones", f"{cantidad_ventas}")
    with col3:
        st.metric("👥 Clientes Únicos", f"{clientes_unicos}")
    with col4:
        st.metric("📦 Ticket Promedio", f"${avg_ticket:,.0f}")