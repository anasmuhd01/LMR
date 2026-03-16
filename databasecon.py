import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             port=3306,
                             database="luminar")
cursor=connection.cursor()

