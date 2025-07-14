import pygame, random, time
pygame.init()
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class enemy(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, me_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=spawn_pos)

        direction = pygame.math.Vector2(me_pos) - spawn_pos
        if direction.length() == 0:
            direction = pygame.math.Vector2(1, 0)
        self.velocity = direction.normalize() * speed

    def update(self):
        self.rect.centerx += self.velocity.x
        self.rect.centery += self.velocity.y

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Comin' straight at you!")
clock = pygame.time.Clock()
img = pygame.image.load("ed.png").convert()
resize = pygame.transform.scale(img, (100, 100))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def fail(text):
    screen.fill(white)
    font = pygame.font.Font('freesansbold.ttf', 30)
    surf, rect = text_objects(text, font)
    rect.center = (width/2, height/2)
    screen.blit(surf, rect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def game_loop():
    pos = resize.get_rect(center = (400, 300))
    crash = False
    enemy_spawn_cooldown = 800     
    last_spawn_time = 0
    enemies = pygame.sprite.Group()
    start = pygame.time.get_ticks()

    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        now = pygame.time.get_ticks()

        if now - last_spawn_time > enemy_spawn_cooldown:
            last_spawn_time = now

            edge = random.randint(0, 3)
            if edge == 0:   
                spawn = pygame.math.Vector2(random.randrange(width), -30)
            elif edge == 1: 
                spawn = pygame.math.Vector2(width + 30, random.randrange(height))
            elif edge == 2: 
                spawn = pygame.math.Vector2(random.randrange(width), height + 30)
            else:           
                spawn = pygame.math.Vector2(-30, random.randrange(height))

            target = pygame.math.Vector2(pos.center)  
            enemies.add(enemy(spawn, target, speed=4))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            pos.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            pos.x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            pos.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            pos.y += 5

        ms = pygame.time.get_ticks() - start
        sec = ms // 1000

        enemies.update()
        for spi in enemies:
            if spi.rect.colliderect(pos):
                fail(f"Oopsie, you died!. You survived for {sec} seconds.")
        
        screen.fill(white)
        screen.blit(resize, pos)
        enemies.draw(screen)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
