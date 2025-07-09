from Modules.Utils.get_df import get_df
from Modules.Utils.get_corpus import get_corpus
from Modules.Utils.get_tokens import get_tokens
from Modules.Utils.get_bow import get_bow
from Modules.Utils.get_bow_df import get_bow_df

def get_bows_dict(start=2015, end=2024):
    dfs, corpuses, tokenses, bows, bow_dfs = {}, {}, {}, {}, {}

    for year in range(start, end + 1):
        try:
            dfs[year] = get_df(year)
            corpuses[year] = get_corpus(dfs[year], year)
            tokenses[year] = get_tokens(corpuses[year])
            bows[year] = get_bow(tokenses[year])
            bow_dfs[year] = get_bow_df(bows[year])
        except Exception as e:
            continue

    return dfs, corpuses, tokenses, bows, bow_dfs
