import pygame, random, time
pygame.init()

width = 800
height = 600
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
red = (255, 0 , 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aliens Game")
img = pygame.image.load("ed.png").convert_alpha()
img = pygame.transform.smoothscale(img, (100, 100))
clock = pygame.time.Clock()

class bullet(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=3):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed

    def update(self):
        self.rect.y -= self.velocity

class enemy(pygame.sprite.Sprite):
    def __init__(self, spawn_pos, speed=5):
        super().__init__()
        self.image = pygame.image.load("ed.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50,50))
        self.rect = self.image.get_rect(center=spawn_pos)
        self.velocity = speed
    
    def update(self):
        self.rect.y += self.velocity

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def disp_mess(text):
    font = pygame.font.Font('freesansbold.ttf', 40)
    btn_font = pygame.font.Font('freesansbold.ttf', 20)
    outside = True
    yes_rect = pygame.Rect(width/2 - 200, height/2 + 50, 150, 50)
    no_rect = pygame.Rect(width/2 + 70, height/2 + 50, 150, 50)
    while outside:
        surf, rect = text_objects(text, font)
        rect.center = (width/2, height/2 - 50)
        screen.fill(white)
        pygame.draw.rect(screen, red, no_rect)
        pygame.draw.rect(screen, green, yes_rect)
        no_txt = btn_font.render("Exit", True, black)
        yes_txt = btn_font.render("Start Again", True, black)
        txt_rect = yes_txt.get_rect(center = yes_rect.center)
        no_txt_rect = no_txt.get_rect(center = no_rect.center)
        screen.blit(no_txt, no_txt_rect)
        screen.blit(yes_txt, txt_rect)
        screen.blit(surf, rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    game_loop()
                if no_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()

def start():
    running = True
    font  = pygame.font.Font('freesansbold.ttf', 20)
    yes_rect = pygame.Rect(width/2 - 250, height/2 - 50, 200, 100)
    no_rect = pygame.Rect(width/2 + 50, height/2 - 50, 200, 100)
    while running:
        screen.fill(white)
        pygame.draw.rect(screen, red, no_rect)
        pygame.draw.rect(screen, green, yes_rect)
        no_txt = font.render("Exit", True, black)
        yes_txt = font.render("Start Game", True, black)
        txt_rect = yes_txt.get_rect(center = yes_rect.center)
        no_txt_rect = no_txt.get_rect(center = no_rect.center)
        screen.blit(no_txt, no_txt_rect)
        screen.blit(yes_txt, txt_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    running = False
                if no_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()


def game_loop():
    safe = True
    mypos = img.get_rect(midbottom = (400, 600))
    spawncd = 500
    last = 0
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    errors = 0
    score = 0
    tex = pygame.font.Font('freesansbold.ttf', 20)
    
    
    while safe:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current = pygame.time.get_ticks()

        if current - last > spawncd:
            last = current
            spawn = pygame.math.Vector2(mypos.center)
            enemyspawn = pygame.math.Vector2(random.randrange(width), -30)
            enemies.add(enemy(enemyspawn,speed=3))
            bullets.add(bullet(spawn,speed=5))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mypos.x -= 10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mypos.x += 10
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            mypos.y -= 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            mypos.y += 10

        screen.fill(white)
        screen.blit(img, mypos)
        score_surf = tex.render(f"Score: {score}", True, black)
        error_surf = tex.render(f"Errors: {errors}", True, black)
        screen.blit(error_surf, (700, 10))
        screen.blit(score_surf, (10, 10))

        for b in bullets:
            if b.rect.y < 0:
                bullets.remove(b)
            for e in enemies:
                if e.rect.colliderect(mypos):
                    disp_mess(f"Game Over. \n Score: {score}")
                    safe = False
                if b.rect.colliderect(e.rect):
                    score += 1
                    enemies.remove(e)
                    bullets.remove(b)
                    break
                if e.rect.y > height:
                    errors += 1
                    enemies.remove(e)
        
        if errors == 10:
            disp_mess(f"Aliens invaded Earth. \n Score: {score}")
            safe = False
                    
        enemies.update()  
        bullets.update()
        enemies.draw(screen)
        bullets.draw(screen)
        pygame.display.update()
        clock.tick(60)

start()
game_loop()
pygame.quit()
quit()


