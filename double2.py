from itertools import izip
import nltk
from textblob import Word
import itertools
import collections
import operator

feature1={'Feature':'count'}
features = []

feature_2 = []


def featureExtract_rule1(sentence):
    feature_1 = []
    postaglist = nltk.pos_tag(nltk.word_tokenize(sentence))
    with open('negative-words.txt') as neg, open('positive-words.txt') as pos:
        for word_neg, word_pos in izip(neg, pos):
            word_neg = word_neg.replace('\n', '')
            word_pos = word_pos.replace('\n', '')
            for post in postaglist:
                if (word_pos == post[0]):
                    for postn in postaglist:
                        if ((postn[1] == 'NN' or postn[1] == 'NNS') and ((postn[0] in feature1) == False)):
                            #feature1.append(Word(postn[0]).singularize())
                            feature1[Word(postn[0]).singularize()]=1
                        elif ((postn[1] == 'NN' or postn[1] == 'NNS') and ((postn[0] in feature1) == True)):
                            feature1[Word(postn[0]).singularize()] = feature1[Word(postn[0]).singularize()]+1

                if (word_neg == post[0]):
                    for postn in postaglist:
                        # if ((postn[1] == 'NN' or postn[1] == 'NNS') and ((postn[0] in feature_1) == False)):
                        #     feature_1.append(Word(postn[0]).singularize())
                        if ((postn[1] == 'NN' or postn[1] == 'NNS') and (((Word(postn[0]).singularize()) in feature1) == False)):
                            # feature1.append(Word(postn[0]).singularize())
                            feature1[Word(postn[0]).singularize()] = 1
                        elif ((postn[1] == 'NN' or postn[1] == 'NNS') and ((Word(postn[0]).singularize() in feature1) == True)):
                            feature1[Word(postn[0]).singularize()] = feature1[Word(postn[0]).singularize()] + 1

    #return feature_1


def featureExtract_rule2(sentence,feature1):

    postaglist = nltk.pos_tag(nltk.word_tokenize(sentence))
    for key in feature1.keys():
        for post in postaglist:
            #print 'feature_1= ' +  feature
            if (key == post[0]):
                #print 'post[0]= ' + post[0]
                for postn in postaglist:
                    #print 'postn ='
                    #print postn
                    # if ((postn[1] == 'NN' or postn[1] == 'NNS')  and ((postn[0] in feature1) == False)):
                    #     #print postn[0]
                    #     feature1.append(postn[0])
                    if ((postn[1] == 'NN' or postn[1] == 'NNS') and ((Word(postn[0]).singularize() in feature1) == False)):
                        # feature1.append(Word(postn[0]).singularize())
                        feature1[Word(postn[0]).singularize()] = 1
                    elif ((postn[1] == 'NN' or postn[1] == 'NNS') and ((Word(postn[0]).singularize()  in feature1) == True)):
                         feature1[Word(postn[0]).singularize()] = feature1[Word(postn[0]).singularize()] + 1
    #return feature1

def controller(fileName):
    final={'Feature':'Count'}

    with open(fileName,'r') as pointer:
        #pointer = open(fileName,'r')
        for row in pointer:
            # feature = featureExtract_rule1(row)
            # feature1.extend(feature)
            featureExtract_rule1(row)

    #print feature1

    with open(fileName, 'r') as pointer2:
        for row in pointer2:
            featureExtract_rule2(row,feature1)


    del feature1['Feature']
    for i in range(20):
        value=max(feature1.iteritems(), key=operator.itemgetter(1))[0]
        final[value]=feature1[value]
        #print final
        del feature1[value]
    del final['Feature']

    return final
