import DoublePropagation
import SpellChecker
import nltk
from nltk.corpus import words
from nltk.corpus import stopwords
#import re, collections
import time
import sys
import double2
import operator

orig_stdout = sys.stdout
f = file('/home/sewwandi/outFinalcheck2.txt', 'w')
sys.stdout = f

start_time = time.time()

features = double2.controller("NotebookCooler.txt")
endtime=time.time()
totalTime= endtime-start_time
# sorted(features.values())
# print features
sorted_x = sorted(features.items(), key=operator.itemgetter(1))
print sorted_x
#print len(features)
print totalTime
sys.stdout = orig_stdout
f.close()
#stop_words = set(stopwords.words("english"))
# cleaned_text = filter(lambda x: x not in stop_words, features)
# print cleaned_text
# print len(cleaned_text)
# for row in sentence:
#     doc=""
#     for word in nltk.word_tokenize(row):
#         if not word in words.words()  :
#             doc=doc+SpellChecker.correct(word)+" "
#         else:
#             doc=doc+word+" "
#
#     print doc

