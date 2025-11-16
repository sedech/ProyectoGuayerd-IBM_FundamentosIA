import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from src.data_loader import cargar_datos_procesados

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ---------- Entrenamiento del modelo (cacheado) ----------

@st.cache_resource
def entrenar_modelo_importe():
    """Entrena un modelo de ML para predecir el importe de venta."""
    df = cargar_datos_procesados().copy()

    # Definimos la variable objetivo
    if "importe" not in df.columns:
        raise ValueError("No se encontró la columna 'importe' en el DataFrame procesado.")

    y = df["importe"]

    # Definimos features numéricas y categóricas
    columnas_numericas = [c for c in ["cantidad", "precio_catalogo"] if c in df.columns]
    columnas_categoricas = [c for c in ["categoria", "ciudad", "medio_pago", "mes"] if c in df.columns]

    X = df[columnas_numericas + columnas_categoricas]

    # Eliminamos filas con nulos en X o y
    mask_valid = X.notna().all(axis=1) & y.notna()
    X = X[mask_valid]
    y = y[mask_valid]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Preprocesamiento
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", columnas_numericas),
            ("cat", OneHotEncoder(handle_unknown="ignore"), columnas_categoricas),
        ]
    )

    # Modelo
    modelo = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", modelo),
        ]
    )

    # Entrenamiento
    pipeline.fit(X_train, y_train)

    # Predicciones en test
    y_pred = pipeline.predict(X_test)

    # Métricas
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)           # RMSE sin usar el parámetro squared
    r2 = r2_score(y_test, y_pred)

    metricas = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
    }

    # Guardamos partes útiles
    info = {
        "pipeline": pipeline,
        "X_test": X_test,
        "y_test": y_test,
        "y_pred": y_pred,
        "columnas_numericas": columnas_numericas,
        "columnas_categoricas": columnas_categoricas,
    }

    return info, metricas


@st.cache_data
def cargar_datos_para_simulador():
    """Carga datos procesados para poblar selects del simulador."""
    df = cargar_datos_procesados().copy()
    return df


# ---------- Página Sprint 3 ----------

def mostrar_pagina_sprint3():
    st.subheader("🔵 3° Sprint – Modelo de Machine Learning (Predicción de Importe)")

    st.markdown("""
En este sprint se entrena un modelo de **Machine Learning** para predecir el **importe de una venta**
a partir de variables como cantidad, precio, categoría, ciudad y medio de pago.
    """)

    with st.spinner("Entrenando modelo de Random Forest..."):
        info_modelo, metricas = entrenar_modelo_importe()

    pipeline = info_modelo["pipeline"]
    X_test = info_modelo["X_test"]
    y_test = info_modelo["y_test"]
    y_pred = info_modelo["y_pred"]

    # ---------- Métricas ----------
    st.markdown("### 📏 Métricas del modelo (con conjunto de test)")

    col1, col2, col3 = st.columns(3)
    col1.metric("MAE", f"${metricas['MAE']:,.0f}")
    col2.metric("RMSE", f"${metricas['RMSE']:,.0f}")
    col3.metric("R²", f"{metricas['R2']:.3f}")

    st.markdown("""
- **MAE**: error promedio absoluto en la predicción del importe.  
- **RMSE**: penaliza más los errores grandes.  
- **R²**: qué porcentaje de la variabilidad del importe explica el modelo.
    """)

    # ---------- Gráfico Real vs Predicho ----------
    st.markdown("### 📈 Comparación Importe Real vs Predicho")

    df_eval = pd.DataFrame(
        {
            "importe_real": y_test,
            "importe_predicho": y_pred,
        }
    ).reset_index(drop=True)

    fig_scatter = px.scatter(
        df_eval,
        x="importe_real",
        y="importe_predicho",
        title="Importe real vs importe predicho",
        labels={"importe_real": "Importe real", "importe_predicho": "Importe predicho"},
    )

    # Línea ideal y = x para comparar real vs predicho
    min_val = float(df_eval[["importe_real", "importe_predicho"]].min().min())
    max_val = float(df_eval[["importe_real", "importe_predicho"]].max().max())

    fig_scatter.add_shape(
        type="line",
        x0=min_val,
        y0=min_val,
        x1=max_val,
        y1=max_val,
        line=dict(dash="dash")
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

    # ---------- Simulador interactivo ----------
    st.markdown("### 🧮 Simulador de predicción de importe")

    df_sim = cargar_datos_para_simulador()

    columnas_numericas = info_modelo["columnas_numericas"]
    columnas_categoricas = info_modelo["columnas_categoricas"]

    col_izq, col_der = st.columns(2)

    with col_izq:
        st.markdown("#### Parámetros de la venta")

        # Valores por defecto tomados del dataset
        cantidad_min = int(df_sim["cantidad"].min()) if "cantidad" in df_sim.columns else 1
        cantidad_max = int(df_sim["cantidad"].max()) if "cantidad" in df_sim.columns else 100
        cantidad_default = int(df_sim["cantidad"].median()) if "cantidad" in df_sim.columns else 1

        precio_min = float(df_sim["precio_catalogo"].min()) if "precio_catalogo" in df_sim.columns else 100.0
        precio_max = float(df_sim["precio_catalogo"].max()) if "precio_catalogo" in df_sim.columns else 10000.0
        precio_default = float(df_sim["precio_catalogo"].median()) if "precio_catalogo" in df_sim.columns else 1000.0

        cantidad = st.slider(
            "Cantidad",
            min_value=cantidad_min,
            max_value=cantidad_max,
            value=cantidad_default,
        )

        precio_catalogo = st.slider(
            "Precio catálogo",
            min_value=float(round(precio_min, 2)),
            max_value=float(round(precio_max, 2)),
            value=float(round(precio_default, 2)),
            step=1.0,
        )

        # Selects para variables categóricas (si existen)
        categoria = None
        ciudad = None
        medio_pago = None
        mes = None

        if "categoria" in df_sim.columns:
            categoria = st.selectbox(
                "Categoría",
                options=sorted(df_sim["categoria"].dropna().unique())
            )

        if "ciudad" in df_sim.columns:
            ciudad = st.selectbox(
                "Ciudad",
                options=sorted(df_sim["ciudad"].dropna().unique())
            )

        if "medio_pago" in df_sim.columns:
            medio_pago = st.selectbox(
                "Medio de pago",
                options=sorted(df_sim["medio_pago"].dropna().unique())
            )

        if "mes" in df_sim.columns:
            mes = st.selectbox(
                "Mes (período de venta)",
                options=sorted(df_sim["mes"].dropna().unique())
            )

    with col_der:
        st.markdown("#### Resultado de la predicción")

        # Armamos un DataFrame con una sola fila para predecir
        data_input = {}

        if "cantidad" in columnas_numericas:
            data_input["cantidad"] = [cantidad]
        if "precio_catalogo" in columnas_numericas:
            data_input["precio_catalogo"] = [precio_catalogo]

        if "categoria" in columnas_categoricas and categoria is not None:
            data_input["categoria"] = [categoria]
        if "ciudad" in columnas_categoricas and ciudad is not None:
            data_input["ciudad"] = [ciudad]
        if "medio_pago" in columnas_categoricas and medio_pago is not None:
            data_input["medio_pago"] = [medio_pago]
        if "mes" in columnas_categoricas and mes is not None:
            data_input["mes"] = [mes]

        if data_input:
            df_input = pd.DataFrame(data_input)

            importe_predicho = pipeline.predict(df_input)[0]

            st.metric(
                "💰 Importe predicho",
                f"${importe_predicho:,.0f}"
            )

            st.markdown("""
Este importe es una **estimación** basada en el comportamiento histórico de ventas,
teniendo en cuenta la combinación de cantidad, precio, categoría, ciudad y medio de pago.
            """)
        else:
            st.warning("No hay suficientes variables para generar la predicción.")
    
    st.markdown("---")
    st.markdown("""
### 🧩 Interpretación orientada al negocio

El modelo logra predecir el importe de una venta con alta precisión.
Las métricas muestran:

MAE bajo ($193): el error promedio es pequeño.

RMSE moderado ($367): no hay errores grandes.

R² = 0.992: el modelo explica casi toda la variabilidad del importe.

➡️ En conjunto, indican que el modelo captura correctamente la relación entre cantidad, precio y demás variables.

📊 Interpretación del gráfico Real vs Predicho

Los puntos siguen la línea diagonal → el modelo predice valores muy cercanos a los reales.

No se observan patrones de sobrepredicción o subpredicción.

➡️ Esto confirma visualmente que el modelo generaliza bien y no está fallando en rangos extremos del importe.

🧮 Interpretación del simulador

El simulador permite probar diferentes combinaciones de:

cantidad

precio catálogo

categoría

ciudad

medio de pago

mes

➡️ El importe predicho cambia de forma coherente: si sube cantidad o precio, sube el importe, 
                lo cual valida que el modelo aprendió correctamente su comportamiento.

📌 Resumen final

El modelo del Sprint 3 es preciso, estable y útil para estimar ventas.
El simulador convierte el modelo en una herramienta práctica para evaluar escenarios comerciales y hacer estimaciones rápidas.
    """)
