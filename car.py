import pygame, random, time
pygame.init()
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)

class enemy(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed

    def update(self):
        self.rect.y += self.velocity

disp = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("Dodge!")
img = pygame.image.load("ed.png").convert_alpha()
img = pygame.transform.smoothscale(img, (100, 100))
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def disp_mess(text):
    font = pygame.font.Font('freesansbold.ttf', 50)
    surf, rect = text_objects(text, font)
    rect.center = (width/2, height/2)
    disp.fill(white)
    disp.blit(surf, rect)
    pygame.display.update()

    time.sleep(2)

    game()


def game():
    score = 0
    tex = pygame.font.Font('freesansbold.ttf', 20)
    pos = img.get_rect(midbottom = (400, 600))
    balls = pygame.sprite.Group()
    spawn_time = 500
    last = 0
    safe = True
    while safe:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
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
        if pos.x > width - 100 or pos.x < 0:
            disp_mess("You crashed at the side")
            

        disp.fill(white)
        disp.blit(img, pos)
        score_surf = tex.render(f"Score: {score}", True, black)
        disp.blit(score_surf, (10, 10))
        balls.update()
        balls.draw(disp)
        for b in balls:
            if b.rect.colliderect(pos):
                disp_mess("Oops. Dodge them bro")
            if b.rect.y > height:
                score += 1
                balls.remove(b)
        pygame.display.update()
        clock.tick(60)
    

game()
pygame.quit()
quit()