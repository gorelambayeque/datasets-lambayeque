#script para sectores como educacion, turismo, natalidad
import pandas as pd
import os
import json

# Cargar el archivo Excel correctamente
#df = pd.read_excel('educacion/turismo/dataset_turismo_2022-2023.xlsx')
df = pd.read_excel('educacion/educacion/data_iiee.xlsx')
#df = pd.read_excel('natalidad/data_natalidad_2020-2025.xlsx')

# Convertir la columna de fecha a string (formato día/mes/año)
df['fecha de corte'] = df['fecha de corte'].dt.strftime('%d/%m/%Y')

# Ruta paa guardar el archivo JSON
#json_file = 'educacion/turismo/dataset_turismo.json'
json_file = 'educacion/educacion/data_iiee.json'
#json_file = 'natalidad/data_natalidad_2020-2025.json'

# Guardar el JSON sin que escape caracteres
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=1)

# Verificar si el archivo JSON fue creado
if os.path.exists(json_file):
    print('File JSON created')
else:
    print('Error: File JSON not created')
