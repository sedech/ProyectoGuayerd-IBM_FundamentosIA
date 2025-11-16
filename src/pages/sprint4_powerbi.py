import streamlit as st

def mostrar_pagina_sprint4():
    st.subheader("🟣 4° Sprint – Power BI")
    st.markdown("""
Interpretación Ejecutiva del Sprint 4 
El dashboard ejecutivo integra todo el proceso del proyecto: los datos originales, el análisis exploratorio y las predicciones del modelo.

En la primera página se presenta una visión global del rendimiento del negocio, mostrando los KPIs clave, los productos que más facturan y las ciudades más relevantes en ventas.

El análisis exploratorio permite entender la estructura de los datos, la distribución de las variables, la presencia de outliers y la relación entre cantidad y precio con el importe. Esto aporta una visión profunda del comportamiento del negocio y habilita la detección temprana de anomalías.

La sección del modelo predictivo muestra que el algoritmo logra un R² de 0.992, lo que indica una capacidad predictiva muy alta. 
El MAE de $193 y el RMSE de $367 confirman que el modelo es preciso y estable. La comparación entre importe real y predicho demuestra que la línea de ajuste sigue correctamente el patrón de ventas.

Finalmente, las recomendaciones ejecutivas consolidan los hallazgos:

Las ventas están fuertemente influenciadas por la cantidad y el precio catálogo.

La categoría “Alimentos” y ciertas ciudades impulsan la mayor parte de la facturación.

Existen ventas atípicas que ameritan revisión para mejorar la calidad del dato.

El modelo predictivo puede utilizarse para simular escenarios y apoyar decisiones comerciales.
    """)

    st.info("💾  Power BI.")
