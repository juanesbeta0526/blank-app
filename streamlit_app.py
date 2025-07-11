import streamlit as st
import pandas as pd
import sqlite3
import requests
import io

st.title("📦 Visor de Importaciones 2025")

# Descargar el archivo .db desde Google Drive
@st.cache_data
def descargar_db():
    url = "https://drive.google.com/uc?export=download&id=1yivdMmrunmaq_lzSKjk4-QrSnQL0Pstt"
    response = requests.get(url)
    return io.BytesIO(response.content)

db_file = descargar_db()
conn = sqlite3.connect(f"file:{db_file}?mode=ro", uri=True)

# Mostrar lista de tablas
tablas = ["01_Importaciones_2025_Enero", "02_Importaciones_2025_Febrero", "03_Importaciones_2025_Marzo", "04_Importaciones_2025_Abril"]
tabla_seleccionada = st.selectbox("Selecciona una tabla", tablas)

# Leer la tabla completa
df = pd.read_sql(f"SELECT * FROM '{tabla_seleccionada}'", conn)
st.write(f"Total de registros: {len(df)}")
st.dataframe(df, use_container_width=True)

