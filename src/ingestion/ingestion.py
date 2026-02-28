import pandas as pd

SHEET_ID = "1ytjOjdyukhqMRVV7WfZ1LbJ_xqDaeJ98XcV1YsCVcPY"

def build_url(sheet_id: str) -> str:
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

def load_raw(sheet_id: str = SHEET_ID) -> pd.DataFrame:
    url = build_url(sheet_id)
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    # Carga de datos sin procesar
    df = load_raw()
    print(f'\n    Forma del DataFrame: {df.shape}')
    print(df.sample(2)) # Ejemplares de muestra
    print(df.tail(1))   # Verificación del último agregado
    print('-' * 80)
    
    # Importacion de función 'cleaning' para limpieza de datos
    from cleaning import clean_data

    df_raw = load_raw()
    df_clean = clean_data(df_raw)

    print(df_clean.sample(5))
    print(df_clean.dtypes)
    
    # Guardar el DataFrame limpio en un archivo CSV
    output_path = 'data/processed/albums_clean.csv'
    df_clean.to_csv(output_path, index=False)
    print(f'\n    Dataset limpio y guardado en: {output_path}')