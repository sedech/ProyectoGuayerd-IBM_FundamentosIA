import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import cargar_datos_procesados
from src.utils import configurar_filtros_sidebar, aplicar_filtros_fecha
from src.components import mostrar_kpis


def detectar_outliers_iqr(serie: pd.Series):
    """Devuelve máscara de outliers y límites inferior/superior usando IQR."""
    q1, q3 = serie.quantile([0.25, 0.75])
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    mask = (serie < lim_inf) | (serie > lim_sup)
    return mask, lim_inf, lim_sup


def mostrar_pagina_eda():
    st.markdown("---")
    st.header("🧪 2° Sprint – Análisis Exploratorio de Datos (EDA)")

    # ================= CARGA DE DATOS =================
    df = cargar_datos_procesados()

    st.markdown(
        f"Dataset procesado: **{df.shape[0]} filas** • **{df.shape[1]} columnas**"
    )

    # ================= FILTROS (IGUAL QUE DASHBOARD) =================
    st.sidebar.markdown("## 🎛️ Filtros EDA (Sprint 2)")
    rango_fechas, ciudades, clientes, categorias, productos = configurar_filtros_sidebar(df)

    df_fecha = aplicar_filtros_fecha(df, rango_fechas)
    df_filtrado = df_fecha[
        (df_fecha["ciudad"].isin(ciudades)) &
        (df_fecha["nombre_cliente"].isin(clientes)) &
        (df_fecha["categoria"].isin(categorias)) &
        (df_fecha["nombre_producto_venta"].isin(productos))
    ]

    st.markdown(
        f"Datos filtrados: **{df_filtrado.shape[0]} filas** después de aplicar filtros de fecha, ciudad, cliente, categoría y producto."
    )

    # ================= KPIs SOBRE DATOS FILTRADOS =================
    st.markdown("### 📌 KPIs del subconjunto filtrado")
    mostrar_kpis(df_filtrado)

    # Columnas numéricas principales
    columnas_numericas = [c for c in ["cantidad", "precio_catalogo", "importe"] if c in df_filtrado.columns]

    # ================= TABS: DASHBOARD + EDA =================
    tab1, tab2, tab3 = st.tabs([
        "📊 Resumen estadístico",
        "📈 Distribuciones & Outliers",
        "🔗 Correlaciones & Relaciones"
    ])

    # ---------- TAB 1: Estadísticas ----------
    with tab1:
        st.subheader("📊 Estadísticas descriptivas básicas")

        if columnas_numericas:
            st.dataframe(df_filtrado[columnas_numericas].describe().round(2), use_container_width=True)
        else:
            st.warning("No se encontraron columnas numéricas para calcular estadísticas.")

        st.markdown("#### Promedios por categoría")
        if "categoria" in df_filtrado.columns and "importe" in df_filtrado.columns:
            resumen_cat = (
                df_filtrado
                .groupby("categoria")[["cantidad", "importe"]]
                .mean()
                .round(2)
                .reset_index()
            )
            st.dataframe(resumen_cat, use_container_width=True)
        else:
            st.info("No se pudo calcular el resumen por categoría.")

    # ---------- TAB 2: Distribuciones & Outliers ----------
    with tab2:
        st.subheader("📈 Distribución de variables")

        c1, c2, c3 = st.columns(3)
        if "cantidad" in df_filtrado.columns:
            with c1:
                st.plotly_chart(
                    px.histogram(df_filtrado, x="cantidad", nbins=30, title="Histograma - Cantidad"),
                    use_container_width=True
                )
        if "precio_catalogo" in df_filtrado.columns:
            with c2:
                st.plotly_chart(
                    px.histogram(df_filtrado, x="precio_catalogo", nbins=30, title="Histograma - Precio catálogo"),
                    use_container_width=True
                )
        if "importe" in df_filtrado.columns:
            with c3:
                st.plotly_chart(
                    px.histogram(df_filtrado, x="importe", nbins=30, title="Histograma - Importe"),
                    use_container_width=True
                )

        st.markdown("#### Boxplot de importe por categoría")
        if {"categoria", "importe"}.issubset(df_filtrado.columns):
            st.plotly_chart(
                px.box(df_filtrado, x="categoria", y="importe", title="Importe por categoría"),
                use_container_width=True
            )

        st.markdown("#### Detección de outliers (IQR) en Importe")
        if "importe" in df_filtrado.columns:
            mask_out, li, ls = detectar_outliers_iqr(df_filtrado["importe"])
            outliers = df_filtrado[mask_out].copy()
            st.write(
                f"Rango IQR estimado: **{li:,.2f}** a **{ls:,.2f}**  |  "
                f"Outliers detectados: **{outliers.shape[0]}** registros"
            )
            st.dataframe(
                outliers[[
                    "fecha", "nombre_cliente", "nombre_producto_venta",
                    "categoria", "cantidad", "precio_catalogo", "importe"
                ]],
                use_container_width=True
            )
        else:
            st.info("No se encontró la columna 'importe' para detectar outliers.")

    # ---------- TAB 3: Correlaciones & Relaciones ----------
    with tab3:
        st.subheader("🔗 Correlaciones y relaciones entre variables")

        if len(columnas_numericas) >= 2:
            corr = df_filtrado[columnas_numericas].corr().round(3)
            st.dataframe(corr, use_container_width=True)
            st.plotly_chart(
                px.imshow(corr, text_auto=True, title="Matriz de correlación (subconjunto filtrado)"),
                use_container_width=True
            )
        else:
            st.info("No hay suficientes variables numéricas para calcular una matriz de correlación.")

        st.markdown("#### Dispersión: cantidad vs importe por categoría")
        if {"cantidad", "importe"}.issubset(df_filtrado.columns):
            st.plotly_chart(
                px.scatter(
                    df_filtrado,
                    x="cantidad",
                    y="importe",
                    color="categoria",
                    hover_data=["nombre_producto_venta", "nombre_cliente"],
                    title="Relación entre cantidad e importe por categoría (datos filtrados)"
                ),
                use_container_width=True
            )

    # ================= DESCARGA CSV LIMPIO =================
    st.markdown("### 💾 Descargar base filtrada para análisis externo (.csv)")
    csv_bytes = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar ventas_limpias_filtradas.csv",
        data=csv_bytes,
        file_name="ventas_limpias_filtradas.csv",
        mime="text/csv",
        use_container_width=True
    )

    # ================= INTERPRETACIÓN =================
    st.markdown("---")
    st.markdown("### 🧩 Interpretación orientada al problema (resumen)")
    st.markdown(
        """
El análisis exploratorio permitió obtener una visión clara del comportamiento de ventas de la tienda Aurelion. 
A partir del subconjunto filtrado (ciudad, cliente, categoría y fechas seleccionadas), se identificaron los siguientes hallazgos clave:

✔ 1. Patrones de venta claros y consistentes

La relación positiva entre cantidad e importe confirma que los productos más vendidos en volumen son también los que más contribuyen a la facturación total. El negocio depende tanto de la cantidad como del precio catálogo.

✔ 2. Dos segmentos de compra muy definidos

Los datos muestran dos comportamientos distintos:

Compras minoristas (1–3 unidades por ticket) → mayoría de las ventas.

Compras especiales / mayoristas (5 unidades, importes > $20.000) → explican los valores máximos y la dispersión.

Esto es clave para diseñar estrategias en Sprint 4 (Power BI) o campañas de marketing.

✔ 3. Outliers relevantes, no errores

Los outliers detectados con IQR corresponden a transacciones legítimas de alto importe, no a errores de carga. 
Representan una oportunidad para segmentar clientes "alto valor".

✔ 4. Diferencias entre categorías

Limpieza genera un importe promedio más alto que Alimentos.

Alimentos tiene mayor volumen y rotación.

Esta diferencia sugiere que Limpieza es el driver de ingresos y Alimentos el driver de tráfico.

✔ 5. Correlaciones útiles para construir el modelo del Sprint 3

La matriz de correlación muestra relaciones estables y sin multicolinealidad problemática:

cantidad → importe: correlación moderada (0.60)

precio_catalogo → importe: correlación moderada-alta (0.67)

cantidad ↔ precio_catalogo: relación nula

Esto indica que el modelo predictivo (Sprint 3) podrá estimar el importe con buena estabilidad y sin variables redundantes.

✔ 6. Calidad del dato

Los datos no presentan valores faltantes significativos, la estructura es coherente y 
las distribuciones corresponden a un negocio real minorista.
Solo se recomienda revisar las transacciones muy altas para clasificar correctamente compras corporativas.

En conclusión, el EDA permitió comprender la estructura del negocio, validar la limpieza del dataset y 
detectar patrones esenciales para el siguiente Sprint. Estos hallazgos son fundamentales para diseñar un modelo predictivo confiable 
y una estrategia de negocio basada en datos.
        """
    )
