Los siguientes Datasets corresponden a información sobre la **Frecuencia de visitas turísticas**, registrados por el Servicio Nacional de Áreas Naturales Protegidas por el estado, comprendidos entre los años 2022 al 2023. Estos datos fueron publicados por el SERNANP en la Plataforma Nacional de Datos Abiertos del gobierno peruano, con fecha del 13/08/2024. La data ya está limpia, se ha filtrado unicamente los registros de la región LAMBAYEQUE, tal como lo indica el repositorio.  

El datset de Educacion, se trata de la lista de las intituciones educativas y los servicios que estas brindan a la población, en la región de Lambayeque, la data fue publicada en la Plataforma de ESCALE (Estadística de Calidad Educativa), herramienta del Ministerio de Educación (Minedu) que ofrece información estadística sobre las instituciones educativas del Perú. 

El dataset de educacion está caracetrizado por:
- Fecha: Fecha de corte.  
- Nombre SSEE: nombre del centro educativo o servicio educativo.    
- Ubicación geográfica: Ubigeo, departamento, provincia, distrito, centro poblado,latitud, longitud, altitud, dirección de la IIEE.  
- Modalidad: Indica si la institución educativa es inicial, primaria, etc.  
- Dependencia: Indica el tipo de gestión de la IIEE, privada, publica, etc.    


El dataset de turismo está caracterizado por:  
- Datos de Área Natural Protegida: Nombre, Sector, Departamento, Provincia y Distrito  
- Datos de turista: Procedencia, grupo de edad  
- Frecuencia de visitas: Fecha de la visita, Estadía 1 día, de 2 a 3 días y 3 a 30 días.  
- Datos de ubicación: ubigeo, departamento,provincia,distrito, residencia   
- Datos de alumno: genero,nacionalidad,año nacimiento, centro poblado, latitud, longitud, altitud    

**Estructura de datos:**   
Los archivos están en formatos: csv, xlsx y json, para mayor facilidad al momento de trabajar con estos.  

**Los datasets de IIEE están conformados por las siguientes columnas:**  
✅Codigo Modular: Identificador único para cada servicio educativo de una institución, este código permite diferenciar entre los distintos servicios (por ejemplo, primaria, secundaria, educación técnica)    
✅Nombre de SS.EE: Nombre de la Institución Educativa  
✅Ubigeo: Código de ubicación geográfica donde se encuentra la IE  
✅Departamento: Nombre del departamento donde se encuentra ubicada la IE   
✅Provincia: Nombre de la provincia donde se encuentra ubicada la IE    
✅Distrito: Nombre del distrito donde se encuentra ubicada la IE  
✅Código DRE/UGEL: Identificador único que asigna cada Dirección Regional de Educación (DRE) y Unidad de Gestión Educativa Local (UGEL) a las IE    
✅DRE / UGEL: Dirección Regional de Educación y Unidad de Gestión Educativa Local que pertenece   
✅Centro Poblado: Centro poblado donde se encuentra ubicada la IE    
✅Codigo Centro Poblado: Codigo del centro poblado  
✅Código Local: Codigo local dentro del perú  
✅Dirección: Dirección geográfica exacta donde esta ubicada la IE  
✅Nivel / Modalidad: Corresponde al nivel, inicial, primaria, secundaria y otros   
✅Gestion / Dependencia: Corresponde al tipo de gestión de la IE  
✅Latitud, longitud y altitud: Coordenadas geográficas que indican la posición precisa de la IE en la superficie terrestre   
✅Fuente de coordenadas: Procedencia de las coordenadas   

**Los datasets de Tirismo están conformados por las siguientes columnas:**  
✅ANP: Nombre del Área Natural Protegida  
✅SECTOR: Sector turístico de interés dentro del Área Natural Protegida  
✅DEPARTAMENTO: Departamento donde se encuentra ubicada el Área Natural Protegida  
✅PROVINCIA: Provincia donde se encuentra ubicada el Área Natural Protegida  
✅DISTRITO: Distrito donde se encuentra ubicada el Área Natural Protegida  
✅UBIGEO: Código de ubicación geográfica donde se encuentra ubicada el Área Natural Protegida  
✅PROCEDENCIA: Procedencia de visitas extranjero, nacional y local  
✅EDAD: Rango de edades en años: Infantes <5, Menores >= 5-16, Adultos >= 17-65 y Adultos mayores >65  
✅FECHA:	Fecha de ingreso al sector del Área Natural Protegida  
✅VISITAS_E1: Número de visitas con tiempo de estadía de 1 día  
✅VISITAS_E2A3: Número de visitas con tiempo de estadía de 2 a 3 días  
✅VISITAS_E3A30: Número de visitas con tiempo de estadía de 3 hasta 30 días  
✅FECHA_CORTE: Día en que se genero el dataset  


**Fuentes:**   
👉SERNANP: https://datosabiertos.gob.pe/dataset/frecuencia-de-visitas-tur%C3%ADsticas-en-las-%C3%A1reas-naturales-protegidas-por-el-estado-%E2%80%93-servicio  
👉ESCALE: https://sigmed.minedu.gob.pe/mapaeducativo/mapassee.aspx      

**Fecha de actualización:**  
👉 05/05/2025  
