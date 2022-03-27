from GameObject import *
from settings import *
import pygame


class Main:
    # __init__ - иннициализация PyGame, установка размера и названия экрана
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("AstroWarrior")
        self.background = loader("bg", False)
        self.player = Player((W // 2, H // 2))
        self.meteor = Meteor((200, 300))

    def main_game_loop(self):
        loop = True
        while loop:
            self.clock.tick(FPS)
            self.controls()
            self.drawing()
            self.game_process()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    loop = False
                    quit()


    def controls(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.player.rotate(clockwise=True)
        if key[pygame.K_LEFT]:
            self.player.rotate(clockwise=False)

    def game_process(self):
        self.player.obj_move()
        self.meteor.obj_move()

    def drawing(self):
        self.screen.blit(self.background, (0, 0))
        self.player.obj_draw(self.screen)
        self.meteor.obj_draw(self.screen)
        pygame.display.flip()


Main().main_game_loop()
