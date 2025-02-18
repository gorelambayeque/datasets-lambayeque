Los siguientes Datasets corresponden a información sobre la **Calidad del aire**, registrados por la Dirección General de Salud Ambiental, comprendidos entre los años 2000 al 2019. Estos datos fueron publicados por DIGESA en su propia plataforma web. Los datos aquí pertenecen especificamente de la región LAMBAYEQUE, a travez de su MONITOREO PUNTUAL HISTÓRICO DE CALIDAD DEL AIRE, tal como lo indica el repositorio. 

Cada Dataset contiene información detallada sobre la concentración de cada contaminantea lo largo del período. Los datos están organizados por departamento, provincia, distritio, año, metodología y concentración (µg/m³).

El dataset se clasifica por el indice de contaminación del aire:  
- CO2: Dioxido de carbono en el aire
- NO2: Dióxido de nitrógeno en el aire   
- PM2.5: Partículas finas del aire
- PM10: Partículas gruesas del aire
- SO2: Dióxido de azufre en el aire

**Fuentes:**   
👉NO2   http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA_AIR_MR_CalidadAirePuntual_LAMBAYEQUE.html#NO2a
👉PM2.5 http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA_AIR_MR_CalidadAirePuntual_LAMBAYEQUE.html#PM2a 
👉PM10  http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA_AIR_MR_CalidadAirePuntual_LAMBAYEQUE.html#PM1a
👉SO2   http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA_AIR_MR_CalidadAirePuntual_LAMBAYEQUE.html#SO2a  

👉MINAM https://datosabiertos.gob.pe/dataset/inventario-nacional-de-emisiones-de-gases-de-efecto-invernadero-ministerio-del-ambiente

**Fecha de actualización:**  
👉 17/02/2025  

**Estructura de datos:**   
Los archivos están en formatos: csv, xlsx y json, para mayor facilidad al momento de trabajar con estos.  

**Los datasets están conformados por las siguientes columnas:**  
- **Para el Dioxido de carbono (CO2)**
✅FECHA_CORTE:	Día en que se generó el DATASET
✅ANIO: Año en el que se generaron las correspondientes emisiones.
✅SECTOR: Uno de los cuatro sectores principales de emisiones según las Directrices del IPCC de 2006: Energía, Industria.
✅CATEGORIA:	Categoría de las emisiones según la clasificación de las Directrices del IPCC de 2006.
✅SUBCATEGORIA:	Subcategoría específica dentro de la categoría principal de emisiones.
✅FUENTE_DE_EMISION:	Fuente específica de las emisiones.
✅IPCC_CLASF:	Código clasificador estandarizado del IPCC para categorizar las fuentes de emisiones.
✅DIOXIDO_DE_CARBONO_GGCO2:	Emisiones de dióxido de carbono (CO2) expresadas en gigagramos de CO2.
✅METANO_GGCH4:	Emisiones de metano (CH4) expresadas en gigagramos de CH4.
✅METANO_EQUIVALENTE_GGCO2EQ:	Emisiones de metano expresadas en dióxido de carbono equivalentes (CO2eq).
✅OXIDO_NITROSO_GGN2O:	Emisiones de óxido nitroso (N2O) expresadas en gigagramos de N2O.
✅OXIDO_NITROSO_EQUIVALENTE_GGCO2EQ:	Emisiones de óxido nitroso expresadas en dióxido de carbono equivalentes (CO2eq).
✅HFC_GGCO2EQ:	Emisiones de hidrofluorocarbonos (HFCs) expresadas en dióxido de carbono equivalentes (CO2eq).
✅EMISIONES_GEI_GGCO2EQ:	Emisiones totales de gases de efecto invernadero, incluyendo CO2, CH4, N2O y HFC, expresadas en dióxido de carbono equivalentes (CO2eq).  

- **Para los demás contaminantes del aire**  
✅DEPARTAMENTO: Región donde se sacó los datos (LAMBAYEQUE)
✅PROVINCIA: Provincias relacionadas al departamento 
✅DISTRITO: Distritos relacionados a cada provincia
✅COD_VAL: valor del contaminante
✅NOMBRE_ESTACION_VAL: Identifica el nombre de las 5 estaciones
✅METODOLOGÍA: Tipo de metodología
✅FECHA: Fecha en la que se realizó el dataset
✅CONCENTRACIÓN (µg/m³): valor decimal de la concentración del contaminante en el aire
✅AÑO: Año en la que se realizó el dataset

