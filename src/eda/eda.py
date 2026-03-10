import pandas as pd

DATA_PATH = 'data/processed/albums_clean.csv'

def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def top_artists(df: pd.DataFrame, n: int = 10) -> pd.Series:
    print('\n    Top 10 artistas por número de álbumes:')
    return df['artist'].value_counts().head(n)

def df_describe(df: pd.DataFrame) -> pd.DataFrame:
    print('\n    Descripción estadística del DataFrame limpio:')
    return df.describe()

def missing_values(df: pd.DataFrame) -> pd.Series:
    print('\n    Valores faltantes por columna:')
    return df.isnull().sum()

def top_decade(df: pd.DataFrame) -> pd.Series:
    df['decade'] = (df['release_date'] // 10) * 10
    print('\n    Número de álbumes por década:')
    return df['decade'].value_counts().sort_index()

def top_year(df:pd.DataFrame) -> pd.Series:
    print('\n    Año con más álbumes:')
    return df['release_date'].value_counts().head(1)

def mean_rating(df: pd.DataFrame) -> pd.Series:
    mean_rating = df.groupby('artist')['rating'].agg(['mean', 'count'])
    result = mean_rating[mean_rating['count'] > 2]
    result = result.sort_values('mean', ascending=False).round(1)
    print('\n    Calificación promedio por artista:')
    return result.head(5)

def mean_decade(df: pd.DataFrame) -> pd.DataFrame:
    df['decade'] = (df['release_date'] // 10) * 10
    result = df.groupby('decade')['rating'].mean().round(1)
    print('\n    Calificación promedio por década:')
    return result

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