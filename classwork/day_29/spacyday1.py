import sys
sys.path.append("../../data")
from lin301 import *

alice = book_to_df("alice.txt", "Alice")
alice = add_columns(alice, stopwords)
print(alice.head())

ly_words = alice[alice["is_ly"]]
print(ly_words.groupby("word").size().sort_values(ascending=False).head(20))

print("===Activity 1====")
say_forms = alice[alice["word"].isin(['go', 'goes', 'went', 'going', 'gone'])]
print(say_forms.groupby("word").size())

# go is the lemma of went

print("====SpaCy!!====")
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("Alice quickly went down the hole, but the only way out was very ugly.")

for token in doc:
    print(token.text)

print("====Making a DF with Spacy====")
alice_sp = book_to_spacy_df("alice.txt", "Alice", nlp)
print(alice_sp.head())

# how many -ly words are adverbs?
alice_sp["is_ly"] = alice_sp["word"].str.endswith("ly")
alice_sp[alice_sp["is_ly"]].groupby("pos").size().sort_values(ascending=False)

# which -ly words are NOT adverbs?
not_adv = alice_sp[alice_sp["is_ly"] & (alice_sp["pos"] != "ADV")]
not_adv.groupby("word").size().sort_values(ascending=False)

# counting lemmas
content = alice_sp[~alice_sp["is_stop"]]
content.groupby("lemma").size().sort_values(ascending=False).head(10)

# editing a label
alice_sp.loc[[2, 3], "pos"] = "NOUN"
alice_sp.head()

print("====Activity Compare 2 Books====")
# creating mansfield as a spacy df:
mp_sp = book_to_spacy_df("mansfield_park.txt", "Mansfield", nlp)
print(mp_sp.head())

# adding columns
alice_sp = book_to_spacy_df("alice.txt", "Alice", nlp)
print(alice_sp.head())
