import pygame
from pygame.display import update

#initilization of pygame
pygame.init()


#screen creation
screen = pygame.display.set_mode((1000, 500))

#Title and Icon
pygame.display.set_caption("Space Invaders")
# icon = pygame.image.load(name of image file)
#pygame.display.set_icon(icon)


#player with image
#playerImage = pygame.image.load(name of file)

#player with internal graphing
color = (255, 175, 0)
playerX = 500
playerY = 250
playerRect = pygame.draw.rect(screen,color, pygame.Rect(playerX, playerY, 50, 50))

#bullet set up
class Bullet():
    bulletX = playerX + 25
    bulletY = playerY
    
    def __init__(self) -> None:
        pygame.draw.circle(screen, (180, 50, 20), (bulletX,bulletY), 10)

    def update(self):
        self.bulletY += 5
        pass

#clock set up for each frame
clock = pygame.time.Clock()

# game loop to allow it to keep going
running = True
while running:
    screen.fill((45, 255, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB fill of the screen
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: playerY -= 3
    if pressed[pygame.K_DOWN]: playerY += 3
    if pressed[pygame.K_RIGHT]: playerX += 3
    if pressed[pygame.K_LEFT]: playerX -= 3
    if pressed[pygame.K_SPACE]: 
        Bullet.__init__(Bullet)
        Bullet.update(Bullet)


    pygame.draw.rect(screen,color, pygame.Rect(playerX, playerY, 50, 50))
    pygame.display.flip()
    clock.tick(60)
