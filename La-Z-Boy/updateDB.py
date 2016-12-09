import sqlite3

def updateDB(channel, movieName, timeF, timeT, rating):
	sqlite_file ='database/InfoBase.sqlite'
	tableName = 'MovieInfo'
	
	#Opening a connection to db
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	
	#Creates a new db if it doesn't exist
	try:
		c.execute("CREATE TABLE IF NOT EXISTS `MovieInfo` ( `Channel` TEXT NOT NULL, `MovieName` TEXT NOT NULL, `TimeFrom` TEXT, `TimeTo` TEXT, `Rating` TEXT )")
	except:
		print("Database creation error")
	
	#Adds the movie data to the table
	try:
		for i in range(len(movieName)):
			c.execute("INSERT INTO {tn} VALUES ('{cn}', '{mn}', '{tf}', '{tt}', '{r}')".format(tn=tableName, cn=channel, mn=movieName[i], tf=timeF[i], tt=timeT[i], r=rating[i]))
	except:
		print("Data insertion error")
	
	#Comminting changes in db and closing it.
	conn.commit()
	conn.close()
