# You have been provided two massive .tsv (tab-separated 
# values) files, named “names.tsv” and “titles.tsv”. The names
# file lists notable individuals in the cinema industry along with
# other relevant information, including a list of their notable
# works, called “knownForTitles”. This column has a comma-
# separated list of titles, listed under a titleID in format 
# “ttXXXXXXX” (ex. tt0816692 corresponds to Interstellar). 
# This column lists films in order of notoriety, with the first
# listed ID corresponding to the title that the actor is 
# (arguably) best known for.
# The titles file holds the title of (almost) all films, along with
# its corresponding title ID, which match to the IDs in the actor
# dataset, along with other data. Given these separate 
# datasets for movies and actors, merge the datasets so that
# an actor’s row has their name, notable works as movie titles,
# and other given attributes.
# This merged dataset should be a .csv (comma-separated
# values) containing ONLY living actors or actresses (hint: all
# living actors/actresses were born after 1925) whose
# birth/death years are known, along with the title of their best
# known work. Duplicate rows may exist in the dataset, which
# should not be included in your submission. Only include the
# columns “primaryName”, “birthYear”, and “primaryTitle” 
# in your final submission. An example of the first five correct rows
# are included below.
# https://imgur.com/a/O4zbA0f
# To submit, utilize the following curl command (Mac users
# use Terminal, Windows users use Command Prompt, NOT
# Powershell) curl -X POST -F "file=@{YOUR FILENAME GOES HERE}" https://movies-eval-dot-
# chunin.uc.r.appspot.com/upload-csv

import pandas as pd

titles_df = pd.read_csv("src\\Data Manipulation\\Movie Merging\\titles.tsv", sep="\\t")
titles_df = titles_df.set_index(["tconst"])

names_df = pd.read_csv("src\\Data Manipulation\\Movie Merging\\names.tsv", sep="\\t")

names_df = names_df.drop_duplicates()
names_df = names_df[names_df["primaryProfession"].str.contains("actor|actress")]

names_df[["birthYear", "deathYear"]] = names_df[["birthYear", "deathYear"]].replace(to_replace="\\N", value=0)
names_df = names_df[(names_df["birthYear"].astype(int) > 1925) & (names_df["deathYear"].astype(int) == 0) & (names_df["knownForTitles"] != "\\N")]

names_df["knownForTitles"] = names_df["knownForTitles"].apply(lambda x: str(x).split(",")[0])
names_df["knownForTitles"] = names_df["knownForTitles"].apply(lambda x: titles_df.xs(x)["primaryTitle"])

merged_df = names_df[["primaryName", "birthYear", "knownForTitles"]]
merged_df = merged_df.rename(columns={"knownForTitles":"primaryTitle"})

merged_df.to_csv("Data Manipulation\\Movie Merging\\movie_merging.csv", index=False)