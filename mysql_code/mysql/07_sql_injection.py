import pymysql

def login1(username,pwd):
    # connect to db
    con=pymysql.connect(host='localhost', port=3306, user='root',passwd='JLiu',db='sxt',charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write in SQL, SQL injection risk
    # sql='select * from table_user where username="'+username+'" and pwd="'+pwd+'";'
    # sql=f'select * from table_user where username="{username}" and pwd="{pwd}";'
    sql='select * from table_user where username=%s and pwd=%s;'
    # 'select * from table_user where username="jingyi" and 1=1 #and pwd="1234";'
    # fetch data
    cursor.execute(sql,(username,pwd))
    rs=cursor.fetchone()
    print(rs)
    # close cursor
    cursor.close()
    # deconnect
    con.close()

if __name__=='__main__':
    # login1('kiko" and 1=1 #','1234')
    login1('jingyi','123')