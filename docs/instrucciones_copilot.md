##  Instrucciones para Copilot

###  Objetivo

El objetivo de las instrucciones es guiar a GitHub Copilot en la generación de código Python y componentes visuales de la aplicación **Streamlit Dashboard Interactivo de Ventas**, basada en los archivos de datos proporcionados.

---

###  Contexto del Proyecto

El proyecto pertenece al curso **Fundamentos de Inteligencia Artificial (Guayerd & IBM)** – *Sprint 1*
Se trabaja con un conjunto de datos en formato Excel (`clientes.xlsx`, `productos.xlsx`, `ventas.xlsx`, `detalle_ventas.xlsx`) para construir un **visor interactivo** que permita explorar la información de ventas mediante filtros y gráficos, sin análisis predictivo.

---

###  Instrucciones dadas a Copilot

1. **Estructura base del programa:**

   * Crear una aplicación en **Streamlit** con un diseño limpio y moderno.
   * Incluir título, autor y descripción del proyecto.
   * Cargar los cuatro archivos Excel con `pandas`.
   * Combinar los datos mediante `merge` para generar un único DataFrame.
   * Incluir filtros en la barra lateral por cliente, producto, ciudad y categoría.

2. **Visualización de datos:**

   * Mostrar **KPIs principales**: Total de ventas, cantidad de ventas, clientes únicos.
   * Crear gráficos:

     * Ventas por categoría (barras).
     * Tendencia mensual (línea).
     * Top productos vendidos (barras horizontales).
   * Mostrar una tabla con los datos filtrados.

3. **Interactividad:**

   * Actualizar los gráficos y KPIs en tiempo real según los filtros.
   * Asegurar que no haya errores de ejecución al cambiar filtros.

---

###  Sugerencias de Copilot — *Aceptadas*

* Propuesta de usar `st.tabs()` para organizar las secciones del dashboard.
* Recomendación de usar `plotly.express` para gráficos más interactivos.
* Sugerencia de mostrar KPIs con íconos y formato monetario usando `st.metric`.
* Implementación del cálculo automático de métricas (`total_ventas`, `cantidad_ventas`, `clientes_únicos`).

---

###  Sugerencias de Copilot — *Descartadas*

* Uso de librerías adicionales como `matplotlib` o `altair` (para mantener simple el entorno Streamlit Cloud).
* Generar análisis predictivo (no requerido en este sprint).
* Crear un modelo de recomendación de productos (fuera del alcance de la entrega).

---

###  Buenas prácticas aplicadas

* Se modularizó el código con funciones para lectura y combinación de datos.
* Se agregaron etiquetas y colores consistentes para mejorar la comprensión visual.
* Se incluyeron comentarios descriptivos en cada sección para facilitar el mantenimiento del código.

---

###  Resultado Final

El resultado es una aplicación **interactiva, estable y clara**, que permite visualizar información organizada y filtrable sobre ventas, cumpliendo con los requerimientos del **Sprint 1**.

---

