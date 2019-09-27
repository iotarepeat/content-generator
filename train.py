import string
from collections import Counter
import pandas as pd
import time
import pickle
start=time.time()

def preProcessLyrics(lyrics: str) -> list:
    """
        - Convert to lower case
        - Remove all numbers, special characters
        - return a list of all words
    """
    lyrics = lyrics.lower()
    processedWords = []
    for word in lyrics.split():
        word = "".join([c for c in word if c in string.ascii_lowercase])
        processedWords.append(word)
    return processedWords


stateDict = dict()
df = pd.read_csv("songdata.csv")
lyrics = df["text"]
lyrics = lyrics.apply(preProcessLyrics)
for text in lyrics:
    for i in range(1, len(text)):
        first, second = text[i - 1], text[i]
        stateDict.setdefault(first,Counter()).update((second,))
print("Elapsed:",time.time()-start)
with open("stateDict.pkl","wb") as f:
    pickle.dump(stateDict,f)
print(len(stateDict))
