import pymysql
connection = pymysql.connect(host="localhost", user="root",password="root",port=3306,database="phonebook")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE customer (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100), contact BIGINT)")
# # cursor.execute("DROP TABLE customer")
               
# print("table created")

# qry=f"insert into customer values(null,'test1','123456')"
# cursor.execute(qry)
# connection.commit()
# print("Data added")

# cursor.execute("select * from customer")
# data=cursor.fetchall()
# for i in data:
#     print(i)