from pygame.image import load


def loader(name, alpha=True):
    path = f'assets/images/{name}.png'
    loaded_sprite = load(path)
    if not alpha:
        return loaded_sprite.convert()
    else:
        return loaded_sprite.convert_alpha()


W = 1024
H = 680
FPS = 50

