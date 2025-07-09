for year in range(start, end + 1):
    try:
        df = get_df(year)
        corpus = get_corpus(df, year)
        tokens = get_tokens(corpus)
        st.write(f"{year}: corpus length = {len(corpus)}, tokens = {len(tokens)}")

        bow = get_bow(tokens)
        bow_df = get_bow_df(bow)

        dfs[year] = df
        corpuses[year] = corpus
        tokenses[year] = tokens
        bows[year] = bow
        bow_dfs[year] = bow_df

    except Exception as e:
        st.warning(f"❌ Failed for year {year}: {e}")
        continue
