
import jieba
import os
import nltk
from nltk.collocations import *

file_path = r'[enter local directory here]'
#this loop loops through all the txt files in the directory 
for filename in os.listdir(file_path):
    if filename.endswith(".txt"):
       file = open("{}/{}".format(file_path,filename),encoding="utf8")
       text = file.read()
       file.close()
       #this line uses jieba to read Chinese words and segment Chinese into two-character words  
       seg_list = jieba.cut(text, cut_all=False)
       #this line uses NLTK's built-in bigram collocation function to find characters highly associated with each other
       bigram_measures = nltk.collocations.BigramAssocMeasures()
       #this line allows you to specify the keyword you are looking for    
       keyword_filter = lambda *w: '[enter keyword here]' not in w
       finder = BigramCollocationFinder.from_words(seg_list)
       finder.apply_ngram_filter(keyword_filter)
       bigrams=finder.nbest(bigram_measures.likelihood_ratio, 5)
       print(bigrams)
