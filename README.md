# 🧠 Proyecto Guayerd & IBM – Fundamentos en IA

## 📊 Aplicación Interactiva de Tienda Aurelion

### 🏆 Proyecto Completo – Sprint 1 • Sprint 2 • Sprint 3 • Sprint 4

---

# 🧩 Descripción General del Proyecto

Este proyecto forma parte del programa **Fundamentos de Inteligencia Artificial (Guayerd & IBM)**.
A lo largo de **4 sprints**, se construye una solución completa de análisis de datos:

1. **Dashboard interactivo con Streamlit**
2. **Análisis Exploratorio de Datos (EDA)**
3. **Modelo de Machine Learning**
4. **Dashboard ejecutivo en Power BI**

El objetivo es transformar datos de ventas de la tienda *Aurelion* en una herramienta integral de inteligencia de negocios, desde la visualización inicial hasta la predicción y generación de insights.

---

# 🏗 Arquitectura General del Proyecto

```
ProyectoGuayerd&IBM_FundamentosIA/
│
├── app.py                     # App principal con roadmap y navegación por Sprints
│
├── datasets/                  # Datos de entrada (fuente)
│   ├── clientes.xlsx
│   ├── productos.xlsx
│   ├── ventas.xlsx
│   └── detalle_ventas.xlsx
│
├── src/
│   ├── components.py          # Componentes visuales (header, KPIs, menú)
│   ├── data_loader.py         # Lectura, combinación y preparación de datos
│   ├── utils.py               # Filtros por fecha, UI y helpers
│   └── pages/                 # Páginas separadas por Sprint
│       ├── sprint1_main.py
│       ├── datos_originales.py
│       ├── dashboard_filtros.py
│       ├── eda_sprint2.py
│       ├── sprint3_ml.py
│       └── sprint4_powerbi.py
│
├── diagramas/                 # Diagramas UML, flujo y arquitectura
│   ├── flujo_interface.png
│   ├── flujo_programa.png
│
├── docs/                      # Documentación entregable
│   ├── documentacion.md
│   └── instrucciones_copilot.md
│
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # (Este archivo)
```

---

# 🚀 Roadmap de Desarrollo (Sprints)

A continuación se detalla **todo el desarrollo del proyecto** dividido por sprint.

---

# 🟢 Sprint 1 – Dashboard Interactivo (Streamlit)

### 🎯 Objetivo

Crear un **visor interactivo** sin análisis ni IA, organizado y modular, que permita explorar los datos de ventas.

### 🔧 Funcionalidades implementadas

✔ Carga automática de los 4 archivos Excel
✔ Unificación de datos en un solo DataFrame
✔ Dashboard con:

* Filtros por fecha, ciudad, categoría, cliente y producto
* KPIs principales
* Tabla filtrada
* Top 10 productos
* Ventas por categoría
* Tendencia mensual

✔ Sección de "Datos Originales" para validar la fuente
✔ UI profesional + navegación modular

### 🧱 Componentes principales

| Archivo                | Función                                |
| ---------------------- | -------------------------------------- |
| `dashboard_filtros.py` | Dashboard completo con gráficos y KPIs |
| `datos_originales.py`  | Vista de datasets crudos               |
| `components.py`        | Header, KPIs y menú de navegación      |
| `data_loader.py`       | Carga y unión de datos                 |
| `app.py`               | Roadmap + navegación entre sprints     |

### 📸 Capturas (placeholder)

(Insertar aquí capturas del Sprint 1)

---

# 🟡 Sprint 2 – Exploración de Datos (EDA)

### 🎯 Objetivo

Realizar un análisis exploratorio profesional, con estadísticas, outliers y correlaciones, **todo basado en filtros dinámicos** como el dashboard.

### 🔧 Funcionalidades implementadas

✔ Estadísticas descriptivas automáticas
✔ Histogramas para variables numéricas
✔ Boxplot por categoría
✔ Detección de outliers usando *IQR Rule*
✔ Matriz de correlación interactiva
✔ Dispersión cantidad vs importe
✔ Exportación de CSV filtrado
✔ Interpretación analítica orientada a negocio

### 📁 Archivos involucrados

* `eda_sprint2.py`
* `data_loader.py`
* `utils.py` (filtros)

### 📊 Hallazgos típicos

* Distribuciones sesgadas (ventas minoristas)
* Outliers relevantes por combos o ventas corporativas
* Correlación positiva entre cantidad e importe
* Categorías con mejor rendimiento

### 📸 Capturas (placeholder)

(Insertar aquí capturas del EDA)

---

# 🔵 Sprint 3 – Machine Learning (Modelo Predictivo)

> ⚠️ *Esta sección se completa cuando implementes tu modelo.*
> Te dejo la estructura lista.

### 🎯 Objetivo

Construir un modelo de predicción basado en los datos procesados.

### 🔧 Requerimientos habituales

✔ Preprocesamiento
✔ Selección de features
✔ División entrenamiento/test
✔ Entrenamiento de modelo (ejemplo: Regresión Lineal)
✔ Métricas: RMSE, MAE, R²
✔ Visualización de errores
✔ Predicción integrada en Streamlit
✔ Inputs interactivos (sliders, selects, numéricos)

### 📁 Archivo a modificar

* `sprint3_ml.py`

### 📸 Capturas (placeholder)

(Se agregarán en el Sprint 3)

---

# 🟣 Sprint 4 – Dashboard Ejecutivo en Power BI

### 🎯 Objetivo

Construir un dashboard profesional en Power BI con los datos limpios del Sprint 2.

### 🔧 Requerimientos

✔ KPIs avanzados
✔ Segmentación de datos
✔ Gráficos ejecutivos
✔ Storytelling visual
✔ Análisis temporal
✔ Publicación opcional en Power BI Service

### 📁 Archivo

* `sprint4_powerbi.py` (texto explicativo + enlace opcional al reporte)

### 📸 Capturas (placeholder)

(Se agregará imagen del dashboard final)

---

# 🛠 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/ProyectoGuayerd-IBM_FundamentosIA.git
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la app

```bash
streamlit run app.py
```

La aplicación abrirá automáticamente en:
🔗 `http://localhost:8501`

---

# 📚 Documentación Técnica

### 📄 `documentacion.md`

Incluye:

* Tema del proyecto
* Problema
* Solución general
* Dataset
* Pseudocódigo del programa
* Diagrama del flujo
* Explicación del modelo (Sprint 3)
* Evidencias del desarrollo

### 📄 `instrucciones_copilot.md`

Incluye:

* Prompts utilizados con Copilot
* Sugerencias aceptadas
* Sugerencias descartadas
* Reflexión sobre la asistencia de IA

---

# 🧠 Conclusiones del Proyecto Completo

* El proyecto evoluciona desde **visualización → exploración → predicción → business intelligence**.
* Streamlit permite crear interfaces interactivas de forma simple y modular.
* El EDA reveló tendencias útiles para negocio.
* El modelo de Machine Learning (Sprint 3) permitirá anticipar eventos o comportamientos.
* Power BI complementa con una capa ejecutiva de alto impacto.

---

# 👨‍💻 Autor

**Melchisedech Belizaire**
Proyecto final – *Fundamentos de Inteligencia Artificial (Guayerd & IBM)*

---

# 📜 Licencia

MIT License – Libre para uso académico y profesional citando la autoría.

---
