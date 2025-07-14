import pygame

pygame.init()
width = 800
height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

ed1 = pygame.image.load("ed.png").convert_alpha()
ed2 = pygame.image.load("ed.png").convert_alpha()
ed1 = pygame.transform.smoothscale(ed1, (100, 100))
ed2 = pygame.transform.smoothscale(ed2, (100, 100))
ball = pygame.image.load("ball.png").convert_alpha()
ball = pygame.transform.smoothscale(ball, (50, 50))

score = 0

def game():
    speed = 10
    ed1rect = ed1.get_rect(midbottom = (400, 100))
    ed2rect = ed2.get_rect(midbottom = (400,600 ))
    ballrect = ball.get_rect(center = (400, 400))
    def update():
       
        ballrect.y += speed 

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ed1rect.x -= 10
        if keys[pygame.K_RIGHT]:
            ed1rect.x += 10
        if keys[pygame.K_UP]:
            ed1rect.y -= 10
        if keys[pygame.K_DOWN]:
            ed1rect.y += 10
        if keys[pygame.K_a]:
            ed2rect.x -= 10
        if keys[pygame.K_d]:
            ed2rect.x += 10
        if keys[pygame.K_w]:
            ed2rect.y -= 10
        if keys[pygame.K_s]:
            ed2rect.y += 10
        
        screen.fill(white)
        screen.blit(ed1, ed1rect)
        screen.blit(ed2, ed2rect)
        screen.blit(ball, ballrect)

        if ballrect.colliderect(ed1rect) or ballrect.colliderect(ed2rect):
            speed *= -1      
        update()
        pygame.display.update()
        clock.tick(60)
game()
pygame.quit()
quit()