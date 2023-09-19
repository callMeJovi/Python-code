import pymysql
"""
under module pymysql, if operating with DML, we need to commit transaction => con.commit()
"""
def add_one():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu', db='sxt',charset='utf8')
    # get cursor
    cursor = con.cursor()
    # write SQL
    # sql="INSERT into table_user VALUES (0,'kiko',30,'M');"
    sql="INSERT into table_user VALUES (0,%s,%s,%s);"
    args1=['gigi',20,'F']
    
    # execute SQL
    cursor.execute(sql,args1)
    con.commit()
    # close cursor
    cursor.close()
    # deconnect
    con.close()

def add_many():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu', db='sxt',charset='utf8')
    # get cursor
    cursor = con.cursor()
    # write SQL
    # sql="INSERT into table_user VALUES (0,'kiko',30,'M');"
    sql="INSERT into table_user VALUES (0,%s,%s,%s);"
    args=[['gigi',20,'F'],['yoyo',35,'ND'],['bobo',16,'M']]
    
    # execute SQL
    cursor.executemany(sql,args)
    con.commit()
    # close cursor
    cursor.close()
    # deconnect
    con.close()

if __name__=='__main__':
    add_many()