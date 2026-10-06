try:
    with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
        alice_text = f.read()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")

import re

alice_list = re.split(r"[\W]+", alice_text)
alice_list = [w for w in alice_list if w != ""]
print(alice_list[0:100])

print("========")

sentence = "the cat saw the dog and the dog saw the cat"
words = sentence.split()

counts = {}                     # 1. start with an empty dict
for w in words:                 # 2. go through each word
    if w in counts:             # 3a. seen it before? add 1
        counts[w] += 1
    else:                       # 3b. new word? start at 1
        counts[w] = 1

print(counts)

print("========")
import re

with open("../../data/gutenberg/mansfield_park.txt", "r", encoding="utf-8") as f:
    mansfield_text = f.read()

mansfield_words = re.split(r"[\W]+", mansfield_text.lower())
mansfield_words = [w for w in mansfield_words if w != ""]

mansfield_counts = {}
for w in mansfield_words:
    if w in mansfield_counts:
        mansfield_counts[w] += 1
    else:
        mansfield_counts[w] = 1

print(mansfield_counts["fanny"])
print(len(mansfield_counts))

from collections import Counter

mansfield_counter = Counter(mansfield_words)
top10 = mansfield_counter.most_common(10)
print(top10)

print("========")
import matplotlib.pyplot as plt

#sentence_words = list(counts.keys())      # the words: labels along the bottom
#sentence_freqs = list(counts.values())    # the counts: how tall each bar is

#plt.bar(sentence_words, sentence_freqs)
#plt.title("Word Counts: The Cat and the Dog")
#plt.xlabel("Word")
#plt.ylabel("Frequency")
#plt.savefig("cat_dog_counts_w_labels.png")
#plt.show()     #open the generated bar graph

print("======")
#top_words = [pair[0] for pair in top10] # pair[0] = the word
#top_freqs = [pair[1] for pair in top10] # pair[1] = its count

#print(top_words)
#print(top_freqs)

#plt.bar(top_words, top_freqs)
#plt.title("Top 10 Words in Mansfield Park")
#plt.xlabel("Word")
#plt.ylabel("Frequency")
#plt.savefig("mansfield_top10.png")
#plt.show()

print("========")
stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t", "am"]

content_words = [w for w in mansfield_words if w not in stopwords]

#content_top10 = Counter(content_words).most_common(10)
#content_labels = [pair[0] for pair in content_top10]
#content_freqs = [pair[1] for pair in content_top10]

#plt.bar(content_labels, content_freqs)
#plt.title("Top 10 Content Words in Mansfield Park")
#plt.xlabel("Word")
#plt.ylabel("Frequency")
#plt.xticks(rotation=45)
#plt.tight_layout()    # keeps the rotated labels from getting cut off
#plt.savefig("mansfield_content_top10.png")
#plt.show()   #SHOW NICE CHART EXAMPLE

print("====Activity====")
import re

with open("../../data/gutenberg/alice.txt", "r", encoding="utf-8") as f:
    alice_text = f.read()

alice_words = re.split(r"[\W]+", alice_text.lower())
alice_words = [w for w in alice_words if w != ""]

alice_counts = {}
for w in alice_words:
    if w in alice_counts:
        alice_counts[w] += 1
    else:
        alice_counts[w] = 1

alice_counter = Counter(alice_words)
alice_top10 = alice_counter.most_common(10)
print(alice_top10)

alice_top_words = [pair[0] for pair in alice_top10] 
alice_top_freqs = [pair[1] for pair in alice_top10] 

print(alice_top_words)
print(alice_top_freqs)

stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t", "am"]

content_words = [w for w in alice_words if w not in stopwords]

alice_content_top10 = Counter(content_words).most_common(10)
alice_content_labels = [pair[0] for pair in alice_content_top10]
alice_content_freqs = [pair[1] for pair in alice_content_top10]

plt.bar(alice_content_labels, alice_content_freqs)
plt.title("Top 10 Content Words in Alice in Wonderland")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()    # keeps the rotated labels from getting cut off
plt.savefig("alice_content_top10.png")
plt.show()  
