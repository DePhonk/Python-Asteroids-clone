#settings.py
from pygame.image import load
from pygame.math import Vector2
import random
#Загрузчик спрайтов из ассетов
def loader(name, alpha=True):
    path = f'assets/{name}.png'
    loaded_sprite = load(path)
    if not alpha:
        return loaded_sprite.convert()
    else:
        return loaded_sprite.convert_alpha()
#Переход на противоположную сторону, если объект выходит из поля видимости игрока (Метеориты и сам игрок)
def wrap_pos(pos, surface):
    x, y = pos
    w, h = surface.get_size()
    return Vector2(x % w, y % h)
#Случайное положение Метеорита, основываясь на векторах ширины и высоты игрового поля
def pos_rand(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )
#Установка случайной скорости
def vel_rand(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)
