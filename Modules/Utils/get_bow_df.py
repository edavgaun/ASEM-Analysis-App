def get_bow_df(bow):
  df_kw=pd.DataFrame({"Word":bow.keys(), "frq":bow.values()}).sort_values("frq", ascending=False
                                                                                ).reset_index(drop=True)
  return df_kw