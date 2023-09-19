"""
https://www.runoob.com/python/python-gui-tkinter.html
https://docs.python.org/3/library/tkinter.html
"""
import tkinter
from service import MusicService
from tkinter.filedialog import askopenfilenames

class PlayerWindow:
    def __init__(self):
    # def music_player():
        top=tkinter.Tk()
        # add button, top is parent container to button
        btn1=tkinter.Button(top,text='PLAY')
        btn2=tkinter.Button(top,text='import a song')
        btn3=tkinter.Button(top,text='Delete a song')
        # window loop
        btn1.grid(row=0,column=0,padx=5,pady=5)
        btn2.grid(row=0,column=2,padx=5, pady=5)
        btn3.grid(row=0,column=4,padx=5, pady=5)

        # add playlist
        self.listbox=tkinter.Listbox(top)
        self.listbox.grid(row=1,column=0,columnspan=5,padx=5,pady=5)
        # get playlist in tk
        self.load_music()
        
        # btn2 event listener
        btn2.bind('<ButtonRelease-1>',self.import_music)
        btn1.bind('<ButtonRelease-1>',self.find_name)
        top.mainloop()

    def import_music(self,event):
        print('importing music')
        filenames=askopenfilenames(filetypes=[('mp3','.mp3'),('flac','.flac')])
        
        ms.add_music(filenames)
        # print(filenames)
        # load imported music
        # self.load_music()
    
    def load_music(self):
        # call music finder to get playlist of a user in tk
        music_plist=ms.find_user_music()
        for music in music_plist:
            self.listbox.insert(0,music[0])

    def find_name(self,event):
        # get current selected music
        index=self.listbox.curselection() # curselection() return un indice
        musicName=self.listbox.get(index)
        # pass musicName to playMusic
        ms.playMusic(musicName)

        

if __name__=='__main__':
    uname=input('enter user name :')
    passwd=input('enter your password:')
    # create service object
    ms=MusicService()
    # if login successfully
    if ms.login(uname,passwd):
        print('login successfully, yeah !')
        pw=PlayerWindow() # initialize class playerWindow when def __init__() in class
    else:
        print('user not found, login unsuccessfully :(')

