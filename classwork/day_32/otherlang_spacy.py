import nltk
import sys
sys.path.append("../../data")
from lin301 import *

import unicodedata
import spacy
nlp = spacy.load("en_core_web_sm")

# unicode gives every character in every writing system its own number and name

### Activity 1: Unicode
# print the name of each character in the word naive
naive = "naïve"
print([unicodedata.name(c) for c in naive])

# print the number and name of each character
for c in "ñßжك":
    print(c, ord(c), unicodedata.name(c))

# make the enje character, its length, and T/F if equals enje
n_tilde = "n\u0303"
print(len(n_tilde), unicodedata.normalize("NFC", n_tilde) == "ñ")

##### Encodings:
# utf-8 stores every unicode character

# downloaded nlp of french and italian langs:
nlp_fr = spacy.load("fr_core_news_sm")
nlp_it = spacy.load("it_core_news_sm")

#### Activity 2: Morphology
it_doc = nlp_it("Alice cominciava a sentirsi stanca.")

#print each token's text, lemma, POS, and morphology:
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.morph)
