# Proyecto Guayerd & IBM - Fundamentos en Inteligencia Artificial

##  Tema
**Visualizador interactivo de datos de ventas.**

Este proyecto permite integrar y visualizar información de diferentes fuentes relacionadas con ventas, productos y clientes, a través de una interfaz moderna desarrollada con **Streamlit**.

---

##  Problema
En muchas empresas, los datos de ventas se encuentran dispersos en distintos archivos (clientes, productos, ventas y detalle de ventas).  
Esto dificulta analizar la información, generar reportes rápidos y tomar decisiones informadas.

---

##  Solución
Desarrollar un **visor interactivo** que consolide todos los datos y permita:
- Visualizar los registros unificados en una sola vista.
- Filtrar por ciudad o categoría de producto.
- Generar gráficos automáticos para entender la evolución y el comportamiento de ventas.

El visor fue desarrollado en **Python + Streamlit**, con un enfoque en **organización y visualización**, sin aplicar aún algoritmos de IA (que se agregarán en futuros sprints).

---

## 📊 Dataset de referencia

Se utilizan cuatro archivos Excel como fuentes de datos:

| Archivo | Descripción | Clave |
|----------|--------------|-------|
| `clientes.xlsx` | Información básica de los clientes: nombre, email, ciudad y fecha de alta. | `id_cliente` |
| `productos.xlsx` | Catálogo de productos con su categoría y precio unitario. | `id_producto` |
| `ventas.xlsx` | Ventas realizadas con fecha, cliente y medio de pago. | `id_venta` |
| `detalle_ventas.xlsx` | Detalle de cada venta: producto, cantidad y precios. | `id_venta`, `id_producto` |

**Escala:** Cada fila representa una transacción individual.  
**Tipos de datos:** cadenas de texto, numéricos y fechas.

---

##  Pasos del desarrollo

1. Cargar los cuatro archivos Excel con `pandas`.
2. Realizar uniones (`merge`) para obtener una vista consolidada.
3. Calcular métricas (importe total = cantidad × precio unitario).
4. Crear un panel lateral para filtros interactivos (Streamlit Sidebar).
5. Visualizar la información en:
   - Tablas dinámicas.
   - Gráficos con **Plotly Express**.
6. Organizar el contenido en pestañas temáticas.

