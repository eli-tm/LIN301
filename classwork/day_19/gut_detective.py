print("====King in Yellow====")

with open("../../data/gutenberg/king_yellow.txt", "r", encoding="utf-8") as f:  #imports The King in Yellow text file as f
    king_lines = f.readlines()      #creates the variable king_lines as a list of every line in king_yellow.txt

while not king_lines[0].startswith("                      THE REPAIRER OF REPUTATIONS"):       #the heading of the first chapter
    king_lines = king_lines[1:]     #gets rid of each line until it reaches the line that starts with the heading
king_lines = king_lines[1:]         #gets rid of the heading

print(king_lines[0:5])      #double checking the above code worked

while not king_lines[-1].startswith("*** END"):
    king_lines = king_lines[:-1]    #chop off the last line until it reaches *** END
king_lines = king_lines[:-1]        #chop off the *** END line itself

print(king_lines[-5:])      #double checking the above code worked

king_text = "".join(king_lines)     #joins all the lines into 1 text instead of a list

import re       #importing RegEx

king_words = re.split(r"[\W]+", king_text.lower())      #splitting the text word-by-word and making all characters lowercase
king_words = [w for w in king_words if w != ""]      #gets rid of all empty words

print(king_words[0:200])        #sampling the cleaned text!


print("====The Wizard of Oz====")
with open("../../data/gutenberg/oz.txt", "r", encoding="utf-8") as f:
    oz_lines = f.readlines()

while not oz_lines[0].startswith("The Cyclone"):    #The heading of the first chapter
    oz_lines = oz_lines[1:]     
oz_lines = oz_lines[1:]         

print(oz_lines[0:5])

while not oz_lines[-1].startswith("*** END"):
    oz_lines = oz_lines[:-1]    
oz_lines = oz_lines[:-1]        

oz_text = "".join(oz_lines)

print(oz_lines[-5:])

import re

oz_words = re.split(r"[\W]+", oz_text.lower())
oz_words = [w for w in oz_words if w != ""]

print(oz_words[0:200])

print("====Explore====")
king_tokens = len(king_words)       #calculates the total number of words
king_types = len(set(king_words))   #calculates the number of unique words
king_ttr = king_types/king_tokens   #calculates the total number of words divided by unique words to get the token-type ratio

oz_tokens = len(oz_words)           #repeating the above for the second novel
oz_types = len(set(oz_words))
oz_ttr = oz_types/oz_tokens

#printing the results:
print("The King in Yellow has", king_tokens, "words,", king_types, "unique words, and a", king_ttr, "TTR.")
print("The Wizard of Oz has", oz_tokens, "words,", oz_types, "unique words, and a", oz_ttr, "TTR.")
print("     The King in Yellow has a richer vocabulary.")

king_ttr_10000 = len(set(king_words[:10000])) / len(king_words[:10000])     #calculates the TTR of the first 10,000 words of king_words
oz_ttr_10000 = len(set(oz_words[:10000])) / len(oz_words[:10000])           #calculates the TTR of the first 10,000 words of oz_words

#printing the results:
print("The King in Yellow TTR (10,000 words):", king_ttr_10000)
print("The Wizard of Oz TTR (10,000 words):", oz_ttr_10000)
print("     The King in Yellow has a richer vocabulary within 10,000 words.")

king_wc = 0                         #creating a word count of 0
for w in king_words:                #for each word,
    king_wc += len(w)               #increase the word count by the length of the word
king_awl = king_wc/len(king_words)  #divide the word count by the total number of words to get the average word length

oz_wc = 0                           #repeat for the second novel
for w in oz_words:
    oz_wc += len(w)
oz_awl = oz_wc/len(oz_words)

#printing the results:
print("The King in Yellow has an average word length of", king_awl, "characters.")
print("The Wizard of Oz has an average word length of", oz_awl, "characters.")

print("========")
from collections import Counter
import matplotlib.pyplot as plt

king_freqs = [pair[1] for pair in Counter(king_words).most_common()]
king_ranks = range(1, len(king_freqs) + 1)    # 1, 2, 3, ... up to the number of words

#plt.plot(king_ranks, king_freqs)
#plt.title("Rank vs. Frequency")
#plt.xlabel("Rank")
#plt.ylabel("Frequency")
#plt.xscale("log")
#plt.yscale("log")
#plt.show()

oz_freqs = [pair[1] for pair in Counter(oz_words).most_common()]
oz_ranks = range(1, len(oz_freqs) + 1)    # 1, 2, 3, ... up to the number of words

#plt.plot(oz_ranks, oz_freqs)
#plt.title("Rank vs. Frequency")
#plt.xlabel("Rank")
#plt.ylabel("Frequency")
#plt.xscale("log")
#plt.yscale("log")
#plt.show()

print("====LY====")
#words ending in -ly per 1,000 words
king_ly = set()             #creates an empty set
for w in king_words:        #for each word in king_words,
    if w.endswith("ly"):    #if the word ends in "ly"
        king_ly.add(w)      #add the word to the set
#printing the results:
print("The King in Yellow has", len(king_ly), "words that end in -ly.")
king_ly_rate = len(king_ly) / len(king_words) * 1000
print("The King in Yellow has", king_ly_rate, "-ly words per 1000 words.")

oz_ly = set()               #repeat for the second novel
for w in oz_words:
    if w.endswith("ly"):
        oz_ly.add(w)
#printing the results:
print("The Wizard of Oz has", len(oz_ly), "words that end in -ly.")
oz_ly_rate = len(oz_ly) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_ly_rate, "-ly words per 1000 words.")

print("====TION====")
king_ion = set()
for w in king_words:
    if w.endswith("ion"):
        king_ion.add(w)
print("The King in Yellow has", len(king_ion), "words that end in -ion")
king_ion_rate = len(king_ion) / len(king_words) * 1000
print("The King in Yellow has", king_ion_rate, "-ion words per 1000 words.")

oz_ion = set()
for w in oz_words:
    if w.endswith("ion"):
        oz_ion.add(w)
print("The Wizard of Oz has", len(oz_ion), "words that end in -ion")
oz_ion_rate = len(oz_ion) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_ion_rate, "-ion words per 1000 words.")

print("====ABLE====")
king_able = set()
for w in king_words:
    if w.endswith("able"):
        king_able.add(w)
print("The King in Yellow has", len(king_able), "words that end in -able")
king_able_rate = len(king_able) / len(king_words) * 1000
print("The King in Yellow has", king_able_rate, "-able words per 1000 words.")

oz_able = set()
for w in oz_words:
    if w.endswith("able"):
        oz_able.add(w)
print("The Wizard of Oz has", len(oz_able), "words that end in -able")
oz_able_rate = len(oz_able) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_able_rate, "-able words per 1000 words.")

print("====ING====")
king_ing = set()
for w in king_words:
    if w.endswith("ing"):
        king_ing.add(w)
print("The King in Yellow has", len(king_ing), "words that end in -ing")
king_ing_rate = len(king_ing) / len(king_words) * 1000
print("The King in Yellow has", king_ing_rate, "-ing words per 1000 words.")

oz_ing = set()
for w in oz_words:
    if w.endswith("ing"):
        oz_ing.add(w)
print("The Wizard of Oz has", len(oz_ing), "words that end in -ing")
oz_ing_rate = len(oz_ing) / len(oz_words) * 1000
print("The Wizard of Oz has", oz_ing_rate, "-ing words per 1000 words.")

print("king -ion words:", king_ion)
print("oz -ion words:", oz_ion)
print("=====")
print("king -able words:", king_able)
print("oz -able words:", oz_able)
print("=====")
print("king -ing words:", king_ing)
print("oz -ing words:", oz_ing)

print("====Dialogue====")
king_cleanlines = [line.strip().lower() for line in king_lines]     #strip line breaks and empty spaces and make all lowercase
king_nonempty = [line for line in king_cleanlines if line != ""]    #gets rid of empty lines

dialoguemarker = "“"

king_dialogue = [line for line in king_nonempty if dialoguemarker in line]
print("The King in Yellow has", len(king_dialogue), "lines of dialogue.")
king_dialoguepercentage = len(king_dialogue) / len(king_lines)
print("The King in Yellow dialogue percentage:", king_dialoguepercentage)


oz_cleanlines = [line.strip().lower() for line in oz_lines]         #repeat for second novel
oz_nonempty = [line for line in oz_cleanlines if line != ""]    

oz_dialogue = [line for line in oz_nonempty if dialoguemarker in line]
print("The Wizard of Oz has", len(oz_dialogue), "lines of dialogue.")
oz_dialoguepercentage = len(oz_dialogue) / len(oz_lines)
print("The Wizard of Oz percentage:", oz_dialoguepercentage)

print("====CommonWords====")
stopwords = ["the", "to", "and", "of", "a", "her", "i", "in", "was", "it",
             "she", "he", "be", "that", "you", "not", "had", "as", "his", "for",
             "with", "is", "have", "but", "at", "so", "all", "my", "been", "him",
             "on", "by", "could", "would", "very", "no", "what", "which", "they",
             "were", "there", "me", "an", "must", "this", "said", "from", "or",
             "will", "any", "much", "than", "such", "their", "them", "if", "do",
             "did", "one", "when", "your", "more", "are", "we", "who", "up",
             "out", "down", "into", "s", "t", "am", "then"]

king_counts = {}                #create empty dictionary
for w in king_words:            #for each word in king_words
    if w in king_counts:        #if the word is in the dictionary
        king_counts[w] += 1     #increase the value by 1
    else:                       #if the word is not in the dictionary
        king_counts[w] = 1      #do not increase the value 

king_counter = Counter(king_words)          #counts all the word appearances in king_words
king_top10 = king_counter.most_common(10)   #creates a variable of the 10 highest valued items
print(king_top10)

king_top_words = [pair[0] for pair in king_top10]       #pairs words and frequencies into a dictionary
king_top_freqs = [pair[1] for pair in king_top10] 

print(king_top_words)
print(king_top_freqs)

king_content_words = [w for w in king_words if w not in stopwords]      #adds words to variable if the words are not within the list stopwords

king_content_top10 = Counter(king_content_words).most_common(10)        #counts all the word appearances in king_content_words
king_content_labels = [pair[0] for pair in king_content_top10]          #pairs words and frequencies into a dictionary
king_content_freqs = [pair[1] for pair in king_content_top10]


oz_counts = {}                  #repeat for second novel
for w in oz_words:
    if w in oz_counts:
        oz_counts[w] += 1
    else:
        oz_counts[w] = 1

oz_counter = Counter(oz_words)
oz_top10 = oz_counter.most_common(10)
print(oz_top10)

oz_top_words = [pair[0] for pair in oz_top10] 
oz_top_freqs = [pair[1] for pair in oz_top10] 

print(oz_top_words)
print(oz_top_freqs)

oz_content_words = [w for w in oz_words if w not in stopwords]

oz_content_top10 = Counter(oz_content_words).most_common(10)
oz_content_labels = [pair[0] for pair in oz_content_top10]
oz_content_freqs = [pair[1] for pair in oz_content_top10]

print("The top 10 words in The King in Yellow are", king_content_labels, "with counts of", king_content_freqs)
print("The top 10 words in The Wizard of Oz are", oz_content_labels, "with counts of", oz_content_freqs)

print("====Plotting====")
import matplotlib.pyplot as plt

# bar chart for the top 10 content words of both novels
#plt.bar(king_content_labels, king_content_freqs, label="The King in Yellow")
#plt.bar(oz_content_labels, oz_content_freqs, label="The Wizard of Oz")
#plt.legend()
#plt.title("Top 10 Content Words in The King in Yellow and The Wizard of Oz")
#plt.xlabel("Word")
#plt.ylabel("Frequency")
#plt.xticks(rotation=45)
#plt.tight_layout()    # keeps the rotated labels from getting cut off
#plt.savefig("hw4_content_top10.png")
#plt.show()

# zipf law plot for the ranks and frequencies of both novels
plt.plot(king_ranks, king_freqs, label="The King in Yellow")
plt.plot(oz_ranks, oz_freqs, label="The Wizard of Oz")
plt.legend()
plt.title("Rank vs. Frequency for The King in Yellow and The Wizard of Oz")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.xscale("log")
plt.yscale("log")
plt.savefig("zipf_hw4.png")
plt.show()
