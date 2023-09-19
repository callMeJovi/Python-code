"""
Add events handler 增加事件处理
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
    def __init__(self):
        pass

    def display_tank(self)->None:
        """
        display tanks"""
        pass

    def move(self):
        """
        tank moves
        """
        pass

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
        font=pygame.font.SysFont("gigi",18)
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
                elif event.key==pygame.K_RIGHT:
                    print('Tank moving to right')
                elif event.key==pygame.K_UP:
                    print('Tank moving up')
                elif event.key==pygame.K_DOWN:
                    print('Tank moving down')

                
    def game_over(self):
        print('See you next time !')
        exit()

if __name__=="__main__":
    # call game_start function in class MainGame to start the game
    MainGame().game_start()


