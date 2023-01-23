
import jieba
import os
import nltk
from nltk.collocations import *

file_path = r'C:\Users\ashle\OneDrive\Documents\dh\chronological database\cases\case 5\corpus'
for filename in os.listdir(file_path):
    if filename.endswith(".txt"):
       file = open("{}/{}".format(file_path,filename),encoding="utf8")
       text = file.read()
       file.close()
       seg_list = jieba.cut(text, cut_all=False)
       #print("Full Mode: " + "/ ".join(seg_list))  # 全模式
       bigram_measures = nltk.collocations.BigramAssocMeasures()
       keyword_filter = lambda *w: '小說' not in w
       finder = BigramCollocationFinder.from_words(seg_list)
       finder.apply_ngram_filter(keyword_filter)
       bigrams=finder.nbest(bigram_measures.likelihood_ratio, 5)
       print(bigrams)