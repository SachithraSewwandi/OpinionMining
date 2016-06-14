
import MySQLdb as mdb
import sys
from Nltk import sentenceTokanize, wordTokanize, posTagging

from DbConnectMethods import createTable, retrieveTable, deleteRow, updateRow

con = mdb.connect('localhost', 'testuser1', 'test623', 'testdb')
createTable(con)
rows =retrieveTable(con)
#sentenceTokanize(rows)
map1={}
for row in rows:
    sentence =row["COMMENT"]
    #print sentence
    sentenceTokanize(sentence)

    tokens =posTagging(wordTokanize(sentence))
    #print tokens
    propernouns = [word for word, pos in tokens if pos == 'NNP' or pos=='NN']
    #print propernouns

    for word in propernouns:
        if map1.has_key(word):
            map1[word]= int(map1.get(word)) + 1
        else:
            map1[word]='1'
        print word

#print map1.get('Caio')
#print map1.has_key('Caio')
print map1
con.close()