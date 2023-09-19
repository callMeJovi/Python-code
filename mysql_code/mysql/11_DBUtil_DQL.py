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
    
    def execute_dml(self,sql,*args):
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

    def query_one(self,sql,*args):
        """
        fetch one data
        """
        try:
            # execute sql
            self.cursor.execute(sql,*args)
            # get result
            rs=self.cursor.fetchone()
            return rs
        except Exception as e:
            if self.con:
                self.con.rollback()
        finally:
            self.close()

    def query_many(self,sql,*args):
        """
        fetch one data
        """
        try:
            # execute sql
            self.cursor.execute(sql,args)
            # get result
            rs=self.cursor.fetchmany()
            return rs
        except Exception as e:
            if self.con:
                self.con.rollback()
        finally:
            self.close()

    def query_all(self,sql,*args):
        """
        fetch one data
        """
        try:
            # execute sql
            self.cursor.execute(sql,*args)
            # get result
            rs=self.cursor.fetchall()
            return rs
        except Exception as e:
            if self.con:
                self.con.rollback()
        finally:
            self.close()

if __name__=='__main__':
    db=DBUtil()
    sql="select * from table_user where age=%s;"
    print(db.query_all(sql,30))