#word = input("Give me an English noun, in the singular: ")
    #remove comment above to play!
word = "dog"

sibilants = ["s", "z", "ʃ", "ʒ", "tʃ", "dʒ"] 
voiceless = ["p", "t", "k", "f", "θ"]

if word[-1] in sibilants:
    plural = word + "ɪz"
elif word[-1] in voiceless:
    plural = word + "s"
else:
    plural = word + "z"

print("Plural: ", plural)

print("=========")
try:
    print(my_age)
except NameError:
    print("That variable doesn't exist yet!")

#Other errors: NameError, FileNotFoundError, TypeError
print("=========")
charlotte = ['The Professor', 'Jane Eyre', 'Shirley', 'Villette']
for title in charlotte: 
    print(title)

print("====Activity====")
words = ["phoneme", "phrase", "morpheme", "reconstruction", "index"]
for term in words:
    print("the word", term, "has", len(term), "letters")