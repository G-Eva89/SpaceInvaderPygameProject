import pygame
import random

#initialize pygame
pygame.init()

#creating a screen
#(width, height)
screen = pygame.display.set_mode((800,600))

#adding title, icon and background to the screen
pygame.display.set_caption("Space Invaders")
gameicon = pygame.image.load("spacetravel.png")
pygame.display.set_icon(gameicon)
background = pygame.image.load("background.jpg")


#adding player to the game
playericon = pygame.image.load("spaceship.png")
#initial coordinates to the position of player
playerX = 364   #1200/2 - 64/2; 64 is the pixel size of playericon
playerY = 480   
playerX_change = 0


#adding enemy to the game
enemyicon = pygame.image.load("alien.png")
#initial coordinates to the position of enemy
enemyX = random.randint(0,736)
enemyY = random.randint(0,300)   
enemyX_change = 0.3
enemyY_change = 40


#adding bullet to the game
bulleticon = pygame.image.load("bullet.png")
#initial coordinates to the position of bullet
bulletX = 0
bulletY = 480  
bulletX_change = 0
bulletY_change = 0.5
#"ready" - bullet is not visible on screen; "fire" - bullet is moving
bullet_state = "ready"


#creating a player
def player(x,y):
    #draws the image of player at the given coordinates
    screen.blit(playericon, (x,y))
    
#creating an enemy
def enemy(x,y):
    #draws the image of enemy at the given coordinates
    screen.blit(enemyicon, (x,y))
    
#creating a bullet
def fire_bullet(x,y):
    #mkae this global variable so that we can check if the bullet is fired or not
    global bullet_state
    bullet_state = "fire"
    #the bullet is coming out from the front centre of the film 
    screen.blit(bulleticon,(x+16,y+10))
    

running = True
while running:
    
    #RGB values (r, g, b)
    screen.fill((0,0,30))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
    
        #quits the game when the cross button is clicked
        if event.type == pygame.QUIT:
            running = False
            
        #checks whether any keystroke is pressed
        if event.type == pygame.KEYDOWN:
            
            #check if its left or right arrow key pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            
            #check if space is pressed to fire a bullet
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":         #shouldnt be able to fire a bullet once youve already fired a bullet
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        
        #checks whether the keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    #adding boundaries to the player movement
    #1136 = 1200-64(size of playericon)
    playerX += playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    
    #adding boundaries to the enemy movement
    #1136 = 1200-64(size of enemyicon)
    enemyX += enemyX_change
    if enemyX<=0:
        enemyX_change=0.3
        enemyY += enemyY_change
    elif enemyX>=736:
        enemyX_change=-0.3
        enemyY += enemyY_change
    
    #bullet movement
    if bulletY <= 0:            #once bullet reaches the end of screen, another bullet can be fired
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state is "fire":          #once the bullet is fired, it should move up
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    
    player(playerX,playerY)   
    enemy(enemyX,enemyY)
    
    #update the screen to reflect the changes made in this while loop
    pygame.display.update()