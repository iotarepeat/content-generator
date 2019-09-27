# Purpose:
- This is a quick script to generate some gibberish words.
- It can be used as placeholder content.

# How it works?
- It uses a dataset of song lyrics
- The program then creates a Markov model of the available lyrics
- Using two parameters inital word (default=The) and max words (default=100) the program then generates text by iterating over trained markov model
- The output is written to output.txt
# Datasets used:
- https://www.kaggle.com/mousehead/songlyrics