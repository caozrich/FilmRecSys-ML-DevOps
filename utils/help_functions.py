import pandas as pd


def genres_bin():
  
  df = pd.read_csv('movies_dataset_reduced.csv')

  df['genres'] = df['genres'].apply(ast.literal_eval)

  genreList = ['History', 'Animation', 'Mystery', 'Comedy', 'Documentary', 'War', 'Action', 'Romance', 'Family', 'Adventure', 'Thriller', 'Fantasy', 'TV Movie', 'Crime', 'Music', 'Horror', 'Drama', 'Foreign', 'Science Fiction', 'Western']

  generos_df = pd.DataFrame(columns=genreList, index=df.index)
  for i, row in df.iterrows():
      genres = row['genres']
      for genre in genres:
          if genre in genreList:
              generos_df.loc[i, genre] = 1

  generos_df.fillna(0, inplace=True)
  generos_df.to_csv('genres_binary.csv')

