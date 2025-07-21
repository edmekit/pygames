import pygame, random, time
pygame.init()

width = 800
height = 600
white = (255, 255, 255)
black = (0,0,0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aliens Game")
img = pygame.image.load("ed.png").convert_alpha()
img = pygame.transform.smoothscale(img, (100, 100))
clock = pygame.time.Clock()

class enemy(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed

    def update(self):
        self.rect.y += self.velocity

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def disp_mess(text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    surf, rect = text_objects(text, font)
    rect.center = (width/2, height/2)
    screen.fill(white)
    screen.blit(surf, rect)
    pygame.display.update()

    time.sleep(2)


def game_loop():
    

