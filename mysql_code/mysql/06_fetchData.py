import pymysql

def query_data():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt', charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write fetch sql
    sql='SELECT id,username,age,sex from table_user;'
    # execute
    cursor.execute(sql)
    #fetch data
    rs=cursor.fetchone()
    print(rs)
    rs=cursor.fetchone()
    print(rs)

    # close
    cursor.close()
    con.close()

def query_many():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt', charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write fetch sql
    sql='SELECT id,username,age,sex from table_user;'
    # execute
    cursor.execute(sql)
    #fetch data
    rs=cursor.fetchmany(2)
    print(rs)
    print(cursor.rowcount) # data au total, different from fetchmany(2)
    # close
    cursor.close()
    con.close()

def query_all():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt', charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write fetch sql
    # sql='SELECT id,username,age,sex from table_user;'
    sql='SELECT * from table_user;'
    # execute
    cursor.execute(sql)
    #fetch data
    rs=cursor.fetchall()
    print(rs)
    
    # close
    cursor.close()
    con.close()

def query_count():
    # connect db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt', charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write fetch sql
    sql='SELECT id,username,age,sex from table_user;'
    # execute
    cursor.execute(sql)
    #fetch data
    cursor.fetchall()
    print(cursor.rowcount)
    
    # close
    cursor.close()
    con.close()

if __name__=='__main__':
    # query_many()
    query_all()
    # query_count()
