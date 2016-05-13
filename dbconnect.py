
import MySQLdb as mdb
import sys
from Nltk import sentenceTokanize, wordTokanize, posTagging

from DbConnectMethods import createTable, retrieveTable, deleteRow, updateRow

con = mdb.connect('localhost', 'testuser1', 'test623', 'testdb')
#createTable(con)
rows =retrieveTable(con)
#sentenceTokanize(rows)
for row in rows:
    sentence =row["COMMENT"]
    sentenceTokanize(sentence)

    posTagging(wordTokanize(sentence))
    #print row
con.close()