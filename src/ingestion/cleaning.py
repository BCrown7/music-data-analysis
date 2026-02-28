import re
import pandas as pd

# Función para convertir la duración a minutos
def parse_length(value: str) -> int:
    if pd.isna(value) or str(value).strip() == "-":
        return None

    match_h = re.search(r'(\d+)h', value)
    match_m = re.search(r'(\d+)min', value)
    match_s = re.search(r'(\d+)s', value)
    
    h = int(match_h.group(1)) if match_h else 0
    m = int(match_m.group(1)) if match_m else 0
    s = int(match_s.group(1)) if match_s else 0
    
    total = (h * 60) + m + round(s / 60)
    return total

# Función para convertir la calificación a un número entero
def parse_rate(value: str) -> int:
    if pd.isna(value):
        return None
    return str(value).count("✯")

# Función para extraer el año de la fecha de lanzamiento (en caso de antologias con varios años)
def parse_year(value: str)-> int:
    if pd.isna(value):
        return None
    match_year = re.search(r'(\d{4})', value)
    return int(match_year.group(1)) if match_year else None

# Función para aplicar las transformaciones al DataFrame
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = ['album', 'artist', 'release_date', 'songs', 'length', 'rate']
    df['duration_min']      = df['length'].apply(parse_length)
    df['rating']            = df['rate'].apply(parse_rate)
    df['release_date']      = df['release_date'].apply(parse_year)
    df['release_date']      = df['release_date'].astype('Int64') # Permite valores enteros
    df["songs"]             = pd.to_numeric(df["songs"], errors="coerce")
    df = df[['album', 'artist', 'release_date', 'songs', 'duration_min', 'rating']]
    return df