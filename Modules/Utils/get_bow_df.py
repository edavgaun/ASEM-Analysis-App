import pandas as pd

def get_bow_df(bow):
    df_kw = pd.DataFrame({"Word": list(bow.keys()), "frq": list(bow.values())})
    df_kw = df_kw.sort_values("frq", ascending=False).reset_index(drop=True)
    return df_kw
