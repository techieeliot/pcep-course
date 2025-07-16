# Levenshtien Distance

# Bean and Mean means one changes needs to occur, so the LV distance is 1

from fuzzywuzzy import fuzz
from pandas import DataFrame as df


def compare_strings(string1, string2):
    """
    Compare two strings using Levenshtein distance and return the similarity ratio.
    """
    ratio = fuzz.ratio(string1, string2)
    print(f"Comparing '{string1}' with '{string2}'")
    print(f"Similarity ratio: {ratio}%")
    return ratio

compare_strings("BeanPath", "The Bean Path")

dict1 = {"name": ["Eliot", "Jude", "David"]}
dict2 = {"name": ["Ranjita", "Norah", "David", "Eliot"]}

# play around with pandas DataFrame
df1 = df(dict1)
df2 = df(dict2)



