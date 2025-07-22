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

class bullet(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed

    def update(self):
        self.rect.y -= self.velocity

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
    safe = True
    mypos = img.get_rect(midbottom = (400, 600))
    spawncd = 500
    last = 0
    start = pygame.time.get_ticks()
    bullets = pygame.sprite.Group()
    
    while safe:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current = pygame.time.get_ticks()

        if current - last > spawncd:
            last = current
            spawn = pygame.math.Vector2(mypos.center)
            bullets.add(bullet(spawn,speed=5))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mypos.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mypos.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            mypos.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            mypos.y += 5

        screen.fill(white)
        screen.blit(img, mypos)
        bullets.update()
        bullets.draw(screen)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()


