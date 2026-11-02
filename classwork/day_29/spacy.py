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