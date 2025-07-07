import pygame 
pygame.init()
width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

img = pygame.image.load("ed.png")
resize = pygame.transform.scale(img, (100, 100))
def draw(x, y):
    screen.fill(white)
    screen.blit(resize, (x, y))
                
x = (width * .43)
y = (height * .8)

draw(x, y)

crash = False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
    
    screen.fill(white)
    draw(x, y)

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
