import pygame
import datetime
import random

pygame.init()

pygame.mixer.music.load('letIt.mp3')
pygame.mixer.music.play(-1)

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
screen = pygame.display.set_mode((900, 600))

#Title and Icon
pygame.display.set_caption("Christmas are this close!")
icon = pygame.image.load('santa-claus.png')
pygame.display.set_icon(icon)

#Tree
treeImg = pygame.image.load('tree.png')
treeX = 100
treeY = 340

def tree():
    screen.blit(treeImg,(treeX,treeY))


font = pygame.font.Font('Pacifico.ttf', 60)
textX = 100
textY = 100

#=========Countdown===============
def countdown():
    futuredate = datetime.datetime.strptime('Dec 24 2020  00:00', '%b %d %Y %H:%M')
    nowdate = datetime.datetime.now()
    count = int((futuredate-nowdate).total_seconds())

    days = count//86400
    hours = (count-days*86400)//3600
    minutes = (count-days*86400-hours*3600)//60
    seconds = count-days*86400-hours*3600-minutes*60
    days = font.render(str(days) + " days ", True, (255,255,255))
    screen.blit(days,(textX + 250,textY))
    time = font.render(str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) 
    + " seconds", True, WHITE)
    screen.blit(time,(textX,(textY+90)))



snow_list=[]
for i in range(200):
        x = random.randrange(0, 600)
        y = random.randrange(0, 900)
        snow_list.append([x,y])

clock = pygame.time.Clock()



#Game Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 153, 76))
    tree()
    countdown()

    for point in snow_list:
        point[1]+=1
        pygame.draw.circle(screen, WHITE, point, 2)

        if(point[1] >= 900):
            point[0] = random.randrange(0, 900)
            point[1] = random.randrange(-10, -5)

    pygame.display.flip()
    clock.tick(50)

    pygame.display.update()
