import pandas as pd
import os
import json
from unidecode import unidecode

# Cargar el archivo CSV
#df = pd.read_csv('ambiente/CO2/dataset_dioxido.csv', dtype={'FECHA_CORTE': str}, sep=';', encoding='utf-8')
#df = pd.read_csv('ambiente/NO2/MONITOREO_CALIDAD_DEL_AIRE.csv', dtype={'FECHA_CORTE': str})
#df = pd.read_csv('ambiente/SO2/MONITOREO_CALIDAD_DEL_AIRE.csv')
#df = pd.read_csv('ambiente/PM2.5/MONITOREO_CALIDAD_AIRE.csv')
df = pd.read_csv('ambiente/PM10/MONITOREO_DE_CALIDAD_AIRE.csv')

# Normalizar los nombres de las columnas
def normalize_columns(col):
    col = unidecode(col) # Elimina tildes
    col = col.replace('Ñ', 'N').replace('ñ', 'n')
    col = col.replace('ANO', 'ANIO')  # Asegura que "AÑO" se convierta a "ANIO"
    return col

df.columns = [normalize_columns(col) for col in df.columns]

# Normalizar la columna FECHA_CORTE (si existe en el DataFrame)
if 'FECHA_CORTE' in df.columns:
    #df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], dayfirst=True, errors='coerce')
    df['FECHA_CORTE'] = pd.to_datetime(df['FECHA_CORTE'], format='%Y%m%d', errors='coerce')
    df['FECHA_CORTE'] = df['FECHA_CORTE'].dt.strftime('%Y/%m/%d')  # Formato DD/MM/YYYY

# Ruta del archivo JSON
#json_file = 'ambiente/CO2/data_dioxido_co2.json'
#json_file = 'ambiente/NO2/data_dioxido_no2.json'
#json_file = 'ambiente/SO2/CALIDAD_DEL_AIRE.json'
#json_file = 'ambiente/PM2.5/dataset_MC_AIRE.json'
json_file = 'ambiente/PM10/data_dioxido_pm10.json'

# Guardar el JSON manualmente sin que escape caracteres
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=4)

# Verificar si el archivo JSON fue creado
if os.path.exists(json_file):
    print('File JSON created')
else:
    print('Error: File JSON not created')
