import pymysql

def query_data():
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt',charset='utf8')
    cursor=con.cursor()
    sql='select * from table_user where;'
    try:
        cursor.execute(sql)
        rs=cursor.fetchone()
        print(rs)
    except Exception as e:
        print('sql execution error')
    finally:
        print('deconnecting database')
        cursor.close()
        con.close()

if __name__=='__main__':
        query_data()