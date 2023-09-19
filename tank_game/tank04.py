"""
show game window
"""
import pygame
# define global variable that all the classes can access to (设置通用属性)
BG_COLOR=pygame.Color(255,255,255)
SCREEN_WID=800
SCREEN_HEI=600


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
            pygame.display.update()
            

    def game_over():
        pass

if __name__=="__main__":
        # call game_start function in class MainGame to start the game
        MainGame().game_start()