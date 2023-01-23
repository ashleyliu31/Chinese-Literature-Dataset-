import nltk
import jieba
import os
import nltk
from nltk.collocations import *


file_path = r'[enter local directory here]'
#this is a list of punctuations and words to be ignored in the colocation calculations
stop_words= [",","》","《","·","\n","、","〕","!","。","：","！", "【","】","〈","〉","，","'」","「","？","（","□","）","“","”","』","<","乎","哉","也","是","乎","（","」"," ","豈",
             "；","焉","『","矣","」","「","曰","矣","曰",">","/",")","\u3000"]
def ngram_tokenize(input_string, n=2):
    return [input_string[i:i+n] for i in range(len(input_string)-(n-1))]

for filename in os.listdir(file_path):
    if filename.endswith(".txt"):
       file = open("{}/{}".format(file_path,filename),encoding="utf8")
       text = file.read()
       file.close()
       seg_list = ngram_tokenize(text)
       seg_list = [str(word) for word in seg_list if not str(word) in stop_words]
       bigram_measures = nltk.collocations.BigramAssocMeasures()
       #this line allows you to specify the keyword you are looking for in the colocation search
       keyword_filter = lambda *w: '[enter keyword]' not in w
       finder = BigramCollocationFinder.from_words(seg_list)
       finder.apply_ngram_filter(keyword_filter)
       score=finder.score_ngrams(bigram_measures.likelihood_ratio)
       print(score)