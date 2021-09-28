import sqlite3

con = sqlite3.connect('movies.db')

mycur = con.cursor()


mycur.execute(" SELECT * FROM mov_det")
mycur.execute("SELECT * FROM mov_det WHERE release_year=2012")

print(mycur.fetchall())

con.commit()
con.close()