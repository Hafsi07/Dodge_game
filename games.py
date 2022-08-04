
from tkinter import *
import pygame
import random
import time 

pygame.init()
win=pygame.display.set_mode((500,501))
pygame.display.set_caption("Dodge game")
pygame.display.set_icon(pygame.image.load("V.png"))

y=50
x=50
mov=10

t=[500,500,500,500,500,500,500]
v=[True,True,True,True,True,True]
n=[0,0,0,0,0,0,0,0]
for i in range(0,6):
    n[i]=random.randrange(0,491)

bbb=pygame.image.load("DGB.png")

Hscore=0
score=0
tl=-1
k=0
hardness=60
ok=False
run=True
while run: 
    #basic sets
    pygame.time.delay(hardness)
    tl+=1
    k+=1
    win.fill((10,10,10))
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    win.blit(bbb,(0,0))
    #the turds // 50
    if v[0] and ok==False: 
        pygame.draw.rect(win,(255,0,0),(t[0],n[0],30,10))
        t[0]-=10
    if tl >=10 and v[1] and ok==False:
       pygame.draw.rect(win,(255,0,0),(t[1],n[1],30,10))
       t[1]-=10
    if tl >= 20 and v[2] and ok==False:
        pygame.draw.rect(win,(255,0,0),(t[2],n[2],30,10))
        t[2]-=10
    if tl >= 30 and v[3] and ok==False:
        pygame.draw.rect(win,(255,0,0),(t[3],n[3],30,10))
        t[3]-=10
    if tl >= 40 and v[4] and ok==False:
        pygame.draw.rect(win,(255,0,0),(t[4],n[4],30,10))
        t[4]-=10
    if tl >= 55 and v[5] and ok==False:
        pygame.draw.rect(win,(255,0,0),(t[5],n[5],30,10))
        t[5]-=10
    
    #resets
    for i in range(6):
        if t[i]==0:
            t[i]=500
            n[i]=random.randrange(y-100,y+100)
            v[i]=True
            score+=1 

    #game movements
    if y==0 :
        y=500
    elif y==500 or y==501 :
        y=0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x-=mov
    if keys[pygame.K_RIGHT] and x<500:
        x+=mov
    if keys[pygame.K_UP]:
        y-=mov
    if keys[pygame.K_DOWN]:
        y+=mov

    #drawing the shapes
    p=pygame.image.load("aha.png")
    p=pygame.transform.scale(p,(50,50))
    win.blit(p,(x,y))

    #score
    font = pygame.font.Font('freesansbold.ttf', 22)
    txt=font.render("score :",True,(255,255,255))
    tex=font.render(str(score),True,(255,255,255))
    win.blit(tex,(290,53))
    win.blit(txt,(210,50))

    #losing the game
    for i in range(6):
        if (t[i] in range(x+5,x+40)or t[i]+30 in range(x+5,x+47))  and (n[i] in range(y+17,y+35) or n[i]+10 in range(y+17,y+35)):
            ok=True
            if score>Hscore: 
                Hscore=score
            hardness=60
            if y <200:
                y+=200
            elif y>300:
                y-=200
            else:
                y+=200
        #if x+10 in range(t[i], t[i]+30) and (y in range(n[i],n[i]+10) or y+50 in  range(n[i],n[i]+10)):
         #   ok=True

    #hardness increase 
    if k % 70==0: 
        hardness-=3
    #replay    
    if keys[pygame.K_SPACE]: 
        ok=False
        score=0  
        k=0
        
    
    if not ok:
        pygame.display.update()
    else:
        fo=pygame.font.Font('freesansbold.ttf',20)
        te=fo.render("to play again press the space bar",False,(255,255,255))
        win.blit(te,(100,400))


#score calculation 
f=open("scores.txt","r")
ch=f.read() 
if Hscore> int(ch): 
    f.close() 
    f=open("scores.txt","w")
    f.write(str(Hscore))
f.close()
print(tl)
print(Hscore)
pygame.quit()
import main_menu_dodge_game.py
exec(main_menu_dodge_game.py)
