import pickle
from sys import argv
from collections import Counter
from numpy.random import choice

MAX_WORDS = 100
START_WORD = "the"


def getWord(distribution):
    words, frequency = [], []
    total = 0
    for k, v in distribution.items():
        words.append(k)
        frequency.append(v)
        total += v
    frequency = [f / total for f in frequency]
    index = choice(range(len(words)), 1, p=frequency)[0]
    return words[index].strip()


if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Using defaults: word count = {MAX_WORDS}, start word = {START_WORD}")
        print("Usuage: ./main.py <start word> <word count>")
    else:
        START_WORD = argv[1].lower()
        MAX_WORDS = int(argv[2])

    with open("stateDict.pkl", "rb") as f:
        stateDict = pickle.load(f)

    prev_word = START_WORD
    with open("output.txt", "w") as f:
        for _ in range(MAX_WORDS):
            f.write(prev_word + " ")
            prev_word = getWord(stateDict.get(prev_word))
    print("Generated output.txt!")

