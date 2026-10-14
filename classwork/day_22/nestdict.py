print("====Nested Lists Review Activity====")

words = ["zombie", "ghoul", "ghost", "vampire"]
begins_with_g = [False, True, True, False]
rhymes_with_most = [False, False, True, False]

length = [len(w) for w in words] #list comprehension

halloween = {}
for w, g, r, l in zip(words, begins_with_g, rhymes_with_most, length):
    halloween[w] = [g, r, l]
print(halloween)

print("====Nested Dictionaries====")

phonemes = ["p", "b", "t", "d", "k", "g"]
place    = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar"]
manner   = ["stop"] * 6
voice    = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced"]

#dictionary comprehension:
stops = {ph: {"place": pl, "manner": m, "voice": v} for ph, pl, m, v in zip(phonemes, place, manner, voice)}

for ph, features in stops.items():
    print(ph, features['voice']) #print only the voicing 

for ph, features in stops.items():          #print only the voiced phonemes
    if features["voice"] == "voiced":
        print(ph)

print("====Activity====")

#add "aspirated" as a new key
for ph, features in stops.items():
    if features["voice"] == "voiceless":
        features["aspirated"] = True
    else:
        features["aspirated"] = False

print(stops)

print("========")
place_counts = {}

for ph, features in stops.items():
    pl = features["place"]
    if pl in place_counts:
        place_counts[pl] += 1
    else:
        place_counts[pl] = 1

print(place_counts)

print("====Activity====")
consonant =  ["p", "b", "t", "d", "k", "g", "s", "z", "m", "n", "l", "r", "w", "j", "h"]
place = ["bilabial", "bilabial", "alveolar", "alveolar", "velar", "velar", "alveolar", "alveolar", "bilabial", "alveolar", "alveolar", "alveolar", "labial-velar", "palatal", "glottal"]
manner = ["stop", "stop", "stop", "stop", "stop", "stop", "fricative", "fricative", "nasal", "nasal", "lateral", "trill", "glide", "glide", "fricative"]
voice = ["voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiceless", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiced", "voiceless"]

#build a nested dict:
consonants = {con: {"place": pl, "manner": m, "voice": v} for con, pl, m, v in zip(consonant, place, manner, voice)}
print(consonants)

#print the place of [j]
print("j is", consonants["j"]["place"])

#print only voiceless consonants
for con, features in consonants.items():        
    if features["voice"] == "voiceless":
        print(con)

#count how many consonants there are of each manner (accidentally did place)
for con, manner in consonants.items():
    pl = features["place"]
    if pl in place_counts:
        place_counts[pl] += 1
    else:
        place_counts[pl] = 1

print(place_counts)
