import nltk
import sys
from nltk.tokenize import TweetTokenizer
from nltk.metrics import *

# open linux dictionary text file and initialize it as a set
dictionary = set(line.strip() for line in open('dict.txt', 'r'))

# ('drum' in dictionary) returns true
# ('nxjgpwe' in dictionary) returns false

# open our corpus specified by commandline argument
lines = open(sys.argv[1], "r").readlines()
# strip newline characters
lines = map(lambda x: x.strip(), lines)

tokenizer = TweetTokenizer()

# load all lines into a single string called corpus
corpus = ''
for line in lines:
    corpus += line + ' '

# tokenize the corpus using nltk's tokenizer
tokens = tokenizer.tokenize(corpus)

mispellings = ['']
for token in tokens:
    if (token not in dictionary) and (len(token) != 1) and (token not in mispellings):
        mispellings.append(token)

for word in mispellings:
    output = word
    for ref in dictionary:
        if(edit_distance(word, ref) < 2):
            output += ref + ' '