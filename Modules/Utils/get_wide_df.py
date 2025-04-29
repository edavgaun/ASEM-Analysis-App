def get_wide_df():
  url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/refs/heads/main/Data/data_full.csv"
  df = pd.read_csv(url)
  return df