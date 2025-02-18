import pandas as pd
import os
import json

# Cargar el archivo CSV
#df = pd.read_excel('salud/distrito/SE_DIAGNOSTICO.xlsx')
#df = pd.read_excel('salud/distrito/SE_EPIDEMIOLOGICA.xlsx')
#df = pd.read_excel('salud/distrito/SE_NUM_CASOS.xlsx')

#df = pd.read_excel('salud/provincia/SE_FCLINICA.xlsx')
df = pd.read_excel('salud/provincia/SE_EPIDEMIOLOGICA.xlsx')
#df = pd.read_excel('salud/provincia/SE_NUM_CASOS.xlsx')

df.columns = [(col) for col in df.columns]

# Ruta del archivo JSON
#json_file = 'salud/distrito/data_x_diagnostico.json'
#json_file = 'salud/distrito/data_x_epidemiologia.json'
#json_file = 'salud/distrito/data_num_casos.json'

#json_file = 'salud/provincia/se_fclinica.json'
json_file = 'salud/provincia/se_epidemiologia.json'
#json_file = 'salud/provincia/se_num_casos.json'

# Guardar el JSON manualmente sin que escape caracteres
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(df.to_dict(orient='records'), f, ensure_ascii=False, indent=4)

# Verificar si el archivo JSON fue creado
if os.path.exists(json_file):
    print('File JSON created')
else:
    print('Error: File JSON not created')
