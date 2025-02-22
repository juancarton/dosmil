#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import time
import random
import folium
from streamlit_folium import folium_static

# Configuración de la aplicación
st.title("🚁 EnRuta para Drones - Simulación")
st.write("Simulación de gestión y monitoreo de drones en entregas a domicilio.")

# Solicitar contraseña para acceso
def check_password():
    password = st.text_input("Ingrese la contraseña", type="password")
    return password == "admin123"

if not check_password():
    st.warning("Acceso denegado. Ingrese la contraseña correcta.")
    st.stop()

# Base de datos simulada de drones
drones = [
    {"id": 1, "modelo": "DJI Mavic 3", "bateria": 100, "capacidad_carga": "2kg"},
    {"id": 2, "modelo": "Parrot Anafi", "bateria": 95, "capacidad_carga": "1.5kg"},
    {"id": 3, "modelo": "Skydio 2", "bateria": 90, "capacidad_carga": "2.5kg"}
]

df_drones = pd.DataFrame(drones)

# Mostrar lista de drones
st.write("### Drones Disponibles")
st.dataframe(df_drones)

# Seleccionar un dron para la misión
selected_dron = st.selectbox("Selecciona un dron", df_drones["modelo"])

# Ingreso de coordenadas de destino
st.write("### Definir ruta de vuelo")
lat = st.number_input("Latitud del destino", value=19.4326, format="%.6f")
lon = st.number_input("Longitud del destino", value=-99.1332, format="%.6f")

if st.button("Iniciar Vuelo 🚀"):
    st.write(f"Dron {selected_dron} en camino...")
    
    # Simulación de vuelo en el mapa
    inicio = [19.4342, -99.1386]  # Ubicación inicial del dron
    destino = [lat, lon]
    
    # Crear mapa
    mapa = folium.Map(location=inicio, zoom_start=15)
    folium.Marker(inicio, tooltip="Inicio", icon=folium.Icon(color='blue')).add_to(mapa)
    folium.Marker(destino, tooltip="Destino", icon=folium.Icon(color='red')).add_to(mapa)
    
    # Simulación de movimiento
    for i in range(1, 11):
        lat_mov = inicio[0] + (destino[0] - inicio[0]) * (i / 10)
        lon_mov = inicio[1] + (destino[1] - inicio[1]) * (i / 10)
        folium.Marker([lat_mov, lon_mov], tooltip=f"Avance {i*10}%", icon=folium.Icon(color='green')).add_to(mapa)
        time.sleep(0.5)
    
    # Mostrar mapa
    folium_static(mapa)
    st.success("Dron ha llegado al destino 🏁")

