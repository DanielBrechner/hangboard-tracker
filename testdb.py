import sqlite3

conn = sqlite3.connect("hang_record.db")

# create a cursor
c = conn.cursor()


c.execute(
    "INSERT INTO workout VALUES ('Daniel','Brechner','brechner.daniel@gmail.com')")

# commit our command
conn.commit()

# close connection
conn.close()
