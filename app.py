import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis exploratorio de datos de anuncios de vehículos")

# crear primer botón
hist_button = st.button('Construir histograma')

# al hacer clic en el botón
if hist_button:
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

# crear segundo botón
disp_button = st.button('Construir un gráfico de dispersión')

# al hacer clic en el botón
if disp_button:
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

# crear una casilla de verificación
build_boxplot = st.checkbox('Construir un gráfico de caja y bigotes')

if build_boxplot:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de caja y bigotes de los días listados de los anuncios')

    # crear un gráfico de caja y bigotes
    fig3 = px.box(car_data, y='days_listed', points="all")

    # mostrar un gráfico iteractivo
    st.plotly_chart(fig3, use_container_width=True)

# crear segunda casilla de verificación
build_bar = st.checkbox('Construir gráfico de barras')

if build_bar:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write(
        'Creación de gráfico de barras para los tipos de transmisión')

    # crear un gráfico de barras
    fig4 = px.histogram(car_data, x='transmission',
                        title='Cantidad por Tipo de Transmisión')

    # mostrar un gráfico iteractivo
    st.plotly_chart(fig4, use_container_width=True)
