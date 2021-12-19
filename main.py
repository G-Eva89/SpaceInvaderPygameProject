import pygame

#initialize pygame
pygame.init()

#creating a screen
#(width, height)
screen = pygame.display.set_mode((1200,600))

#adding a title and an icon to the screen
pygame.display.set_caption("Space Invaders")
gameicon = pygame.image.load("spaceship2.png")
pygame.display.set_icon(gameicon)

#adding player to the game
playericon = pygame.image.load("spaceship.png")

#initial coordinates to the position of player
playerX = 568   #1200/2 - 64/2; 64 is the pixel size of playericon
playerY = 440   

def player(x,y):
    #draws the image of player at the given coordinates
    screen.blit(playericon, (x,y))

running = True
while running:
    
    #RGB values (r, g, b)
    screen.fill((0,0,30))
    
    for event in pygame.event.get():
    
        #quits the game when the cross button is clicked
        if event.type == pygame.QUIT:
            running = False
          
    

    player(playerX,playerY)
    
    #update the screen to reflect the changes made in this while loop
    pygame.display.update()
