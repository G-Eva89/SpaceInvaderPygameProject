import pygame
from pygame import mixer

import random
import math

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

#player score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#game over
game_over_font = pygame.font.Font('freesansbold.ttf',64)


#adding player to the game
playericon = pygame.image.load("spaceship.png")

#initial coordinates to the position of player
playerX = 364   #800/2 - 64/2; 64 is the pixel size of playericon
playerY = 480   
playerX_change = 0


#adding enemy to the game
enemyicon = pygame.image.load("alien.png")
enemies = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

#initial coordinates to the position of enemy
for i in range(no_of_enemies):
    enemies.append(enemyicon)
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(64,300))
    enemyX_change.append(0.4)
    enemyY_change.append(20)


#adding bullet to the game
bulleticon = pygame.image.load("bullet.png")

#initial coordinates to the position of bullet
bulletX = 0
bulletY = 480  
bulletX_change = 0
bulletY_change = 1
#"ready" - bullet is not visible on screen; "fire" - bullet is moving
bullet_state = "ready"


#adding score to the screen
def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

#creating a player
def player(x,y):
    #draws the image of player at the given coordinates
    screen.blit(playericon, (x,y))
    
#creating an enemy
def enemy(x,y,i):
    #draws the image of enemy at the given coordinates
    screen.blit(enemies[i], (x,y))
    
#creating a bullet
def fire_bullet(x,y):
    #mkae this global variable so that we can check if the bullet is fired or not
    global bullet_state
    bullet_state = "fire"
    #the bullet is coming out from the front centre of the film 
    screen.blit(bulleticon,(x+16,y+10))
    
#checking for collision
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt( math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2) )    
    if distance < 27:
        return True
    else:
        return False

#game over condition
def game_over():
    game_over_text = game_over_font.render("OOPS! GAME OVER!", True, (255,255,255))
    screen.blit(game_over_text, (200,250))

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
                playerX_change = -0.7
            
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            
            #check if space is pressed to fire a bullet
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":         #shouldnt be able to fire a bullet once youve already fired a bullet
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
        
        #checks whether the keystroke has been released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    
    #adding boundaries to the player movement
    #736 = 800-64(size of playericon)
    playerX += playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    
    #for every enemy-
    for i in range(no_of_enemies):
    
        #GAME OVER condition
        if enemyY[i]>440 :
            for j in range(no_of_enemies):
                enemyY[j] = 1000
            game_over()
            break

        #adding boundaries to the enemy movement
        #736 = 800-64(size of enemyicon)
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.4
            enemyY[i] += enemyY_change[i]
 
        #check whether the bullet has collided with the enemy
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480           #reset bullet
            bullet_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(32,300)
            bullet_hit = mixer.Sound("explosion.wav")
            bullet_hit.play()
        
        #draw enemy on screen
        enemy(enemyX[i],enemyY[i],i)
    
    #bullet movement
    if bulletY <= 0:            #once bullet reaches the end of screen, another bullet can be fired
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":          #once the bullet is fired, it should move up
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    
    
    #draw player on screen
    player(playerX,playerY)   
    
    #draw the score on screen
    show_score(textX,textY)
    
    #update the screen to reflect the changes made in this while loop
    pygame.display.update()