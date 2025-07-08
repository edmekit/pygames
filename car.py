import pygame, random
pygame.init()
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)

class enemy(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed

    def update(self):
        self.rect.y += self.velocity

disp = pygame.display.set_mode((width, height))
img = pygame.image.load("ed.png").convert_alpha()
img = pygame.transform.smoothscale(img, (100, 100))
pos = img.get_rect(midbottom = (400, 600))
clock = pygame.time.Clock()


balls = pygame.sprite.Group()
spawn_time = 500
last = 0
safe = True

while safe:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            safe = False
    
    now = pygame.time.get_ticks()
    if now - last > spawn_time:
        last = now
        spawn = pygame.math.Vector2(random.randrange(width), -30)
        balls.add(enemy(spawn, speed=5))

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pos.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pos.x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        pos.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        pos.y += 5

    disp.fill(white)
    disp.blit(img, pos)
    balls.update()
    balls.draw(disp)
    for b in balls:
        if b.rect.colliderect(pos):
            safe = False
    pygame.display.update()
    clock.tick(60)
    
