import pymysql

def update_data(args):
    # connecting db
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='JLiu',db='sxt',charset='utf8')
    # get cursor
    cursor=con.cursor()
    # write/update sql
    sql='UPDATE table_user set age=%s where id=%s;'
    # update args
    
    # execute sql
    cursor.execute(sql,args)

    # commit transaction
    con.commit()
    # close cursor
    cursor.close()

    # deconnecting with db
    con.close()

if __name__=='__main__':
    args=[70,6]
    update_data(args)