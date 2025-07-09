def get_corpus(df, year):
    """
    Extracts and cleans the text corpus from Title, KeyWords, and Abstract columns.
    """
    text_parts = [df['Title'], df['Abstract']]
    if year != 2015:
        text_parts.insert(1, df['KeyWords'])

    text = ", ".join([
        str(t).lower() if isinstance(t, str) else ""
        for part in text_parts for t in part
    ])

    # Basic punctuation and formatting cleanup
    text = text.replace(";", ",").replace(".", ",")
    text = text.replace("4,0", "4.0").replace("5,0", "5.0")

    return text
