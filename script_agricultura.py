import pandas as pd
import os
import json
from unidecode import unidecode

# Cargar el archivo CSV
#df = pd.read_csv('agricultura/componente_ambiental_suelo.csv')
df = pd.read_csv('agricultura/data_sedimentos.csv')

# Normalizar los nombres de las columnas
def normalize_columns(col):
    col = unidecode(col)  # Elimina tildes
    return col

df.columns = [normalize_columns(col) for col in df.columns]

# Ruta del archivo JSON
#json_file = 'agricultura/ca_suelo.json'
json_file = 'agricultura/data_sedimentos.json'

# Guardar el JSON manualmente sin que escape caracteres
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=4)

# Verificar si el archivo JSON fue creado
if os.path.exists(json_file):
    print('File JSON created')
else:
    print('Error: File JSON not created')
