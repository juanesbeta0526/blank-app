import streamlit as st
import pandas as pd
import sqlite3
import requests

st.title("📦 Visor de Importaciones 2025")

# URL de descarga directa desde Google Drive
URL_DB = "https://drive.google.com/file/d/1fBn2GPoGV6CTTwt55jNAF5UchM_E37bk/view?usp=sharing"

# Descargar y guardar archivo temporalmente
@st.cache_resource
def descargar_y_guardar_db():
    response = requests.get(URL_DB)
    with open("importaciones.db", "wb") as f:
        f.write(response.content)
    return "importaciones.db"

ruta_db = descargar_y_guardar_db()
conn = sqlite3.connect(ruta_db)

# Mostrar lista de tablas
tablas = [
    "01_Importaciones_2025_Enero",
    "02_Importaciones_2025_Febrero",
    "03_Importaciones_2025_Marzo",
    "04_Importaciones_2025_Abril"
]
tabla = st.selectbox("📁 Selecciona una tabla:", tablas)

# Mostrar los datos de la tabla seleccionada
try:
    df = pd.read_sql(f"SELECT * FROM '{tabla}'", conn)
    st.success(f"✅ Total de registros: {len(df)}")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error("❌ Error al cargar la tabla.")
    st.exception(e)
