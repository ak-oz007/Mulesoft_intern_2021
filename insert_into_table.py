import sqlite3

con = sqlite3.connect('movies.db')

mycur = con.cursor()

mycur.execute("INSERT INTO mov_det VALUES('Vijay','Asin','Bodygard','Siddique',2014)")
mycur.execute("INSERT INTO mov_det VALUES('Hemsworth','Jennifer','Thor','Thomas',2011)")
mycur.execute("INSERT INTO mov_det VALUES('Rajinikanth','Rai','Robot','Shankar',2012)")
mycur.execute("INSERT INTO mov_det VALUES('Kamal','Simran','5_mantras','Ravi',2004)")
mycur.execute("INSERT INTO mov_det VALUES('Dhanush','Sonam','Raanjana','Anand',2014)")

print("Values written into the table")

con.commit()
con.close()
