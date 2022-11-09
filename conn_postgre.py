import psycopg2
conn = psycopg2.connect(
	host = "localhost",
	database = "template1",
	user = "postgres",
	password = "postgrespw",
	port = "55000"
 
)

cursor = conn.cursor()
cursor.execute('select * from ex')
data = cursor.fetchall()

print(data)

conn.close()
