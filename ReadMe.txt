Design Aproach
-----------------
From folder of english59 ( from assignment #1), our buildWordList function  (from TextCollector.py) read all xmls
and create a list (dynamic array) of words.

Then spellsuggest.py contain different function for processing the list.

This start with processing text using Counter function, which
automatically create a dictionary name WORDS which contain word along with its frequency ({word:nn})

How to Use:
----------
for testing, we have added a python file spellcheck.py
which call corrections function that return correct word or candidates words.

Dependancy:
----------
english59 (folder of 0-quran.rar not included due to size limit)
Python 3.6
nltk (using pip install nltk)