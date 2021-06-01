import pygame

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

#player with internal grraphing
color = (255, 175, 0)
playerX = 500
playerY = 250
playerRect = pygame.draw.rect(screen,color, pygame.Rect(30, 30, 50, 50))



# game loop to allow it to keep going
running = True
while running:
    screen.fill((45, 255, 180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB fill of the screen
    
    pygame.display.flip()
