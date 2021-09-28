import sqlite3
con = sqlite3.connect('movies.db')

mycur = con.cursor()

mycur.execute(""" CREATE TABLE mov_det (#actor text, actress text,name text, director text, release_year int ) """)

print(" Table has been created..")

con.commit()

con.close()
