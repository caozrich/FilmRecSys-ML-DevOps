import ast
import numpy as np
import pandas as pd
from fastapi import FastAPI
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import OneHotEncoder

app  = FastAPI(
    title="API películas",
    version="1.0",
    description="Esta API permite buscar información sobre películas y series, desarrolada por Richard Libreros (Github:caozrich)",
    docs_url="/docs",
)


df   = pd.read_csv('data/movies_dataset_cleaned.csv') 
df_r = pd.read_csv('data/movies_dataset_reduced.csv') 


@app.get("/peliculas_mes/{mes}")
async def peliculas_mes(mes:str):
        
    """ 
    Esta función sirve para obtener la cantidad de películas lanzadas en un mes específico.

    Parametros:
    - mes: str, el nombre del mes en español (por ejemplo, 'enero', 'febrero', etc.).

    Retorna:
    - Un diccionario con dos claves: 'mes' y 'cantidad'. 'mes' contiene el nombre del mes ingresado y 'cantidad' contiene el número de películas lanzadas en ese mes.

    Ejemplo de uso:
    >>> peliculas_mes('enero')

    """ 
    
    meses = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio': 'July',
        'agosto': 'August',
        'septiembre': 'September',
        'octubre': 'October',
        'noviembre': 'November',
        'diciembre': 'December'
    }
    
    df['release_date'] = pd.to_datetime(df['release_date'])
    df_mes = df[df['release_date'].dt.month_name() == meses[mes].capitalize()]
    respuesta = len(df_mes)
    
    return {'mes': mes, 'cantidad': respuesta}



@app.get("/peliculas_dia/{dia}")
async def peliculas_dia(dia:str):
        
    """ 
    Esta función sirve para obtener la cantidad de películas lanzadas en un día de la semana específico.

    Parametros:
    - dia: str, el nombre del día de la semana en español (por ejemplo, 'lunes', 'martes', etc.).

    Retorna:
    - Un diccionario con dos claves: 'dia' y 'cantidad'. 'dia' contiene el nombre del día ingresado y 'cantidad' contiene el número de películas lanzadas en ese día de la semana.

    Ejemplo de uso:
    >>> peliculas_dia('lunes')

    """
            
    dias = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miércoles': 'Wednesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sábado': 'Saturday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'
    }
    
    df['release_date'] = pd.to_datetime(df['release_date'])
    df_dia = df[df['release_date'].dt.day_name() == dias[dia].capitalize()]
    respuesta = len(df_dia)
    
    return {'dia': dia, 'cantidad': respuesta}



@app.get("/franquicia/{franquicia}")
async def franquicia(franquicia:str):
    
    """
    Esta función recibe el nombre de una franquicia y devuelve la cantidad de películas en la franquicia,
    la suma de los retornos de todas las películas de la franquicia y el retorno promedio de la franquicia.

    Parámetros:
    - franquicia: str, el nombre de la franquicia.

    Retorna:
    - Un diccionario con las siguientes claves:
        - 'franquicia': str, el nombre de la franquicia ingresada.
        - 'cantidad': int, la cantidad de películas en la franquicia.
        - 'ganancia_total': float, la suma de los retornos de todas las películas de la franquicia.
        - 'ganancia_promedio': float, el retorno promedio de la franquicia.

    Ejemplo de uso:
    >>> franquicia('Pixar Animation Studios')
    """
    
    franquicia_data = df.loc[df['belongs_to_collection'] == franquicia]
    cantidad = len(franquicia_data)
    ganancia_total = franquicia_data['return'].sum()
    ganancia_promedio = franquicia_data['return'].mean()
    
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}



@app.get("/peliculas_pais/{pais}")
async def peliculas_pais(pais:str):
    
    """ 
    Esta función recibe el nombre de un país y devuelve la cantidad de películas producidas en ese país.

    Parámetros:
    - pais: str, el nombre del país.

    Retorna:
    - Un diccionario con dos claves: 'pais' y 'cantidad'. 'pais' contiene el nombre del país ingresado y 'cantidad' contiene la cantidad de películas producidas en ese país.

    Ejemplo de uso:
    >>> peliculas_pais('United States of America')

    """ 
    
    num_movies = 0

    for countries in df['production_countries'].dropna():
        if pais in countries:
            num_movies += 1

    return {'pais': pais, 'cantidad': num_movies}



@app.get("/productoras/{productora}")
async def productoras(productora:str):
    """
    Toma como entrada el nombre de una productora, la ganancia total y cantidad de películas
    producidas por esa productora.
        
    Parámetros:
    - productora: str, el nombre de la productora.

    Retorna:
    - Un diccionario con las siguientes claves:
        - 'productora': str, el nombre de la productora ingresada.
        - 'ganancia_total': int, la ganancia total de las películas producidas por la productora.
        - 'cantidad': int, la cantidad de películas producidas por la productora.

    Ejemplo de uso:
    >>> productoras('Warner Bros. Pictures')

    """
    
    mask = df['production_companies'].apply(lambda x: isinstance(x, str) and productora in x)
    df_filtered = df[mask].dropna(subset=['production_companies'])


    ganancia_total = df_filtered['revenue'].sum()
    cantidad = len(df_filtered)

    return {'productora': productora, 'ganancia_total': int(ganancia_total), 'cantidad': cantidad}




@app.get("/retorno/{pelicula}")
async def retorno(pelicula:str):
        
    """ 
    Esta función recibe el título de una película y devuelve un diccionario con información sobre su inversión, ganancia, retorno y año de lanzamiento. 

    Parámetros:
    - pelicula: str, el título de la película.

    Retorna:
    - Un diccionario con las siguientes claves:
        - 'pelicula': str, el título de la película ingresada.
        - 'inversion': int, la inversión realizada en la película.
        - 'ganancia': int, la ganancia obtenida por la película.
        - 'retorno': float, el retorno de la inversión de la película.
        - 'año': int, el año de lanzamiento de la película.

    Ejemplo de uso:
    >>> retorno('Toy Story 2')

    """ 
        
    pelicula_data = df.loc[df['title'] == pelicula]
    inversion = pelicula_data['budget'].iloc[0]
    ganancia = pelicula_data['revenue'].iloc[0]
    retorno = pelicula_data['return'].iloc[0]
    año = pelicula_data['release_year'].iloc[0]
    
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'año': año}



@app.get("/recomendacion/{selected_title}")
async def recomendacion(selected_title:str):
    """ 
    Esta función recibe el título de una película y devuelve una lista de 5 pelicula recomendadas por similitud y puntaje.
    Parámetros:
    - selected_title: str, el título de la película seleccionada.

    Retorna:
    - Una lista de 5 películas recomendadas por similitud y puntaje.

    Ejemplo de uso:
    >>> recomendacion3('Batman')

    """ 

    k = 6
    df_r['genres'] = df_r['genres'].apply(ast.literal_eval)
    df_r['genres_str'] = df_r['genres'].apply(lambda x: '|'.join(x))
    encoder = OneHotEncoder()
    encoder.fit(df_r[['genres_str']])
    genres_encoded = encoder.transform(df_r[['genres_str']])
    generos_df = pd.DataFrame(genres_encoded.toarray(), columns=encoder.get_feature_names_out(['genres_str']))
    selected_genres = df_r.loc[df_r['title'] == selected_title]['genres'].values[0]
    df_r['genre_similarity'] = df_r['genres'].apply(lambda x: len(set(selected_genres) & set(x)) / len(set(selected_genres) | set(x)))
    df_r['same_series'] = df_r['title'].apply(lambda x: 1 if selected_title in x else 0)
    features_df = pd.concat([generos_df, df_r['vote_average'], df_r['genre_similarity'], df_r['same_series']], axis=1)
    knn = NearestNeighbors(n_neighbors=k+1, algorithm='auto')
    knn.fit(features_df)
    indices = knn.kneighbors(features_df.loc[df_r['title'] == selected_title])[1].flatten()
    recommended_movies = list(df_r.iloc[indices]['title'])
    recommended_movies = sorted(recommended_movies, key=lambda x: (df_r.loc[df_r['title'] == x]['same_series'].values[0], df_r.loc[df_r['title'] == x]['vote_average'].values[0], df_r.loc[df_r['title'] == x]['genre_similarity'].values[0]), reverse=True)
    recommended_movies = [movie for movie in recommended_movies if movie != selected_title]
    return {'lista recomendada': recommended_movies[0:5]}
        


# import asyncio

# async def main():
#     result1 = await peliculas_mes("febrero")
#     print(result1)
    
#     result2 = await peliculas_dia('miercoles')
#     print(result2)
    
#     result3 = await franquicia('Toy Story Collection')
#     print(result3)
    
#     result4 = await peliculas_pais('United States of America')
#     print(result4)
    
#     result5 = await productoras('Pixar Animation Studios')
#     print(result5)
    
#     result6 = await retorno('Toy Story')
#     print(result6)
    
#     result7 = await recomendacion("Batman")
#     print(result7)

# asyncio.run(main())
