import sys
import re
import difflib

# open linux dictionary text file and initialize it as a set
dictionary = set(line.strip() for line in open('en_US.txt', 'r'))

# ('drum' in dictionary) returns true
# ('nxjgpwe' in dictionary) returns false

# open our corpus specified by commandline argument
lines = open(sys.argv[1], "r").readlines()
# strip newline characters
lines = map(lambda x: x.strip(), lines)

#tokenizer = TweetTokenizer()

# load all lines into a single string called corpus
corpus = ''
for line in lines:
    corpus += line + ' '

# tokenize the corpus using our regex
tokens = re.findall(r"[\w']+|[.,!?;:()]",corpus)

mispellings = []
for token in tokens:
    if (token not in dictionary) and (token.lower() not in dictionary) and (len(token) != 1 and token not in ['a', 'o', 'A', 'I', 'O']) and (token not in mispellings):
        mispellings.append(token)

for word in mispellings:
    matches = difflib.get_close_matches(word, dictionary)
    recommendations = ''
    for match in matches:
    	recommendations += match + ', '
    print (word + ': ' + recommendations[0:len(recommendations)-2])
