import sqlite3

conn = sqlite3.connect('cars.db')

cursor = conn.cursor()


res = cursor.execute("INSERT INTO cars ('price', 'make', 'model', 'num_of_wheels') VALUES (3000, 'BMW', 'e39', 4)")

print(res)
conn.commit()
conn.close()