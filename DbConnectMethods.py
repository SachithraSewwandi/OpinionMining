# Import MySQLdb       $ sudo apt-get install python-mysqldb
import MySQLdb as mdb
import sys


# CREATE A NEW TABLE and INSERT SOME VALUES
def createTable(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS TableTest")
        cur.execute("CREATE TABLE TableTest(Id INT PRIMARY KEY AUTO_INCREMENT, \
                     COMMENT VARCHAR(25))")
        cur.execute("INSERT INTO TableTest(COMMENT) VALUES('Babbo Natale is good')")
        cur.execute("INSERT INTO TableTest(COMMENT) VALUES('Tizio was a murderer')")
        cur.execute("INSERT INTO TableTest(COMMENT) VALUES('Caio is good')")
        cur.execute("INSERT INTO TableTest(COMMENT) VALUES('Sempronio swims a lot')")
        cur.execute("INSERT INTO TableTest(COMMENT) VALUES('Giulio Cesare works hard')")



# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT COMMENT FROM TableTest")

        rows = cur.fetchall()

        #for row in rows:
        #    print row["Id"], row["Name"]
        return rows


# UPDATE ROW
def updateRow(con):
    with con:

        cur = con.cursor()

        cur.execute("UPDATE TableTest SET Name = %s WHERE Id = %s",
            ("Nome Acaso", "4"))

        print "Number of rows updated:",  cur.rowcount



# DELETE ROW
def deleteRow(con):
    with con:

        cur = con.cursor()

        cur.execute("DELETE FROM TableTest WHERE Id = %s", "2")

        print "Number of rows deleted:", cur.rowcount

