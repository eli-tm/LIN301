orwell_novels = ["Animal Farm", "Nineteen Eighty-Four", "Burmese Days", "Keep the Aspidistra Flying", "Coming Up for Air"]
pub_year = [1945, 1949, 1934, 1936, 1939]
#task 1: print names of first and last novel
print(orwell_novels[-1], orwell_novels[0])
#task 2: find position of Burmese Days and find corresponding publication year
days_index = orwell_novels.index("Burmese Days")
print(days_index)
print(pub_year[days_index])
#task 3: find novel published in 1936
index_1936 = pub_year.index(1936)
print(orwell_novels[index_1936])