import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import cargar_datos_procesados
from src.components import mostrar_kpis
from src.utils import configurar_filtros_sidebar, aplicar_filtros_fecha

def mostrar_pagina_dashboard():
    """Muestra la página del dashboard con filtros"""
    st.markdown("---")
    st.header("🔍 Dashboard Interactivo con Filtros")
    
    # Cargar datos procesados
    df = cargar_datos_procesados()
    
    # Configurar filtros en sidebar
    rango_fechas, ciudades, clientes, categorias, productos = configurar_filtros_sidebar(df)
    
    # Aplicar filtros
    df_temp = aplicar_filtros_fecha(df, rango_fechas)
    df_filtrado = df_temp[
        (df_temp["ciudad"].isin(ciudades)) &
        (df_temp["nombre_cliente"].isin(clientes)) &
        (df_temp["categoria"].isin(categorias)) &
        (df_temp["nombre_producto_venta"].isin(productos))
    ]
    
    # Mostrar KPIs
    mostrar_kpis(df_filtrado)
    
    # Tabs del dashboard
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Datos Filtrados", "📈 Ventas por Categoría", "📆 Tendencia Mensual", "🏆 Top Productos"
    ])
    
    with tab1:
        mostrar_tab_datos(df_filtrado)
    
    with tab2:
        mostrar_tab_categorias(df_filtrado)
    
    with tab3:
        mostrar_tab_tendencia(df_filtrado)
    
    with tab4:
        mostrar_tab_top_productos(df_filtrado)

def mostrar_tab_datos(df_filtrado):
    """Muestra el tab de datos filtrados"""
    st.subheader("📋 Vista de Datos Filtrados")
    
    # Estadísticas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Registros:** {len(df_filtrado):,}")
    with col2:
        st.info(f"**Productos únicos:** {df_filtrado['nombre_producto_venta'].nunique()}")
    with col3:
        st.info(f"**Período:** {df_filtrado['mes'].min()} a {df_filtrado['mes'].max()}")
    
    # Dataframe
    columnas_default = ['id_venta', 'fecha', 'nombre_cliente', 'nombre_producto_venta', 'cantidad', 'importe']
    st.dataframe(df_filtrado[columnas_default].head(1000), use_container_width=True, height=400)
    
    # Descarga
    st.download_button(
        label="📥 Descargar Datos Filtrados (CSV)",
        data=df_filtrado.to_csv(index=False).encode('utf-8'),
        file_name="ventas_filtradas.csv",
        use_container_width=True
    )

def mostrar_tab_categorias(df_filtrado):
    """Muestra el tab de categorías"""
    st.subheader("📈 Distribución de Ventas por Categoría")
    
    ventas_cat = df_filtrado.groupby("categoria")["importe"].sum().reset_index()
    
    if not ventas_cat.empty:
        fig = px.bar(
            ventas_cat, x="categoria", y="importe", color="categoria",
            title="Total de Ventas por Categoría", text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No hay datos para mostrar")

def mostrar_tab_tendencia(df_filtrado):
    """Muestra el tab de tendencia mensual"""
    st.subheader("📆 Tendencia Mensual de Ventas")
    
    ventas_mes = df_filtrado.groupby("mes")["importe"].sum().reset_index().sort_values("mes")
    
    if not ventas_mes.empty:
        fig = px.line(ventas_mes, x="mes", y="importe", markers=True, title="Evolución Mensual de Ventas")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No hay datos para mostrar")

def mostrar_tab_top_productos(df_filtrado):
    """Muestra el tab de top productos"""
    st.subheader("🏆 Top 10 Productos más Vendidos")
    
    top_prod = df_filtrado.groupby("nombre_producto_venta")["cantidad"].sum().reset_index()
    top_prod = top_prod.sort_values("cantidad", ascending=False).head(10)
    
    if not top_prod.empty:
        fig = px.bar(
            top_prod, x="nombre_producto_venta", y="cantidad", color="nombre_producto_venta",
            title="Productos más Vendidos", text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No hay datos para mostrar")