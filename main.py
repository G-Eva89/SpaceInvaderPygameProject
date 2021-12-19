import pygame

#initialize pygame
pygame.init()

#creating a screen
#(width, height)
screen = pygame.display.set_mode((1200,600))

#adding a title and an icon to the screen
pygame.display.set_caption("Space Invaders")
gameicon = pygame.image.load("spacetravel.png")
pygame.display.set_icon(gameicon)

running = True
while running:
    
    #RGB values (r, g, b)
    screen.fill((0,0,30))
    
    for event in pygame.event.get():
    
        #quits the game when the cross button is clicked
        if event.type == pygame.QUIT:
            running = False
          

    #update the screen to reflect the changes made in this while loop
    pygame.display.update()
