# pip install pymysql
import pymysql

# connecting db
con=pymysql.connect(host='localhost',port=3306, user='root',passwd='JLiu',charset='utf8',db='sxt')
# get interactive cursor
cursor=con.cursor()
# to write sql
sql="""
CREATE TABLE table_user(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key',
    username VARCHAR(30) not NULL,
    age int(10) not NULL,
    sex VARCHAR(5)
    
) DEFAULT CHARSET UTF8;
"""
# execute sql
cursor.execute(sql)
# close sql
cursor.close()
# deconnect db
con.close()