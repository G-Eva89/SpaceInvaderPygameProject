import pygame
import random

#initialize pygame
pygame.init()

#creating a screen
#(width, height)
screen = pygame.display.set_mode((1200,600))

#adding a title and an icon to the screen
pygame.display.set_caption("Space Invaders")
gameicon = pygame.image.load("spacetravel.png")
pygame.display.set_icon(gameicon)

#adding player to the game
playericon = pygame.image.load("spaceship.png")
#initial coordinates to the position of player
playerX = 568   #1200/2 - 64/2; 64 is the pixel size of playericon
playerY = 440   
playerX_change = 0


#adding player to the game
enemyicon = pygame.image.load("alien.png")
#initial coordinates to the position of enemy
enemyX = random.randint(0,1136)
enemyY = random.randint(0,300)   
enemyX_change = 0

#creating a player
def player(x,y):
    #draws the image of player at the given coordinates
    screen.blit(playericon, (x,y))
    
#creating an enemy
def enemy(x,y):
    #draws the image of player at the given coordinates
    screen.blit(enemyicon, (x,y))

running = True
while running:
    
    #RGB values (r, g, b)
    screen.fill((0,0,30))
    
    for event in pygame.event.get():
    
        #quits the game when the cross button is clicked
        if event.type == pygame.QUIT:
            running = False
            
        #checks whether any keystroke is pressed
        if event.type == pygame.KEYDOWN:
            
            #check if its left or right arrow key pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        
        #checks whether the keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    #adding boundaries to the player movement
    #1136 = 1200-64(size of playericon
    if playerX<=0:
        playerX=0
    elif playerX>=1136:
        playerX=1136
        
    
    playerX += playerX_change
    player(playerX,playerY)
    
    enemy(enemyX,enemyY)
    
    #update the screen to reflect the changes made in this while loop
    pygame.display.update()