import sys
sys.path.append("../../data")
from lin301 import *

import spacy
nlp = spacy.load("en_core_web_sm")

alice_svo = book_to_svo_df("alice.txt", "Alice", nlp)

### WordNet !
# synsets: sets of words that share meanings (hyponym/hypernym, meronyms, antonyms)

import nltk
nltk.download("wordnet")
from nltk.corpus import wordnet as wn

wn.synsets("bat")

## Activity 1:
# how many meanings does "bank, duck, and soup" have?:
for word in ["bank", "duck", "soup"]:
    print(word, len(wn.synsets(word)),
          len(wn.synsets(word, pos=wn.NOUN)),
          len(wn.synsets(word, pos=wn.VERB)))

for synset in wn.synsets("soup", pos=wn.NOUN):
    print(synset.name(), "→", synset.definition())