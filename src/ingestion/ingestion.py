import pandas as pd

SHEET_ID = "1ytjOjdyukhqMRVV7WfZ1LbJ_xqDaeJ98XcV1YsCVcPY"

def build_url(sheet_id: str) -> str:
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

def load_raw(sheet_id: str = SHEET_ID) -> pd.DataFrame:
    url = build_url(sheet_id)
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    df = load_raw()
    print(df.shape)
    print(df.head(3))
    print(df.tail(3))