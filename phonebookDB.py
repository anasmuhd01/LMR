import pymysql
connection = pymysql.connect(host="localhost", user="root",password="root",port=3306,database="phonebook")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE customer (name VARCHAR(100), contact BIGINT)")
# print("table created")