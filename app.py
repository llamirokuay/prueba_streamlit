import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    st.header('Venta de coches')
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir tabla dispersion') # crear un botón
    
if hist_button:
    st.write('Creación de una tabla de dispersion para el conjunto de datos de anuncios de venta de coches')
    st.header('Grafico dispersion')
    fig = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig, use_container_width=True)