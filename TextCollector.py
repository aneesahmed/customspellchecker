# coding=utf-8
from glob import glob
from nltk.corpus.reader import XMLCorpusReader
from nltk.corpus import XMLCorpusReader
import os, os.path
import nltk.data
from nltk import Text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os
####################################33

def buildWordList(corpus_root):
    stop_words = set(stopwords.words('english'))

    fileids = '.xml'
    xmlreader = XMLCorpusReader(corpus_root, fileids)
    #print(xmlreader)
    termList = []
    for file in os.listdir(corpus_root):
        if file.endswith(".xml"):
            terms =Text(xmlreader.words(file))
            termList.append(terms)

    #print(termList)
    stop_words = set(stopwords.words('english'))
    terms = word_tokenize(str(termList))
    newTerms  = []
    for w in terms:
        if (w not in (stop_words)  and w.isalpha() ):
            newTerms.append(w)
    #print(newTerms)
    return (newTerms)

#print(buildWordList(corpus_root))