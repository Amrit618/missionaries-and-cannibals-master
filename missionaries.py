import pygame
import time

pygame.init()
font = pygame.font.SysFont(None, 72)
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
display_width = 655
display_height = 433
FPS = 40
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('missionary and cannbals')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()
crashed = False
font = pygame.font.SysFont(None, 35)
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2 , display_height/2])

BGImg = pygame.image.load('bgpng.png')
boat = pygame.image.load('wood1.png')
cannibal1 = pygame.image.load('zomb1.png')
cannibal2 = pygame.image.load('zomb2.png')
cannibal3 = pygame.image.load('zomb3.png')
missionary1 = pygame.image.load('child1.png')
missionary2 = pygame.image.load('child2.png')
missionary3 = pygame.image.load('child3.png')

firstblack_x = 20
firstblack_y = 200
secondblack_x = 40
secondblack_y = 200
thirdblack_x = 60
thirdblack_y = 200
firstred_x = 20
firstred_y = 300
secondred_x = 40
secondred_y = 300
thirdred_x = 60
thirdred_y = 300
boatleft_x = 200
boatleft_y = 230


def background():
    gameDisplay.blit(BGImg, [0,0])

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_0:
                if boatleft_x == 200:
                    if firstblack_x == 20 and firstblack_y == 200:
                        if secondblack_x == 200 or thirdblack_x ==200 or firstred_x == 200 or secondred_x ==200 or thirdred_x ==200:
                            if secondblack_y != 260 or thirdblack_y !=260 or firstred_y != 260 or secondred_y !=260 or thirdred_y !=260:
                                firstblack_x = 200
                                firstblack_y = 260
                                print('first missionary on boat')
                                if secondblack_y == 260 or thirdblack_y ==260 or firstred_y == 260 or secondred_y ==260 or thirdred_y ==260:
                                    firstblack_x = 20
                                    firstblack_y = 200
                                    print('first missionary on boat')
                        else:
                            firstblack_x = 200
                            firstblack_y = 230
                            print('first missionary on boat')
            
            if event.key == pygame.K_1:
                if boatleft_x == 200:
                    if secondblack_x == 40 and secondblack_y == 200:
                        if firstblack_x == 200 or thirdblack_x == 200 or firstred_x == 200 or secondred_x ==200 or thirdred_x ==200:
                            if firstblack_y != 260 or thirdblack_y !=260 or firstred_y != 260 or secondred_y !=260 or thirdred_y !=260:
                                secondblack_x = 200
                                secondblack_y = 260
                                if firstblack_y == 260 or thirdblack_y ==260 or firstred_y == 260 or secondred_y ==260 or thirdred_y ==260:
                                    secondblack_x = 40
                                    secondblack_y = 200
                            
                        else:
                            secondblack_x = 200
                            secondblack_y = 230
                        
            if event.key == pygame.K_2:
                if boatleft_x == 200:
                    if thirdblack_x == 60 and thirdblack_y == 200:
                        if firstblack_x == 200 or secondblack_x == 200 or firstred_x == 200 or secondred_x ==200 or thirdred_x ==200:
                            if firstblack_y != 260 or secondblack_y !=260 or firstred_y != 260 or secondred_y !=260 or thirdred_y !=260:
                                thirdblack_x = 200
                                thirdblack_y = 260
                                if secondblack_y == 260 or firstblack_y ==260 or firstred_y == 260 or secondred_y ==260 or thirdred_y ==260:
                                    thirdblack_x = 60
                                    thirdblack_y = 200
                            
                        else:
                            thirdblack_x = 200
                            thirdblack_y = 230
            if event.key == pygame.K_3:
                if boatleft_x == 200:
                    if firstred_x == 20 and firstred_y == 300:
                        if firstblack_x == 200 or thirdblack_x ==200 or secondblack_x == 200 or secondred_x ==200 or thirdred_x ==200:
                            if firstblack_y != 260 or thirdblack_y !=260 or secondblack_y != 260 or secondred_y !=260 or thirdred_y !=260:
                                firstred_x = 200
                                firstred_y = 260
                                if secondblack_y == 260 or thirdblack_y ==260 or secondblack_y == 260 or secondred_y ==260 or thirdred_y ==260:
                                    firstred_x = 20
                                    firstred_y = 300
                            
                        else:
                            firstred_x = 200
                            firstred_y = 230
            if event.key == pygame.K_4:
                if boatleft_x == 200:
                    if secondred_x == 40 and secondred_y == 300:
                        if firstblack_x == 200 or thirdblack_x ==200 or firstred_x == 200 or secondblack_x ==200 or thirdred_x ==200:
                            if firstblack_y != 260 or thirdblack_y !=260 or firstred_y != 260 or secondblack_y !=260 or thirdred_y !=260:
                                secondred_x = 200
                                secondred_y = 260
                                if secondblack_y == 260 or thirdblack_y ==260 or firstred_y == 260 or secondblack_y ==260 or thirdred_y ==260:
                                    secondred_x = 40
                                    secondred_y = 300
                            
                        else:
                            secondred_x = 200
                            secondred_y = 230
            if event.key == pygame.K_5:
                if boatleft_x == 200:
                    if thirdred_x == 60 and thirdred_y == 300:
                        if firstblack_x == 200 or thirdblack_x ==200 or firstred_x == 200 or secondred_x ==200 or secondblack_x ==200:
                            if firstblack_y != 260 or thirdblack_y !=260 or firstred_y != 260 or secondred_y !=260 or secondblack_y !=260:
                                thirdred_x = 200
                                thirdred_y = 260
                                if secondblack_y == 260 or thirdblack_y ==260 or firstred_y == 260 or secondred_y ==260 or secondblack_y ==260:
                                    thirdred_x = 60
                                    thirdred_y = 300
                            
                        else:
                            thirdred_x = 200
                            thirdred_y = 230
            
                    
        if event.type == pygame.KEYDOWN:
            if boatleft_x == 200:
                if firstblack_y == 230  and firstblack_x == 200:
                    if event.key == pygame.K_UP:
                        firstblack_x = 20
                        firstblack_y = 200
                if firstblack_y == 260 and firstblack_x ==200:
                    if event.key == pygame.K_DOWN:
                        firstblack_x = 20
                        firstblack_y = 200
                    
                if secondblack_y == 230 and secondblack_x == 200:
                    if event.key == pygame.K_UP:
                        secondblack_x = 40
                        secondblack_y = 200
                if secondblack_y == 260 and secondblack_x == 200:
                    if event.key == pygame.K_DOWN:
                        secondblack_x = 40
                        secondblack_y = 200
                    
                if thirdblack_y == 230 and thirdblack_x == 200:
                    if event.key == pygame.K_UP:
                        thirdblack_x = 60
                        thirdblack_y = 200
                if thirdblack_y == 260 and thirdblack_x == 200:
                    if event.key == pygame.K_DOWN:
                        thirdblack_x = 60
                        thirdblack_y = 200
                    
                if firstred_y == 230 and firstred_x == 200:
                    if event.key == pygame.K_UP:
                        firstred_x = 20
                        firstred_y = 300
                if firstred_y == 260 and firstred_x == 200:
                    if event.key == pygame.K_DOWN:
                        firstred_x = 20
                        firstred_y = 300
                    
                if secondred_y == 230 and secondred_x == 200:
                    if event.key == pygame.K_UP:
                        secondred_x = 40
                        secondred_y = 300
                if secondred_y == 260 and secondred_x == 200:
                    if event.key == pygame.K_DOWN:
                        secondred_x = 40
                        secondred_y = 300
                    
                if thirdred_y == 230 and thirdred_x == 200:
                    if event.key == pygame.K_UP:
                        thirdred_x = 60
                        thirdred_y = 300
                if thirdred_y == 260 and thirdred_x == 200:
                    if event.key == pygame.K_DOWN:
                        thirdred_x = 60
                        thirdred_y = 300
                        break
            
                
                
        if event.type == pygame.KEYDOWN:
            if boatleft_x == 200:
                 if event.key == pygame.K_RIGHT:
                    if boatleft_x == 200 and boatleft_y ==230 or firstblack_y == 230 or firstback_y ==260 or secondblack_y ==230 or secondblack_y ==260 or thirdblack_y ==230 or thirdblack_y ==260 or firstred_y ==230 or firstred_y ==260 or secondred_y ==230 or secondred_y ==260 or thirdred_y ==230 or thirdred_y ==260:
                        if firstblack_x != 20 and firstblack_y == 230 or firstblack_y == 260:
                            if firstblack_y == 230:
                                firstblack_x = 400
                                firstblack_y = 230
                                
                                    
                            if firstblack_y == 260:
                                firstblack_x = 400
                                firstblack_y = 260

                            boatleft_x = 400
                            boatleft_y = 230
                    
                        if secondblack_x != 40 and secondblack_y == 230 or secondblack_y ==260:
                            if secondblack_y == 230:
                                secondblack_x = 400
                                secondblack_y = 230
                            if secondblack_y ==260:
                                secondblack_x = 400
                                secondblack_y = 260
                            boatleft_x = 400
                            boatleft_y = 230
                        if thirdblack_x != 60 and thirdblack_y == 230 or thirdblack_y == 260:
                            if thirdblack_y == 230:
                                thirdblack_x = 400
                                thirdblack_y = 230
                            if thirdblack_y == 260:
                                thirdblack_x = 400
                                thirdblack_y = 260
                            boatleft_x = 400
                            boatleft_y = 230
                        if firstred_x ==200 and firstred_y == 230 or firstred_y == 260:
                            if firstred_y == 230:
                                firstred_x = 400
                                firstred_y = 230
                            if firstred_y == 260:
                                firstred_x = 400
                                firstred_y = 260
                            boatleft_x = 400
                            boatleft_y = 230
                        if secondred_x ==200 and secondred_y ==230 or secondred_y == 260:
                            if secondred_y == 230:
                                secondred_x = 400
                                secondred_y = 230
                            if secondred_y == 260:
                                secondred_x = 400
                                secondred_y = 260
                            boatleft_x = 400
                            boatleft_y = 230
                        if thirdred_x ==200 and thirdred_y == 230 or thirdred_y == 260:
                            if thirdred_y == 230:
                                thirdred_x = 400
                                thirdred_y = 230
                            if thirdred_y == 260:
                                thirdred_x = 400
                                thirdred_y = 260
                            boatleft_x = 400
                            boatleft_y = 230
                            
                        if firstred_x == 20 and secondred_x == 40 and thirdred_x == 60:
                            if firstblack_x == 20 and secondblack_x !=40 and thirdblack_x !=60:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if secondblack_x == 40 and firstblack_x !=20 and thirdblack_x !=60:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if thirdblack_x == 60 and secondblack_x !=40 and firstblack_x !=60:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            else:
                                break
                        if (firstred_x == 20 and secondred_x == 40) or (firstred_x == 20 and thirdred_x == 60) or (firstred_x == 20 and thirdred_x == 60):
                            if firstblack_x == 20 and secondblack_x !=40 and thirdblack_x !=60:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if secondblack_x ==40 and firstblack_x !=20 and thirdblack_x !=60:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if thirdblack_x == 60 and firstblack_x !=20 and secondblack_x !=40:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                        
                        
                    
        
                    
        if event.type == pygame.KEYDOWN:
            if boatleft_x == 400 or firstblack_y == 230 or firstblack_y ==260 or secondblack_y ==230 or secondblack_y ==260 or thirdblack_y ==230 or thirdblack_y ==260 or firstred_y ==230 or firstred_y ==260 or secondred_y ==230 or secondred_y ==260 or thirdred_y ==230 or thirdred_y ==260:
                if event.key == pygame.K_UP:
                    if firstblack_y == 230:
                        firstblack_x = 500
                        firstblack_y = 200
                    if secondblack_y == 230:
                        secondblack_x = 520
                        secondblack_y = 200
                    if thirdblack_y == 230:
                        thirdblack_x = 540
                        thirdblack_y = 200
                    if firstred_y == 230:
                        firstred_x = 500
                        firstred_y = 300
                    if secondred_y ==230:
                        secondred_x = 520
                        secondred_y = 300
                    if thirdred_y == 230:
                        thirdred_x = 540
                        thirdred_y = 300
                    
                if event.key == pygame.K_DOWN:
                    if firstblack_y == 260:
                        firstblack_x = 500
                        firtblack_y = 200
                    if secondblack_y == 260:
                        secondblack_x = 520
                        secondblack_y = 200
                    if thirdblack_y == 260:
                        thirdblack_x = 540
                        thirdblack_y = 200
                    if firstred_y == 260:
                        firstred_x = 500
                        firstred_y = 300
                    if secondred_y == 260:
                        secondred_x = 520
                        secondred_y = 300
                    if thirdred_y == 260:
                        thirdred_x = 540
                        thirdred_y = 300
                
                            
                        boatleft_x = 400
                        boatleft_y = 230
                    else:
                        boatleft_x = 400
                        boatleft_y = 230
                    
        if event.type == pygame.KEYDOWN:
            if boatleft_x == 400:
                if firstblack_x == 500:
                    if event.key == pygame.K_0:
                        if firstblack_x == 500 and firstblack_y == 200:
                            if secondblack_y == 230 or thirdblack_y == 230 or firstred_y == 230 or secondred_y == 230 or thirdred_y ==230:
                                if secondblack_y != 260 or thirdblack_y != 260 or firstred_y != 260 or secondred_y != 260 or thirdred_y !=260:

                                    firstblack_x = 400
                                    firstblack_y = 260
                                if secondblack_y == 260 or thirdblack_y == 260 or firstred_y == 260 or secondred_y == 260 or thirdred_y ==260:
                                    firstblack_x = 500
                                    firstblack_y =200

                        
                            else:
                                firstblack_x = 400
                                firstblack_y = 230
                if secondblack_x == 520:
                    if event.key == pygame.K_1:
                        if secondblack_x == 520 and secondblack_y == 200:
                            if firstblack_y == 230 or thirdblack_y == 230 or firstred_y == 230 or secondred_y == 230 or thirdred_y ==230:
                                if firstblack_y != 260 or thirdblack_y != 260 or firstred_y != 260 or secondred_y != 260 or thirdred_y !=260:

                                    secondblack_x = 400
                                    secondblack_y = 260
                                if firstblack_y == 260 or thirdblack_y == 260 or firstred_y == 260 or secondred_y == 260 or thirdred_y ==260:
                                    secondblack_x = 520
                                    secondblack_y = 200

                            else:
                                secondblack_x = 400
                                secondblack_y = 230
                if thirdblack_x == 540:
                    if event.key == pygame.K_2:
                        if thirdblack_x == 540 and thirdblack_y == 200:
                            if secondblack_y == 230 or firstblack_x == 230 or firstred_x == 230 or secondred_x == 230 or thirdred_x ==230:
                                if secondblack_y != 260 or firstblack_x != 260 or firstred_x != 260 or secondred_x != 230 or thirdred_x !=260:
                                    thirdblack_x = 400
                                    thirdblack_y = 260
                                if secondblack_y == 260 or firstblack_x == 260 or firstred_x == 260 or secondred_x == 260 or thirdred_x ==260:
                                    thirdblack_x = 400
                                    thirdblack_y = 260
                            else:
                                thirdblack_x = 400
                                thirdblack_y = 230
                if firstred_x == 500:
                    if event.key == pygame.K_3:
                        if firstred_x == 500 and firstred_y == 300:
                            if secondblack_y == 230 or thirdblack_y == 230 or firstblack_y == 230 or secondred_y == 230 or thirdred_y ==230:
                                if secondblack_y != 230 or thirdblack_y != 230 or firstblack_y != 230 or secondred_y != 230 or thirdred_y !=230:
                                    firstred_x = 400
                                    firstred_y = 260
                                if secondblack_y == 260 or thirdblack_y == 260 or firstblack_y == 260 or secondred_y == 260 or thirdred_y ==260:
                                    firstred_x = 500
                                    firstred_y = 300
                            else:
                                firstred_x = 400
                                firstred_y = 230
                if secondred_x == 520:
                    if event.key == pygame.K_4:
                        if secondred_x == 520 and secondred_y == 300:
                            if secondblack_y == 230 or thirdblack_y == 230 or firstred_y == 230 or firstblack_y == 230 or thirdred_y ==230:
                                if secondblack_y != 260 or thirdblack_y != 260 or firstred_y != 260 or firstblack_y != 260 or thirdred_y !=260:
                                    secondred_x = 400
                                    secondred_y = 260
                                if secondblack_y == 260 or thirdblack_y == 260 or firstred_y == 260 or firstblack_y == 260 or thirdred_y ==260:
                        
                                    secondred_x = 520
                                    secondred_y = 300
                            else:
                                secondred_x = 400
                                secondred_y = 230
                if thirdred_x == 540:
                    if event.key == pygame.K_5:
                        if secondblack_y == 230 or thirdblack_y == 230 or firstred_y == 230 or secondred_y == 230 or firstblack_y ==230:
                            if secondblack_y != 260 or thirdblack_y != 260 or firstred_y != 260 or secondred_y != 260 or firstblack_y !=260:
                        
                                thirdred_x = 400
                                thirdred_y = 260
                            if secondblack_y == 260 or thirdblack_y == 260 or firstred_y == 260 or secondred_y == 260 or firstblack_y ==260:
                                thirdred_x = 540
                                thirdred_y = 300
                        else:
                            thirdred_x = 400
                            thirdred_y = 230
                        
        if event.type == pygame.KEYDOWN:
            if boatleft_x == 400:
                 if event.key == pygame.K_LEFT:
                    if boatleft_x == 400 and boatleft_y ==230 or firstblack_y == 230 or firstback_y ==260 or secondblack_y ==230 or secondblack_y ==260 or thirdblack_y ==230 or thirdblack_y ==260 or firstred_y ==230 or firstred_y ==260 or secondred_y ==230 or secondred_y ==260 or thirdred_y ==230 or thirdred_y ==260:
                        if firstblack_x != 20 and firstblack_y == 230 or firstblack_y == 260:
                            if firstblack_y == 230:
                                firstblack_x = 200
                                firstblack_y = 230
                                
                                    
                            if firstblack_y == 260:
                                firstblack_x = 200
                                firstblack_y = 260

                            boatleft_x = 200
                            boatleft_y = 230
                    
                        if secondblack_x != 40 and secondblack_y == 230 or secondblack_y ==260:
                            if secondblack_y == 230:
                                secondblack_x = 200
                                secondblack_y = 230
                            if secondblack_y ==260:
                                secondblack_x = 200
                                secondblack_y = 260
                            boatleft_x = 200
                            boatleft_y = 230
                        if thirdblack_x != 60 and thirdblack_y == 230 or thirdblack_y == 260:
                            if thirdblack_y == 230:
                                thirdblack_x = 200
                                thirdblack_y = 230
                            if thirdblack_y == 260:
                                thirdblack_x = 200
                                thirdblack_y = 260
                            boatleft_x = 200
                            boatleft_y = 230
                        if firstred_x !=20 and firstred_y == 230 or firstred_y == 260:
                            if firstred_y == 230:
                                firstred_x = 200
                                firstred_y = 230
                            if firstred_y == 260:
                                firstred_x = 200
                                firstred_y = 260
                            boatleft_x = 200
                            boatleft_y = 230
                        if secondred_x !=40 and secondred_y ==230 or secondred_y == 260:
                            if secondred_y == 230:
                                secondred_x = 200
                                secondred_y = 230
                            if secondred_y == 260:
                                secondred_x = 200
                                secondred_y = 260
                            boatleft_x = 200
                            boatleft_y = 230
                        if thirdred_x !=60 and thirdred_y == 230 or thirdred_y == 260:
                            if thirdred_y == 230:
                                thirdred_x = 200
                                thirdred_y = 230
                            if thirdred_y == 260:
                                thirdred_x = 200
                                thirdred_y = 260
                            boatleft_x = 200
                            boatleft_y = 230
                        if firstred_x == 500 and secondred_x == 520 and thirdred_x == 540:
                            if firstblack_x == 500 and secondblack_x != 520 and thirdblack_x !=540:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if secondblack_x == 520 and firstblack_x !=500 and thirdblack_x !=540:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if thirdblack_x == 540 and firstblack_x !=500 and secondblack_x !=520:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                        if (firstred_x == 500 and secondred_x == 520) or (firstred_x == 500 and thirdred_x == 540) or (firstred_x == 500 and thirdred_x == 540):
                            if firstblack_x == 500 and secondblack_x !=520 and thirdblack_x !=540:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if secondblack_x ==520 and firstblack_x !=500 and thirdblack_x !=540:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                            if thirdblack_x == 540 and firstblack_x !=500 and secondblack_x !=530:
                                message_to_screen("Game Over",red)
                                pygame.display.update()
                                time.sleep(2)
                                crashed = True
                        if firstred_x == 500 and secondred_x == 520 and thirdred_x == 500 and firstblack_x == 500 and secondblack_x == 520 and thirdblack_x == 540:
                            message_to_screen("You win",red)
                            pygame.display.update()
                            time.sleep(2)
                            crashed = True
        
            

    gameDisplay.fill(white)
    
    background()

    
    gameDisplay.blit(boat , [boatleft_x,boatleft_y,70,80])
    textsurface = myfont.render('0', False, (255, 0, 239))
    gameDisplay.blit(missionary1,[firstblack_x,firstblack_y,20,20])
    gameDisplay.blit(textsurface,(firstblack_x+15,firstblack_y-18))
    textsurface = myfont.render('1', False, (255, 0, 239))
    gameDisplay.blit(missionary2,[secondblack_x,secondblack_y,20,20])
    gameDisplay.blit(textsurface,(secondblack_x+15,secondblack_y-17))
    textsurface = myfont.render('2', False, (255, 0, 239))
    gameDisplay.blit(missionary3,[thirdblack_x,thirdblack_y,20,20])
    gameDisplay.blit(textsurface,(thirdblack_x+15,thirdblack_y-32))
    textsurface = myfont.render('3', False, (252, 11, 11))
    gameDisplay.blit(cannibal1,[firstred_x,firstred_y,20,20])
    gameDisplay.blit(textsurface,(firstred_x+15,firstred_y-29))
    textsurface = myfont.render('4', False, (252, 11, 11))
    gameDisplay.blit(cannibal2,[secondred_x,secondred_y,20,20])
    gameDisplay.blit(textsurface,(secondred_x+15,secondred_y-25))
    textsurface = myfont.render('5', False, (252, 11, 11))
    gameDisplay.blit(cannibal3,[thirdred_x,thirdred_y,20,20])
    gameDisplay.blit(textsurface,(thirdred_x+15,thirdred_y-27))
    
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
