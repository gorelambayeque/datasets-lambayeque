Los siguientes Datasets corresponden a información sobre la **Frecuencia de visitas turísticas**, registrados por el Servicio Nacional de Áreas Naturales Protegidas por el estado, comprendidos entre los años 2022 al 2023. Estos datos fueron publicados por el SERNANP en la Plataforma Nacional de Datos Abiertos del gobierno peruano, con fecha del 13/08/2024. La data ya está limpia, se ha filtrado unicamente los registros de la región LAMBAYEQUE, tal como lo indica el repositorio.  

El datset de Educacion, se trata de la lista de las intituciones educativas y los servicios que estas brindan a la población, en la región d eLambayeque, la data fue publicada en la Plataforma de ESCALE (Estadística de Calidad Educativa), herramienta del Ministerio de Educación (Minedu) que ofrece información estadística sobre las instituciones educativas del Perú. 

El dataset está caracterizado por:  
- Datos de Área Natural Protegida: Nombre, Sector, Departamento, Provincia y Distrito  
- Datos de turista: Procedencia, grupo de edad  
- Frecuencia de visitas: Fecha de la visita, Estadía 1 día, de 2 a 3 días y 3 a 30 días.  
- Datos de ubicación: ubigeo, departamento,provincia,distrito, residencia   
- Datos de alumno: genero,nacionalidad,año nacimiento, centro poblado, latitud, longitud, altitud    

**Fuentes:**   
👉SERNANP: https://datosabiertos.gob.pe/dataset/frecuencia-de-visitas-tur%C3%ADsticas-en-las-%C3%A1reas-naturales-protegidas-por-el-estado-%E2%80%93-servicio  
👉ESCALE: https://sigmed.minedu.gob.pe/mapaeducativo/mapassee.aspx      

**Fecha de actualización:**  
👉 17/02/2025  

**Estructura de datos:**   
Los archivos están en formatos: csv, xlsx y json, para mayor facilidad al momento de trabajar con estos.  

**Los datasets están conformados por las siguientes columnas:**  
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
