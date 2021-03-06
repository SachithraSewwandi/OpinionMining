import re, collections
from nltk.corpus import wordnet as wn
from itertools import chain

def words(text): return re.findall('[a-z]+', text.lower())
#print words(file('big1.txt').read())

def train(features):
    model = collections.defaultdict(lambda: 1)
    #print model;
    #print features
    for f in features:
        #print f
        model[f] += 1
        #print model[f];
    return model
wordset = words(file('big.txt').read());
NWORDS = train(wordset)
#print NWORDS;
#print NWORDS['second'];

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)



# word = file('test.txt').read()
# #print word
# sentence=nltk.sent_tokenize(word)
# #print sentence
# target=open('write.txt','w')
# for sent in sentence:
#     print sent
#     for word in nltk.word_tokenize(sent):
#         #print word
#         if not wordnet.synsets(word):
#             target.write(correct(word)+" ")
#             print "****" + word
#         else:
#             print "///////////" + word
#             target.write(word+" ")
#     target.write("/n")
# target=open('write.txt','w')
# for wr in word:
#     #print wordnet.synsets(wr);
#    if not wordnet.synsets(wr):
#         target.write(correct(wr)+" ")
#     else:
#        target.write(wr+" ")
#
# target.close()