import pandas as pd

def cargar_datos_originales():
    """Carga los datasets originales sin procesar"""
    detalle = pd.read_excel("datasets/detalle_ventas.xlsx")
    ventas = pd.read_excel("datasets/ventas.xlsx")
    productos = pd.read_excel("datasets/productos.xlsx")
    clientes = pd.read_excel("datasets/clientes.xlsx")
    
    return {
        "detalle_ventas": detalle,
        "ventas": ventas,
        "productos": productos,
        "clientes": clientes
    }

def cargar_datos_procesados():
    """Carga y procesa los datos para el dashboard"""
    # Cargar archivos
    detalle = pd.read_excel("datasets/detalle_ventas.xlsx")
    ventas = pd.read_excel("datasets/ventas.xlsx")[["id_venta", "id_cliente", "fecha", "medio_pago"]]
    productos = pd.read_excel("datasets/productos.xlsx")[["id_producto", "nombre_producto", "categoria", "precio_unitario"]]
    clientes = pd.read_excel("datasets/clientes.xlsx")[["id_cliente", "nombre_cliente", "ciudad", "fecha_alta"]]

    # Merge de datos
    df = detalle.merge(productos, on="id_producto", how="left")
    df = df.merge(ventas, on="id_venta", how="left")
    df = df.merge(clientes, on="id_cliente", how="left")

    # Calcular importe
    df["importe"] = df["cantidad"] * df["precio_unitario_y"]

    # Conversión de fechas
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    
    # Limpieza de nombres
    df = df.rename(columns={
        "nombre_producto_x": "nombre_producto_venta",
        "nombre_producto_y": "nombre_producto_catalogo",
        "precio_unitario_x": "precio_venta",
        "precio_unitario_y": "precio_catalogo"
    })

    return df