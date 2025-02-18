import pandas as pd
import os
import json

# Cargar el archivo Excel correctamente
df = pd.read_excel('turismo/dataset_Turismo.xlsx')

# Normalizar la columna FECHA (si existe en el DataFrame)
for col in ['FECHA', 'FECHA_CORTE']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format='%Y%m%d', errors='coerce')
        df[col] = df[col].dt.strftime('%Y/%m/%d')  # Formato YYYY/MM/DD

# Convertir la columna UBIGEO a tipo entero, eliminando los decimales
if 'UBIGEO' in df.columns:
    df['UBIGEO'] = df['UBIGEO'].astype('Int64')

# Ruta del archivo JSON
json_file = 'turismo/dataset_turismo.json'

# Guardar el JSON sin que escape caracteres
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=1)

# Verificar si el archivo JSON fue creado
if os.path.exists(json_file):
    print('File JSON created')
else:
    print('Error: File JSON not created')
