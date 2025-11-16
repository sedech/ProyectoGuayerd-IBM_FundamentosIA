import streamlit as st
import pandas as pd

def configurar_filtros_sidebar(df):
    """Configura y retorna los filtros del sidebar"""
    st.sidebar.header("🎛️ Panel de Control")
    
    # Filtro de fecha
    fecha_min = df["fecha"].min().date()
    fecha_max = df["fecha"].max().date()
    
    rango_fechas = st.sidebar.date_input(
        "Seleccionar período:",
        value=(fecha_min, fecha_max)
    )
    
    # Filtros principales
    ciudades = st.sidebar.multiselect(
        "🌍 Ciudad", 
        options=sorted(df["ciudad"].dropna().unique()), 
        default=df["ciudad"].dropna().unique()
    )
    
    clientes = st.sidebar.multiselect(
        "👥 Cliente", 
        options=sorted(df["nombre_cliente"].dropna().unique()),
        default=df["nombre_cliente"].dropna().unique()
    )
    
    categorias = st.sidebar.multiselect(
        "📦 Categoría", 
        options=sorted(df["categoria"].dropna().unique()),
        default=df["categoria"].dropna().unique()
    )
    
    productos = st.sidebar.multiselect(
        "🏷️ Producto", 
        options=sorted(df["nombre_producto_venta"].dropna().unique()),
        default=df["nombre_producto_venta"].dropna().unique()
    )
    
    # Botón para resetear
    if st.sidebar.button("🔄 Resetear Filtros", use_container_width=True):
        # para versiones anteriores de Streamlit
        st.experimental_rerun()
    
    return rango_fechas, ciudades, clientes, categorias, productos

def aplicar_filtros_fecha(df, rango_fechas):
    """Aplica filtro de fechas al DataFrame"""
    if len(rango_fechas) == 2:
        mask = (df['fecha'].dt.date >= rango_fechas[0]) & (df['fecha'].dt.date <= rango_fechas[1])
        return df[mask]
    return df
