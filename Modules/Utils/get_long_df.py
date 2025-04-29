def get_long_df():
  url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/refs/heads/main/Data/df_long.csv"
  df = pd.read_csv(url, index_col="Unnamed: 0")
  return df