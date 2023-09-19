"""
move my tank
"""
import pygame
#define global variable that all the classes can access to (设置通用属性)
BG_COLOR=pygame.Color(0,0,0)
SCREEN_WID=800
SCREEN_HEI=600
TEXT_COLOR=pygame.Color(255,0,0)


class Tank:
    """
    class tank
    """
    def __init__(self,left,top):
        # upload images when initializing class
        # dict of images
        self.images={'U':pygame.image.load('./img/p1tankU.gif'), # load returns object "surface", then goto surface in pygame
                     'D':pygame.image.load('./img/p1tankD.gif'),
                     'L':pygame.image.load('./img/p1tankL.gif'),
                     'R':pygame.image.load('./img/p1tankR.gif'),
        }
        # set orientation of the tanks, save value of 'u' to self.orientation
        self.orientation='L'
        # get the image of 'u'
        self.image=self.images.get(self.orientation)
        # get rect of the surface
        self.rect=self.image.get_rect()
        # position of my tank
        self.rect.left=left
        self.rect.top=top
        self.speed=10
        print(self.rect.width,self.rect.height)


    def display_tank(self)->None:
        """
        display tanks
        """
        self.image=self.images.get(self.orientation)
        #print(self.orientation)
        MainGame.window.blit(self.image,self.rect)

    def move(self):
        """
        tank moves
        """
        if self.orientation=='L':
            if self.rect.left>0:
                self.rect.left=self.rect.left-self.speed
            
        if self.orientation=='U':
            if self.rect.top>0:
                self.rect.top=self.rect.top-self.speed
        if self.orientation=='R':
            if self.rect.left+self.rect.width<SCREEN_WID:
                self.rect.left=self.rect.left+self.speed
        if self.orientation=='D':
            if self.rect.top+self.rect.height<SCREEN_HEI:
                self.rect.top=self.rect.top+self.speed
        

    
    def shoot(self):
        """
        tank shoots
        """
        pass

class MyTank(Tank):
    """
    tank on our side

    """
    def __init__(self):
        pass

class EnemyTank(Tank):
    """
    enenmy
    """
    def __init__(self):
        pass

class Bullet:

    def __init__(self) -> None:
        pass
    def bullet_display(self):
        pass

    def bullet_move():
        pass

class Mural:
    def __init__(self) -> None:
        pass

    def mural_display():
        """
        show mural
        """
        pass

class Explode:
    def __init__(self) -> None:
        pass

    """
    display bomb
    """

    def explode_display(self):
        pass

class Music:
    def __init__(self) -> None:
        pass

    def music_display():
        pass

class MainGame:
    # inside class, define a global variable named window that the main window object (游戏主窗口) can assign to
    # at the begining, nothing in this window 
    # window是类属性
    window=None
    #create a new global "my tank" variable that other functions can access to with prefix MainGame
    my_tank=None

    def __init__(self) -> None:
        pass

    def game_start(self):
        """
        I want to display the game window once the game starts
        so the game window initialisation should be put here
        """
        # initialize the game window
        pygame.display.init()
        # create a window object
        # I pass the value of the window object that I created to the class variable window
        MainGame.window=pygame.display.set_mode((SCREEN_WID,SCREEN_HEI))
        # rename name of the window
        pygame.display.set_caption("Tank game v1.0")
        # create and initialize my tank 将显示我方坦克放到while true中因为每次window刷新都要显示坦克
        MainGame.my_tank=Tank(350,280)  # my_tank=Tank() this can't be callable outside the fn
        
        # update window constantly
        while True:
            # fill the window with color. 
            MainGame.window.fill(BG_COLOR)
            # add notification texts (增加提示文字)
            # 1. 添加文字内容
            num=6
            text=self.get_text_surface(f'the enemy tanks remain {num}')

            # 2. 如何把文字加上 use the result of fn pygame.display.set_mode coz I want add the text on game window
            MainGame.window.blit(text,(10,10))

            # add events
            self.get_event()
            # show my tank
            MainGame.my_tank.display_tank()

            pygame.display.update()
    
    def get_text_surface(self,text:str):
        """
        get text object 获取文本对象
        """
        # initialize font module
        pygame.font.init()
        
        # create font
        # create a Font object from the system fonts
        # SysFont(name, size, bold=False, italic=False) -> Font
        font=pygame.font.SysFont("kaiti",18)
        # render font
        text_surface=font.render(text,True,TEXT_COLOR)
        # return text_surface
        return text_surface

    def get_event(self):
        """
        get event
        """
        #get event lists
        event_list=pygame.event.get()
        # go over all events
        for event in event_list:
            # determine events
             #close the window
                # print(event.type)
            if event.type==pygame.QUIT:
                self.game_over()
            
            if event.type==pygame.KEYDOWN:
                # press keydown
                if event.key==pygame.K_LEFT:
                    print('Tank moving to left')
                    # through tank object my_tank=Tank()
                    # switch orientation
                    self.my_tank.orientation="L"
                    #MainGame.my_tank.orientation="L"
                    self.my_tank.display_tank()
                    self.my_tank.move()
                    #MainGame.my_tank.display_tank()
                elif event.key==pygame.K_RIGHT:
                    print('Tank moving to right')
                    self.my_tank.orientation="R"
                    self.my_tank.display_tank()
                    self.my_tank.move()
                elif event.key==pygame.K_UP:
                    print('Tank moving up')
                    self.my_tank.orientation="U"
                    self.my_tank.display_tank()
                    self.my_tank.move()
                elif event.key==pygame.K_DOWN:
                    print('Tank moving down')
                    self.my_tank.orientation="D"
                    self.my_tank.display_tank()
                    self.my_tank.move()

                
    def game_over(self):
        print('See you next time !')
        exit()

if __name__=="__main__":
    # call game_start function in class MainGame to start the game
    MainGame().game_start()


