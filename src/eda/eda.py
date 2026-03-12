import pandas as pd

DATA_PATH = 'data/processed/albums_clean.csv'

# Carga del DataFrame limpio
def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

# Top 10 artistas por número de álbumes
def top_artists(df: pd.DataFrame, n: int = 10) -> pd.Series:
    print('\n    Top 10 artistas por número de álbumes:')
    return df['artist'].value_counts().head(n)

# Descripción estadística del DataFrame limpio
def df_describe(df: pd.DataFrame) -> pd.DataFrame:
    print('\n    Descripción estadística del DataFrame limpio:')
    return df.describe()

# Valores faltantes por columna
def missing_values(df: pd.DataFrame) -> pd.Series:
    print('\n    Valores faltantes por columna:')
    return df.isnull().sum()

# Número de álbumes por década
def top_decade(df: pd.DataFrame) -> pd.Series:
    df['decade'] = (df['release_date'] // 10) * 10
    print('\n    Número de álbumes por década:')
    return df['decade'].value_counts().sort_index()

# Año con más álbumes
def top_year(df:pd.DataFrame) -> pd.Series:
    print('\n    Año con más álbumes:')
    return df['release_date'].value_counts().head(1)

# Calificación promedio por artista (solo artistas con más de 2 álbumes)
def mean_rating(df: pd.DataFrame) -> pd.Series:
    mean_rating = df.groupby('artist')['rating'].agg(['mean', 'count'])
    result = mean_rating[mean_rating['count'] > 2]
    result = result.sort_values('mean', ascending=False).round(1)
    print('\n    Calificación promedio por artista:')
    return result.head(5)

# Calificación promedio por década
def mean_decade(df: pd.DataFrame) -> pd.DataFrame:
    df['decade'] = (df['release_date'] // 10) * 10
    result = df.groupby('decade')['rating'].mean().round(1)
    print('\n    Calificación promedio por década:')
    return result

# Álbumes con calificación de 5 estrellas
def five_stars_albums(df: pd.DataFrame) -> pd.DataFrame:
    five_stars = df[df['rating'] == 5]
    print('\n    Álbumes con calificación de 5 estrellas:')
    return five_stars.describe()

def corr_albums(df: pd.DataFrame) -> pd.DataFrame:
    print('\n    Correlación entre variables numéricas:')
    corr_songs_rating = df[['songs', 'rating']].corr()
    corr_durations_rating = df[['duration_min', 'rating']].corr()
    corr_year_duration = df[['release_date', 'duration_min']].corr()
    return corr_songs_rating, corr_durations_rating, corr_year_duration

if __name__ == '__main__':
    df = load_data()
    print('\n    Forma del DataFrame limpio: ', df.shape)
    print(df_describe(df))
    print(missing_values(df))
    print(top_artists(df))
    print(top_decade(df))
    print(top_year(df))
    print(mean_rating(df))
    print(mean_decade(df))
    print(five_stars_albums(df))
    print(corr_albums(df))