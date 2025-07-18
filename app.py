import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos

st.write('Creación gráficos interactivos')

hist_button = st.button('Construir histograma') # crear un botón
sc_button = st.button('Construir dispersión') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if sc_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un dispersión para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)