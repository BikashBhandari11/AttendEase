import mysql.connector

conn = mysql.connector.connect(username='bikash', password='',host='localhost',database='Face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()