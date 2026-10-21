# Building, Saving, and Looking
df = pd.DataFrame(rows)          # list of dicts → table (dicts = rows, keys = columns)

df.to_csv("file.csv", index=False, encoding="utf-8-sig")   # save
df = pd.read_csv("file.csv")                                # load

df.head()           # first 5 rows   (df.head(20) = first 20)
df.tail()           # last 5 rows
len(df)             # how many rows
df.columns          # the column names
df["word"]          # one column


# Filtering
df[df["word"] == "queen"]                 # equals
df[df["word"] != "under"]                 # does not equal
df[df["word"].str.endswith("ly")]         # ends with
df[df["word"].str.startswith("un")]       # starts with
df[df["word"].isin(stopwords)]            # is in a list
df[~df["word"].isin(stopwords)]           # ~ flips it: NOT in a list

df[(df["word"] == "queen") & (df["chapter"] == 8)]    # & = and
df[(df["word"] == "king") | (df["word"] == "queen")]  # | = or


# Counting and Sorting
df["word"].value_counts()                  # count each value, most common first
df["word"].value_counts().head(10)         # top 10
df["word"].value_counts(normalize=True)    # proportions instead of counts
df["chapter"].value_counts().sort_index()  # sort by the label (1, 2, 3...)

df["word"].nunique()                       # how many unique values (types)
df["length"].mean()                        # average
df["length"].max()                         # biggest

df.sort_values("length", ascending=False)  # sort rows, biggest first
df.drop_duplicates("word")                 # keep one row per word


# New Columns, Grouping, and Plotting
import matplotlib.pyplot as plt               # needed for plotting

df["length"] = df["word"].str.len()           # new column from a string method
df["is_ly"] = df["word"].str.endswith("ly")   # new True/False column
df["is_she"] = df["word"] == "she"            # new True/False column from a test
df["text"] = "alice"                          # same value in every row

books = pd.concat([df1, df2], ignore_index=True)   # stack two tables

books.groupby("text").size()                  # rows per group
books.groupby("text")["length"].mean()        # average per group
books.groupby("text")["word"].nunique()       # types per group
books.groupby("text")["is_ly"].mean() * 1000  # True/False mean = rate per 1,000

rate = books.groupby("text")["is_ly"].mean() * 1000
rate.plot(kind="bar")                         # bar chart (.plot() alone = line chart)
plt.title("Title")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.show()