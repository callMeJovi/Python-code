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
    def __init__(self) -> None:
        """
        connecting to database
        get cursor
        """
        self.con=pymysql.connect(**DBUtil.config)
        self.cursor=self.con.cursor()
        print('connected to database')

    def close(self):
        if self.cursor:
            self.cursor.close()
            print('cursor closed')
        if self.con:
            self.con.close()
            print('deconnected to database')
        
        
if __name__=='__main__':
    db=DBUtil()
    db.close()