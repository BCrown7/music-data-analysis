import pandas as pd

DATA_PATH = 'data/processed/albums_clean.csv'

def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

if __name__ == '__main__':
    df = load_data()
    print('    Forma del DataFrame limpio: ', df.shape)
    print(df.describe())
    print(df.isnull().sum())