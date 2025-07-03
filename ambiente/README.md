Los siguientes Datasets corresponden a información sobre la **Calidad del aire**, registrados por la Dirección General de Salud Ambiental, comprendidos entre los años 2000 al 2019. Estos datos fueron publicados por DIGESA en su propia plataforma web. Los datos aquí pertenecen específicamente de la región LAMBAYEQUE, a través de su MONITOREO PUNTUAL HISTÓRICO DE CALIDAD DEL AIRE, tal como lo indica el repositorio.
Los datos del CO2, los publicó el Ministerio del Ambiente - MINAM con el propósito de proporcionar una base de datos comprensiva que permita evaluar y monitorear las emisiones de Gases de Efecto Invernadero - GEI, facilitando el desarrollo de políticas y estrategias para mitigar el cambio climático. Están disponibles en la Plataforma Nacional de Datos Abiertos del gobierno peruano.

Cada Dataset contiene información detallada sobre la concentración de cada contaminante lo largo del período. Los datos están organizados por departamento, provincia, distrito, año, metodología y concentración (µg/m³).

El dataset se clasifica por el índice de contaminación del aire:

* CO2: Dióxido de carbono en el aire
* NO2: Dióxido de nitrógeno en el aire
* PM2.5: Partículas finas del aire
* PM10: Partículas gruesas del aire
* SO2: Dióxido de azufre en el aire

**Estructura de datos:**  
Los archivos están en formatos: csv, xlsx y json, para mayor facilidad al momento de trabajar con estos.

**Los datasets están conformados por las siguientes columnas:**

**Para el Dioxido de carbono (CO2)**  
  ✅FECHA\_CORTE:	Día en que se generó el dataset  
  ✅ANIO: Año en el que se generaron las correspondientes emisiones  
  ✅SECTOR: Uno de los cuatro sectores principales de emisiones según las Directrices del IPCC de 2006: Energía, Industria.  
  ✅CATEGORIA:	Categoría de las emisiones según la clasificación de las Directrices del IPCC de 2006.  
  ✅SUBCATEGORIA: Subcategoría específica dentro de la categoría principal de emisiones.  
  ✅FUENTE\_DE\_EMISION:	Fuente específica de las emisiones.  
  ✅IPCC\_CLASF: Código clasificador estandarizado del IPCC para categorizar las fuentes de emisiones.  
  ✅DIOXIDO\_DE\_CARBONO\_GGCO2:	Emisiones de dióxido de carbono (CO2) expresadas en gigagramos de CO2.  
  ✅METANO\_GGCH4: Emisiones de metano (CH4) expresadas en gigagramos de CH4.  
  ✅METANO\_EQUIVALENTE\_GGCO2EQ: Emisiones de metano expresadas en dióxido de carbono equivalentes (CO2eq)  
  ✅OXIDO\_NITROSO\_GGN2O:	Emisiones de óxido nitroso (N2O) expresadas en gigagramos de N2O  
  ✅OXIDO\_NITROSO\_EQUIVALENTE\_GGCO2EQ:	Emisiones de óxido nitroso expresadas en dióxido de carbono equivalentes (CO2eq)  
  ✅HFC\_GGCO2EQ:	Emisiones de hidrofluorocarbonos (HFCs) expresadas en dióxido de carbono equivalentes (CO2eq)  
  ✅EMISIONES\_GEI\_GGCO2EQ:	Emisiones totales de gases de efecto invernadero, incluyendo CO2, CH4, N2O y HFC, expresadas en dióxido de carbono equivalentes (CO2eq)

**Para los demás contaminantes del aire**  
  ✅DEPARTAMENTO: Región donde se sacó los datos (LAMBAYEQUE)  
  ✅PROVINCIA: Provincias relacionadas al departamento  
  ✅DISTRITO: Distritos relacionados a cada provincia  
  ✅COD\_VAL: valor del contaminante  
  ✅NOMBRE\_ESTACION\_VAL: Identifica el nombre de las 5 estaciones  
  ✅METODOLOGÍA: Tipo de metodología  
  ✅FECHA: Fecha en la que se realizó el dataset  
  ✅CONCENTRACIÓN (µg/m³): valor decimal de la concentración del contaminante en el aire  
  ✅AÑO: Año en la que se realizó el dataset


**Fuentes:**  
👉NO2   http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA\_AIR\_MR\_CalidadAirePuntual\_LAMBAYEQUE.html#NO2a  
👉PM2.5 http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA\_AIR\_MR\_CalidadAirePuntual\_LAMBAYEQUE.html#PM2a  
👉PM10  http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA\_AIR\_MR\_CalidadAirePuntual\_LAMBAYEQUE.html#PM1a  
👉SO2   http://www.digesa.minsa.gob.pe/DCOVI/mapas/DIGESA\_AIR\_MR\_CalidadAirePuntual\_LAMBAYEQUE.html#SO2a

👉CO2 https://datosabiertos.gob.pe/dataset/inventario-nacional-de-emisiones-de-gases-de-efecto-invernadero-ministerio-del-ambiente

**Fecha de actualización:**  
👉 17/02/2025