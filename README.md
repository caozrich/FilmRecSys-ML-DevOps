<p align="center">
  <img alt="Files Logo" src="https://github.com/caozrich/FilmRecSys-ML-DevOps/assets/34092193/8d3f6f12-8472-49ed-8213-287ec46a7373" width="450" />
  <h1 align=center style="color: #FF2403">MLOps: Proyecto de Recomendación de Películas</h1>
</p>

![Python version](https://img.shields.io/badge/Python-3.11.0-lightgrey) ![AppFramework](https://img.shields.io/badge/libs-pandas-blue) ![API](https://img.shields.io/badge/-fast--api-blue) ![ML](https://img.shields.io/badge/-scikit--learn-orange) ![ML](https://img.shields.io/badge/-uvicorn-brightgreen) ![AppFramework](https://img.shields.io/badge/-streamlit-yellow) ![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-green)

## Contenido
- [Description](#Descripción del proyecto)
- [About](#About)
- [Download](#Download)

## Descripción del proyecto

Este proyecto tiene como objetivo implementar un sistema de recomendación de películas utilizando técnicas de `Machine Learning Operations (MLOps)`. Se aborda el desafío de llevar el modelo de recomendación al mundo real y asegurar un ciclo de vida completo para el proyecto de Machine Learning.

### Descripción del Problema

El contexto de este proyecto se encuentra en una start-up que ofrece servicios de agregación de plataformas de streaming. Como Data Scientist, el rol consiste en desarrollar un sistema de recomendación que aún no ha sido implementado. El desafío es transformar los [datos disponibles](https://github.com/caozrich/FilmRecSys-ML-DevOps/tree/main/data), que presentan problemas de madurez, en un formato adecuado para el entrenamiento y mantenimiento del modelo de Machine Learning.

### Rol a Desarrollar
Como Data Scientist en esta start-up, se requiere llevar a cabo tareas de `Data Engineering` para tratar y recolectar los datos existentes. Esto implica realizar procesos de transformación, automatizar la actualización de nuevos datos y asegurar la calidad de los mismos. El objetivo es desarrollar un Minimum Viable Product (MVP), lo que requiere un trabajo rápido y eficiente en la ingeniería de datos.

## Objetivos del Proyecto
- Realizar el proceso de Extracción, Transformación y Carga (ETL) de los datos de películas disponibles.
- Realizar un Análisis Exploratorio de Datos (EDA) para comprender las características y calidad de los datos.
- Implementar funciones de recomendación basadas en técnicas de Machine Learning. 
- Desplegar un servicio web (API) para acceder al modelo de recomendación de películas.
- Desarrollar una aplicación web que consuma el API y ofrezca una interfaz amigable para los usuarios.

## Pipeline

<img src="https://github.com/caozrich/FilmRecSys-ML-DevOps/assets/34092193/0148eb2b-3380-47a9-a36d-0c10975cc86f" width="800" height="538"/>

## Extracción, Transformación y Carga (ETL):
[Acede aquí al júpiter notebook](https://github.com/caozrich/FilmRecSys-ML-DevOps/blob/main/ETL.ipynb)

### 1. Preparación inicial de datos

- Imports y Carga de Datos: Se importan las bibliotecas y módulos necesarios para el proyecto, y se carga el conjunto de datos desde un archivo CSV.
- Eliminación de duplicados: Se verifica y elimina cualquier registro duplicado en el conjunto de datos.
- Verificación de valores nulos: Se identifican las columnas que contienen valores nulos en el conjunto de datos.
- Tratamiento de valores nulos: Se lleva a cabo un tratamiento para reemplazar o eliminar los valores nulos en las columnas relevantes.

### 2. Transformación y manipulación de datos

- Eliminar columnas que no se utilizarán: Se eliminan del conjunto de datos aquellas columnas que no son relevantes para el análisis o el modelo de recomendación. Esto ayuda a reducir la dimensionalidad y enfocarse en las características más importantes.

- Eliminar filas con valores faltantes en el campo 'release_date': Se eliminan las filas que tienen valores faltantes en el campo  `release_date`. Esto garantiza que todas las películas tengan una fecha de lanzamiento válida para su análisis y recomendación.

- Convertir 'release_date' al formato de fecha (AAAA-mm-dd): Se convierte la columna  `release_date` al formato de fecha estándar (AAAA-mm-dd). Esto permite un manejo más conveniente y consistente de las fechas en el conjunto de datos.

- Extraer el año de la fecha de estreno y crear una nueva columna `release_year`: Se extrae el año de la fecha de estreno y se crea una nueva columna llamada 'release_year'. Esta columna proporciona una representación simplificada del año de lanzamiento de cada película.

- Conversión de tipos de datos: Se realiza la conversión de los tipos de datos de ciertas columnas numéricas que pueden convertirse a tipos de datos numéricos apropiados para un análisis más preciso.

- Crear una nueva columna 'return' que calcule el retorno de inversión (revenue / budget): Se crea una nueva columna llamada `return` que calcula el retorno de inversión dividiendo los ingresos (`revenue`) por el presupuesto (`budget`). Esta columna proporciona información sobre la rentabilidad de cada película y puede ser útil para el proceso de recomendación.

### 3. Procesamiento de datos anidados

- Procesar datos anidados y extraer información relevante: se aborda el desafío de los datos anidados presentes en el conjunto de datos. Se realiza un procesamiento específico para extraer la información relevante de los campos anidados. Esto implica desglosar estructuras de datos complejas y extraer los atributos necesarios para el modelo de recomendación de películas.

### 4. Exportación

- Guardar el conjunto de datos limpio en un nuevo archivo CSV: Después de realizar todas las transformaciones y procesamientos necesarios en los datos, se guarda el conjunto de datos limpio en un nuevo archivo CSV. Esto asegura que los datos preprocesados estén disponibles para su uso posterior, sin la necesidad de repetir todo el proceso de limpieza y transformación cada vez que se ejecute el proyecto. 


## Análisis Exploratorio de Datos (EDA):
[Acede aquí al júpiter notebook](https://github.com/caozrich/FilmRecSys-ML-DevOps/blob/main/EDA.ipynb)


<img src="https://github.com/caozrich/FilmRecSys-ML-DevOps/assets/34092193/8864de30-9f61-4b08-8dbb-a9c227d7fd0f" width="800" height="538"/>

### 1.Exploración y Visualización del Conjunto de Datos:

- Visualización de las primeras filas del conjunto de datos (`df.head(5)`)

- Resumen estadístico del conjunto de datos (`df.describe()`)

- Información general sobre el conjunto de datos (`df.info()`)

### 2. Relación entre variables

* Outliers:

  Se identificaron outliers en el conjunto de datos en los siguientes aspectos:

  *Relación entre número de películas y puntaje de votación: La mayoría de las películas tienen un puntaje promedio alrededor de 6, indicando una calificación moderada. Sin embargo, un número significativo de películas tienen un puntaje de 0, considerados outliers en la distribución.

  *Presupuesto por año: La cantidad de películas estrenadas alcanza su máximo en 2018 y experimenta un descenso abrupto en 2019, lo cual puede considerarse un outlier en los datos. Esto podría ser atribuido a la influencia negativa de la pandemia en la industria cinematográfica.

  *Cantidad de películas estrenadas por año: Se observa un descenso en la cantidad de películas estrenadas en 2019, coincidiendo con la conclusión anterior sobre el presupuesto. Esto sugiere que el año 2019 fue atípico en la producción cinematográfica debido a la influencia de la pandemia.

### 3. Correlaciones

#### Variables con mayor correlación:

```
Variables más correlacionadas:
revenue - budget: 0.7683533474519021
popularity - revenue: 0.5051410846102767
revenue - popularity: 0.5051410846102767
budget - popularity: 0.4469396146589477
release_year - id: 0.30150514963953473
vote_average - popularity: 0.148352941806674
```

- Se observa una relación significativa entre el presupuesto y las ganancias de las películas, así como entre las ganancias y la popularidad. Estas correlaciones indican que, en general, a medida que aumenta el presupuesto invertido en una película, también tienden a aumentar las ganancias generadas por la misma. Además, existe una tendencia a que las películas más populares sean las que generan mayores ganancias.


## Desarrollo del API

Para disponibilizar los datos de la empresa, se propone utilizar el framework FastAPI para crear una API. Se han desarrollado varias funciones que corresponden a diferentes endpoints que se consumirán en la API. Cada función está decorada con el decorador @app.get('/') para indicar la ruta del endpoint.

A continuación, se describen las funciones disponibles en el API:

* Obtener cantidad de películas estrenadas por mes
   * Endpoint: `/peliculas_mes/{mes}`

   Descripción: Esta función recibe como parámetro el nombre del mes (por ejemplo, 'enero') y retorna la cantidad de películas que se estrenaron históricamente en ese mes.

* Obtener cantidad de películas estrenadas por día de la semana
   * Endpoint: `/peliculas_dia/{dia}`

   Descripción: Esta función recibe como parámetro el día de la semana (por ejemplo, 'lunes') y retorna la cantidad de películas que se estrenaron históricamente en ese día.

* Obtener información de una franquicia
   * Endpoint: `/franquicia/{franquicia}`

   Descripción: Esta función recibe como parámetro el nombre de una franquicia y retorna la cantidad de películas de esa franquicia, la ganancia total y el promedio de ganancia.

* Obtener cantidad de películas producidas en un país
   * Endpoint: `/peliculas_pais/{pais}`

   Descripción: Esta función recibe como parámetro el nombre de un país y retorna la cantidad de películas producidas en ese país.

* Obtener información de una productora
   * Endpoint: `/productoras/{productora}`

   Descripción: Esta función recibe como parámetro el nombre de una productora y retorna la ganancia total y la cantidad de películas producidas por esa productora.

* Obtener información de retorno de una película
   * Endpoint: `/retorno/{pelicula}`

    Descripción: Esta función recibe como parámetro el nombre de una película y retorna la inversión, la ganancia, el retorno y el año en que se lanzó.

* Obtener recomendaciones de películas similares
   * Endpoint: `/recomendacion/{selected_title}`

    Descripción: Esta función recibe el título de una película y devuelve una lista de 5 pelicula recomendadas por similitud y puntaje.
    Parámetros.

