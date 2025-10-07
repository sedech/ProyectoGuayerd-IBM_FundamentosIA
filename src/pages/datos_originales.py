import streamlit as st
import pandas as pd
from src.data_loader import cargar_datos_originales

def mostrar_pagina_datos_originales():
    """Muestra la página de datos originales"""
    st.markdown("---")
    st.header("📂 Datos Originales - Datasets Crudos")
    st.info("Esta sección muestra los datasets originales sin procesar.")
    
    # Cargar datos
    datos = cargar_datos_originales()
    
    # Tabs para cada dataset
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Detalle Ventas", "🧾 Ventas", "📦 Productos", "👥 Clientes"
    ])
    
    with tab1:
        st.subheader("Detalle de Ventas")
        st.dataframe(datos["detalle_ventas"], use_container_width=True)
        st.metric("Total Registros", len(datos["detalle_ventas"]))
        
    with tab2:
        st.subheader("Ventas")
        st.dataframe(datos["ventas"], use_container_width=True)
        st.metric("Total Registros", len(datos["ventas"]))
        
    with tab3:
        st.subheader("Productos")
        st.dataframe(datos["productos"], use_container_width=True)
        st.metric("Total Registros", len(datos["productos"]))
        
    with tab4:
        st.subheader("Clientes")
        st.dataframe(datos["clientes"], use_container_width=True)
        st.metric("Total Registros", len(datos["clientes"]))