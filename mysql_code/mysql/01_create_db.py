# pip install pymysql
import pymysql

# connecting db - 'db=' no needed coz we're creating a db named sxt
con=pymysql.connect(host='localhost',port=3306, user='root',passwd='JLiu',charset='utf8')
# get interactive cursor
cursor=con.cursor()
# to write sql
sql="""
CREATE DATABASE sxt
    DEFAULT CHARACTER SET = 'utf8mb4';
"""
# execute sql
cursor.execute(sql)
# close sql
cursor.close()
# deconnect db
con.close()