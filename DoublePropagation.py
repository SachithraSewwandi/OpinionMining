from itertools import izip
import nltk
import collections
import re
from nltk.stem import *
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

features = []

opinions = []


def featureExtract_rule1(sentence):
    feature_1 = []
    postaglist = nltk.pos_tag(nltk.word_tokenize(sentence))
    with open('negative-words.txt') as neg, open('positive-words.txt') as pos:
        for word_neg, word_pos in izip(neg, pos):
            word_neg = word_neg.replace('\n', '')
            word_pos = word_pos.replace('\n', '')
            for post in postaglist:
                if (word_pos == post[0]):
                    opinions.append(word_pos)
                    for postn in postaglist:
                        if ((postn[1] == 'NN' or postn[1] == 'NNS') and ((postn[0] in feature_1) == False)):
                            feature_1.append(postn[0])
                if (word_neg == post[0]):
                    opinions.append(word_neg)
                    for postn in postaglist:
                        if ((postn[1] == 'NN' or postn[1] == 'NNS') and ((postn[0] in feature_1) == False)):
                            feature_1.append(postn[0])


    return feature_1


#print featureExtract('It charges AA batteries just fine but has a huge problem securing smaller AAA batteries')

def featureExtract_rule2(sentence,feature1):

    postaglist = nltk.pos_tag(nltk.word_tokenize(sentence))
    for feature in feature1:
        for post in postaglist:
            #print 'feature_1= ' +  feature
            if (feature == post[0]):
                #print 'post[0]= ' + post[0]
                for postn in postaglist:
                    #print 'postn ='
                    #print postn
                    if ((postn[1] == 'NN' or postn[1] == 'NNS')  and ((postn[0] in feature1) == False)):
                        #print postn[0]
                        feature1.append(postn[0])
    #return feature1

def featureExtract_rule3(sentence,feature1):
    new_opinions = []
    postaglist = nltk.pos_tag(nltk.word_tokenize(sentence))

    for feature in feature1:
        for post in postaglist:
            #print 'feature_1= ' +  feature
            if (feature == post[0]):
                #print 'post[0]= ' + post[0]
                for postn in postaglist:
                    #print 'postn ='
                    #print postn
                    if ((postn[1] == 'JJ' or postn[1] == 'JJR' or postn[1] == 'JJS') and ((postn[0] in feature1) == False)):
                        print 'opinions////////////////////////'
                        print post[0]
                        new_opinions.append(postn[0])
    return

def controller(fileName):
    #stemmer = nltk.stem.WordNetLemmatizer()

    feature1 = []

    with open(fileName,'r') as pointer:
        #pointer = open(fileName,'r')
        for row in pointer:
            feature = featureExtract_rule1(row)
            feature1.extend(feature)

    #print feature1

    with open(fileName, 'r') as pointer2:
        for row in pointer2:
            featureExtract_rule2(row,feature1)

    #print 'featuress1'
    #print feature1


    #return feature1
    feature_counter = collections.Counter(feature1)
    #print feature_counter.most_common(20)
    counter = collections.Counter(feature1)

    #print 'finalyly//////////////////'
    #print feature2

    #return feature_counter.most_common(20)
    # return counter
    return feature1

# controller()


features = controller("dataset.txt")
print(features)
print 'opinions'
print opinions