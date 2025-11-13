import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", page_icon="🚗", layout="wide")

# Encabezado principal
st.header("🚗 Análisis de Anuncios de Venta de Coches")

# Descripción de la aplicación
st.write("""
Esta aplicación web permite explorar un conjunto de datos de anuncios de venta de coches en Estados Unidos.
Selecciona las casillas de verificación a continuación para generar visualizaciones interactivas.
""")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar información básica del dataset
st.subheader("📊 Información del Dataset")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de Vehículos", f"{len(car_data):,}")
with col2:
    st.metric("Precio Promedio", f"${car_data['price'].mean():,.0f}")
with col3:
    st.metric("Kilometraje Promedio", f"{car_data['odometer'].mean():,.0f} km")

# Separador
st.markdown("---")

# Sección de visualizaciones
st.subheader("📈 Visualizaciones Interactivas")
st.write("Selecciona las visualizaciones que deseas ver:")

# Casilla de verificación para construir histograma del odómetro
build_histogram = st.checkbox('Construir un histograma del odómetro')

if build_histogram:
    st.write('**Histograma del kilometraje de los vehículos**')
    
    # Crear un histograma del odómetro
    fig = px.histogram(car_data, 
                       x="odometer",
                       title="Distribución del Kilometraje (Odómetro)",
                       labels={"odometer": "Kilometraje"},
                       nbins=50,
                       color_discrete_sequence=['#636EFA'])
    
    fig.update_layout(
        xaxis_title="Kilometraje",
        yaxis_title="Frecuencia",
        showlegend=False
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Estadísticas adicionales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Kilometraje Mínimo", f"{car_data['odometer'].min():,.0f} km")
    with col2:
        st.metric("Kilometraje Máximo", f"{car_data['odometer'].max():,.0f} km")
    with col3:
        st.metric("Kilometraje Promedio", f"{car_data['odometer'].mean():,.0f} km")

# Casilla de verificación para construir gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('**Gráfico de dispersión: Relación entre kilometraje y precio**')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, 
                     x="odometer", 
                     y="price",
                     title="Relación entre Kilometraje y Precio",
                     labels={"odometer": "Kilometraje", "price": "Precio (USD)"},
                     opacity=0.6,
                     color_discrete_sequence=['#EF553B'])
    
    fig.update_layout(
        xaxis_title="Kilometraje",
        yaxis_title="Precio (USD)"
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Análisis de correlación
    correlation = car_data[['odometer', 'price']].corr().iloc[0, 1]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Correlación", f"{correlation:.3f}")
    with col2:
        if correlation < 0:
            st.info("📉 Correlación negativa: a mayor kilometraje, menor precio")
        else:
            st.info("📈 Correlación positiva: a mayor kilometraje, mayor precio")

# Casilla de verificación para histograma de precios
build_price_histogram = st.checkbox('Construir un histograma de precios')

if build_price_histogram:
    st.write('**Histograma de la distribución de precios**')
    
    # Crear un histograma de precios
    fig = px.histogram(car_data, 
                       x="price",
                       title="Distribución de Precios de Vehículos",
                       labels={"price": "Precio (USD)"},
                       nbins=50,
                       color_discrete_sequence=['#00CC96'])
    
    fig.update_layout(
        xaxis_title="Precio (USD)",
        yaxis_title="Frecuencia",
        showlegend=False
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Estadísticas adicionales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Precio Mínimo", f"${car_data['price'].min():,.0f}")
    with col2:
        st.metric("Precio Máximo", f"${car_data['price'].max():,.0f}")
    with col3:
        st.metric("Precio Promedio", f"${car_data['price'].mean():,.0f}")

# Casilla de verificación para gráfico de dispersión con color por condición
build_scatter_condition = st.checkbox('Construir gráfico de dispersión por condición del vehículo')

if build_scatter_condition:
    st.write('**Gráfico de dispersión: Kilometraje vs Precio (coloreado por condición)**')
    
    # Crear un gráfico de dispersión con color por condición
    fig = px.scatter(car_data, 
                     x="odometer", 
                     y="price",
                     color="condition",
                     title="Relación entre Kilometraje, Precio y Condición del Vehículo",
                     labels={"odometer": "Kilometraje", "price": "Precio (USD)", "condition": "Condición"},
                     opacity=0.6)
    
    fig.update_layout(
        xaxis_title="Kilometraje",
        yaxis_title="Precio (USD)"
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    # Información adicional
    st.info("💡 Los diferentes colores representan las distintas condiciones de los vehículos. Esto permite identificar patrones de precio según el estado del vehículo.")

# Separador
st.markdown("---")

# Sección adicional: Datos en bruto (opcional)
with st.expander("🔍 Ver datos en bruto"):
    st.dataframe(car_data.head(100))
    st.write(f"Mostrando las primeras 100 filas de {len(car_data)} registros totales")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Aplicación desarrollada con Streamlit y Plotly Express</p>
    <p>Sprint 7 - Proyecto de Análisis de Datos</p>
</div>
""", unsafe_allow_html=True)
