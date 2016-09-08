from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def polarityCheckerTextBlob(fileName):

    with open(fileName,'r') as pointer:
        for row in pointer:
            print row
            blob = TextBlob(row)
            print(blob.sentiment.polarity)
            print

    #text = "This work is not good"

    #blob = TextBlob(text)
    #blob.tags
    #print blob.tags

    #blob.noun_phrases
    #print blob.noun_phrases

    #for sentence in blob.sentences:
     #   print(sentence.sentiment.polarity)


    blob.translate(to="es")



def polarityCheckerNLTK(fileName):

    sentences =[]
    with open(fileName, 'r') as pointer:
        for row in pointer:
            sentences.append(row)




    #lines_list = tokenize.sent_tokenize(paragraph)
    #sentences.extend(lines_list)



    #sentences.extend(tricky_sentences)
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)

        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]))


    #with open(fileName, 'r') as pointer:
     #   for row in pointer:
      #      print row





print "with TextBlob"
polarityCheckerTextBlob("dataset.txt")
print "With NLTK/////////////"
polarityCheckerNLTK("test.txt")