def get_df(file_year):
  base_url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/refs/heads/main/Data/CP_{}.csv"
  file_name=base_url.format(file_year)
  df = pd.read_csv(file_name, index_col="Unnamed: 0")
  if file_year!=2015:
    df["Paper"] = df["Title"].str.lower()+ ", " \
                   + df["KeyWords"].str.lower() + ", " \
                   + df["Abstract"].str.lower()+", "
  else:
    df["Paper"] = df["Title"].str.lower()+ ", " \
                + df["Abstract"].str.lower()+", "
  return df