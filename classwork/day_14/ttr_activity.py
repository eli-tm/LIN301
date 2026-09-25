austen_opening = ["it", "is", "a", "truth", "universally", "acknowledged", "that", "a",
                   "single", "man", "in", "possession", "of", "a", "good", "fortune",
                   "must", "be", "in", "want", "of", "a", "wife"]

bronte_opening = ["there", "was", "no", "possibility", "of", "taking", "a", "walk",
                   "that", "day", "we", "had", "been", "wandering", "in", "the",
                   "leafless", "shrubbery", "an", "hour", "in", "the", "morning"]

   # calculate length, unique words, and ttr of each opening
austen_tokens = len(austen_opening)
austen_types = len(set(austen_opening))
austen_ttr = austen_types/austen_tokens
print(austen_tokens, austen_types, austen_ttr)

bronte_tokens = len(bronte_opening)
bronte_types = len(set(bronte_opening))
bronte_ttr = bronte_types/bronte_tokens
print(bronte_tokens, bronte_types, bronte_ttr)

   # comparing the passages
austen_words = set(austen_opening)
bronte_words = set(bronte_opening)

print(austen_words & bronte_words)   # which words appear in both; function words!
print(austen_words - bronte_words)   # words unique to austen

   # back to lists
print(austen_opening.count("a"))  #how many times "a" appears in austen opening