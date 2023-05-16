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

Este proyecto tiene como objetivo implementar un sistema de recomendación de películas utilizando técnicas de Machine Learning Operations (MLOps). Se aborda el desafío de llevar el modelo de recomendación al mundo real y asegurar un ciclo de vida completo para el proyecto de Machine Learning.

### Descripción del Problema

El contexto de este proyecto se encuentra en una start-up que ofrece servicios de agregación de plataformas de streaming. Como Data Scientist, el rol consiste en desarrollar un sistema de recomendación que aún no ha sido implementado. El desafío es transformar los [datos disponibles](https://github.com/caozrich/FilmRecSys-ML-DevOps/tree/main/data), que presentan problemas de madurez, en un formato adecuado para el entrenamiento y mantenimiento del modelo de Machine Learning.

### Rol a Desarrollar
Como Data Scientist en esta start-up, se requiere llevar a cabo tareas de Data Engineering para tratar y recolectar los datos existentes. Esto implica realizar procesos de transformación, automatizar la actualización de nuevos datos y asegurar la calidad de los mismos. El objetivo es desarrollar un Minimum Viable Product (MVP), lo que requiere un trabajo rápido y eficiente en la ingeniería de datos.

## Objetivos del Proyecto
- Realizar el proceso de Extracción, Transformación y Carga (ETL) de los datos de películas disponibles.
- Realizar un Análisis Exploratorio de Datos (EDA) para comprender las características y calidad de los datos.
- Implementar funciones de recomendación basadas en técnicas de Machine Learning. 
- Desplegar un servicio web (API) para acceder al modelo de recomendación de películas.
- Desarrollar una aplicación web que consuma el API y ofrezca una interfaz amigable para los usuarios.

## Pipeline

<img src="https://github.com/caozrich/FilmRecSys-ML-DevOps/assets/34092193/0148eb2b-3380-47a9-a36d-0c10975cc86f" width="800" height="538"/>

## Extracción, Transformación y Carga (ETL):
`1. Preparación inicial de datos`

- Imports: Se importan las bibliotecas y módulos necesarios para el proyecto.
- Eliminación de duplicados: Se verifica y elimina cualquier registro duplicado en el conjunto de datos.
- Verificación de valores nulos: Se identifican las columnas que contienen valores nulos en el conjunto de datos.
- Tratamiento de valores nulos: Se lleva a cabo un tratamiento para reemplazar o eliminar los valores nulos en las columnas relevantes.

3. Ingesta de datos (Archivos .csv provistos por el cliente) en respectivos dataframes (Disney, Amazon, Hulu y Netflix)
4. Análisis exploratorio de los distintos datasets para conocer sus características principales
