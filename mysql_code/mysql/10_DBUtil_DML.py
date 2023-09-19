import pymysql
class DBUtil:
    config ={
        'host':'localhost',
        'port':3306,
        'user':'root',
        'passwd':'JLiu',
        'db':'sxt',
        'charset':'utf8'
    }
    def __init__(self):
        """
        connecting to database
        get cursor
        """
        self.con=pymysql.connect(**DBUtil.config)
        self.cursor=self.con.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()
    
    def execute_dml(self,sql,args):
        """
        可以执行dml语句,用于数据的增删改
        """
        # error handling
        try:
            # execute sql
            self.cursor.execute(sql,args)
            # commit sql
            self.con.commit()
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally: 
            self.close()


if __name__=='__main__':
    db=DBUtil()
    sql='INSERT INTO table_user VALUES(0,%s,%s,%s,%s)'
    args=('fengkuzi',28,'F','123')
    db.execute_dml(sql,args)
    # db.execute_dml(sql,'fengkuzi',28,'F','123') # if use *args