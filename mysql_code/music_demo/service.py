from tools import DBUtil
import pygame
class MusicService:
    def __init__(self):
        self.user=None
    # login feature
    def login(self,uname:str,passwd:str)-> bool:
        '''
        login
        param uname:
        param passwd: 
        return: true if sucessful login, false if failure
        '''
        # edit sql
        sql='select id, uname from t_user where uname=%s and passwd=%s'
        # create tool object
        db=DBUtil()
        # execute sql
        user = db.query_one(sql,uname,passwd)
        # determine if login is successful. if user is not null, return true
        if user:
            # print('login successfully !')
            # record user info once user login
            self.u_id=user
            return True
        else:
            # print('user not found')
            return

    def add_music(self,files:tuple[str]):  # pass tuple made of str into the func
        """
        feature that adds mudic to the table
        param files: path of music, multiple path made of str
        return none
        """
        # edit sql
        insert_music='insert into t_music(mname,path) values(%s,%s)'
        # go over data to sort music
        for f in files:
            print(f)
            # get music name according to the path
            mname=f[f.rfind('/')+1:f.rfind('.')]
            # create DBUtil object
            db=DBUtil()
            # execute sql
            # a=db.execute_dml(insert_music,mname,f)
            # print(a)
            m_id=db.execute_dml_returnId(insert_music,mname,f)
            
            # sql that bond user and music
            insert_play_music='insert into playlist(u_id,m_id) values(%s,%s)'
            # create the object again to avoid the error 'already closed'
            db=DBUtil()
            db.execute_dml(insert_play_music,self.u_id[0],m_id)
            
    def find_user_music(self)->list[str]:
        # sql
        sql='SELECT m.mname from playlist p left join t_music m on p.m_id=m.id where u_id=%s;'
        # create service object
        db=DBUtil()
        # execute sql
        m_list=db.query_all(sql,self.u_id[0])
        return m_list

    def playMusic(self,music_name:str):
        """
        play music when clicking the music on playlist
        """
        # get music path
        sql='select m.path from t_music m left join playlist p on p.m_id=m.id where u_id=%s and m.mname = %s;'
        db=DBUtil()
        path=db.query_one(sql,self.u_id[0],music_name)[0] # ('C:/user/blabla.mp3',)
        print(path)
        # call music player in pygame to play the music
        pygame.mixer.init()
        # load music
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()


# if __name__=='__main__':
#     ser=MusicService()
#     ser.login('bz','123')
    
    