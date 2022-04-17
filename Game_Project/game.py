#game.py
from GameObject import *
from settings import loader, pos_rand
import pygame
class Main: #Основной класс
    MIN_DIST = 200
    # __init__ - иннициализация PyGame, установка размера и названия экрана
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1024, 640))
        pygame.display.set_caption("SpaceWarrior")
        self.background = loader("bg", False)
        #Вызов объектов, объекты meteor и bullets создаются как простой список
        self.meteor = []
        self.bullets = []
        self.player = Player((1024 // 2, 640 // 2), self.bullets.append)
        #Случайна расстановка метеоритов
        for m in range(10):
            while True:
                pos = pos_rand(self.screen)
                if pos.distance_to(self.player.pos) > self.MIN_DIST:
                    break
            self.meteor.append(Meteor(pos, self.meteor.append))
    #Вызов главного цикла игры
    def main_game_loop(self):
        while True:
            #Пока пользователь не прервёт сессию - бедут выполняться обработка следующих данных:
            self._controls()
            self._drawing()
            self._game_process()
    #Обработка нажатий клавиш
    def _controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            elif (self.player
                  and event.type == pygame.KEYDOWN
                  and event.key == pygame.K_ESCAPE):
                self.player.shoot()
        key = pygame.key.get_pressed()
        if self.player:
            if key[pygame.K_d]:
                self.player.rotate(clockwise=True)
            elif key[pygame.K_a]:
                self.player.rotate(clockwise=False)
            if key[pygame.K_w]:
                self.player.fow_accelerate()
            elif key[pygame.K_s]:
                self.player.back_accelerate()
            if key[pygame.K_SPACE]:
                self.player.shoot()
    #Обработка игровых процессов(логики)
    def _game_process(self):
        for obj in self._get_obj():
            obj.obj_move(self.screen)
        if self.player:
            for meteor in self.meteor:
                if meteor.obj_collide(self.player):
                    self.player = None
                    break
        for bullet in self.bullets[:]:
            for meteor in self.meteor[:]:
                if meteor.obj_collide(bullet):
                    self.meteor.remove(meteor)
                    self.bullets.remove(bullet)
                    meteor.split()
                    break
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.pos):
                self.bullets.remove(bullet)
    #Обработка и прорисовка объектов
    def _drawing(self):
        self.screen.blit(self.background, (0, 0))
        for obj in self._get_obj():
            obj.obj_draw(self.screen)
        pygame.display.flip()
        self.clock.tick(50)
    def _get_obj(self):
        game_obj = [*self.meteor, *self.bullets]
        if self.player:
            game_obj.append(self.player)
        return game_obj
