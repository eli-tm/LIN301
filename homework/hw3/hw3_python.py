# Part One

### Numbers
#Step 1
books = 24
war_years = 10
journey_years = 10
# Step 2
total_years_away = war_years + journey_years
print(total_years_away)
# Step 3
books_per_week = books // 7
leftover_books = books % 7
print(books_per_week,  leftover_books)
# Step 4
print(type(books), type(total_years_away), type(books_per_week))

### Strings
# Step 5
hero = "Odysseus"
epithet = "that one guy in that one movie"
# Step 6
print(hero+ epithet)
print(hero, epithet)
# Step 7
homer_quote = '"the man of twists and turns."'
print(homer_quote)

### Booleans
# Step 8
years_match = war_years == journey_years
print(years_match)
# Step 9
book_number = 24
# Step 10
is_first_book = book_number == 1
is_last_book = book_number == 24
# Step 11
is_bookend = (is_first_book == True) or (is_last_book == True)
print(book_number, is_bookend)

### Book Profile
# Step 12
guess_book_number = 1
my_guess = "The beginning of the hero's journey is introduced."
is_double_digit = guess_book_number >= 10
# Step 13
print(guess_book_number, my_guess, is_double_digit)
print(type(guess_book_number), type(my_guess), type(is_double_digit))


# Part Two
    # *Set up
with open("odyssey.txt", encoding="utf-8") as f:
    text = f.read()
    words = text.split()

### Lists
# Step 14
print(len(words))
# Step 15
print(words[0:20])
# Step #16
print(words[1000:1020]) #['when', 'now', 'the', 'year', 'had', 'come', 'in', 'the', 'courses', 'of', 'the', 'seasons,', 'wherein', 'the', 'gods', 'had', 'ordained', 'that', 'he', 'should']

### Sets
# Step 17
unique_words = set(words)
print(len(unique_words))
# Step 18
ttr = len(unique_words) / len(words)
print(ttr)
# Step 19
    #The longer a text is, the more likely it is for words to repeat-- especially function words such as determiners, demonstratives, complementizers, prepositions, pronouns, etc. Odysseus is significantly longer than the first 20 words of Alice.

### Dictionaries
# Step 20
text.count("Odysseus")
# Step 21
position = text.find("Odysseus")
text[position - 150 : position + 150]
# Step