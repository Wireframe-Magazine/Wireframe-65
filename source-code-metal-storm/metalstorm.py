# Metal Storm
import pgzrun
from pygame import image

gunner = Actor('gunnerr01',(400,400))
gunner.direction = "r"
gunner.jump = 0
gunner.onground = False
gunner.gravity = 1
count = 0
mymap = image.load('images/map.png')
mapx = 0

def draw():
    drawBackground()
    drawForeground()
    gunner.draw()
    
def update():
    global count
    gunner.image = "gunner"+ gunner.direction + "0" + str(gunner.gravity)
    if keyboard.left:
        moveGunner(-2,0)
        gunner.direction = "l"
        gunner.image = "gunnerl"+ str(int(count/6)%3) + str(gunner.gravity)
    if keyboard.right:
        moveGunner(2,0)
        gunner.direction = "r"
        gunner.image = "gunnerr"+ str(int(count/6)%3) + str(gunner.gravity)
    checkGravity()
    if gunner.jump > 0:
        gunner.image = "gunner"+ gunner.direction + str(int(count/6)%3) + str(gunner.gravity)
    count += 1
    
def on_key_down(key):
    if key.name == "SPACE":
        if keyboard.up:
            gunner.gravity = gunner.gravity * -1
        else:
            if gunner.onground == True:
                gunner.jump = 18
            
def drawBackground():
    xoff = (mapx/2)%75
    for x in range(0,13):
        for y in range(0,8):
            screen.blit("block6",((x*75)-xoff,(y*75)))
            
def drawForeground():
    xoff = mapx%75
    for x in range(0,12):
        for y in range(0,8):
            pixel = mymap.get_at((int((mapx/75)+x),y))
            if pixel == (0, 255, 0, 255): screen.blit("block1",((x*75)-xoff,(y*75)))
            if pixel == (0, 100, 0, 255): screen.blit("block2",((x*75)-xoff,(y*75)))
            if pixel == (0, 150, 0, 255): screen.blit("block3",((x*75)-xoff,(y*75)))
            if pixel == (255, 255, 255, 255): screen.blit("block4",((x*75)-xoff,(y*75)))
            if pixel == (125, 125, 125, 255): screen.blit("block5",((x*75)-xoff,(y*75)))

def moveGunner(x,y):
    global mapx
    mx = int((mapx/75)+((gunner.x+x)/75))
    my = int((gunner.y/75))
    pixel = mymap.get_at((mx,my))
    if mapx+x < 6676 and mapx+x > 0 and gunner.x == 400:
        if pixel[0] > 0:
            mapx += x
    else:
        if pixel[0] > 0:
            gunner.x += x

def checkGravity():
    mx = int((mapx/75)+((gunner.x)/75))
    my = int((gunner.y/75)+(0.5*gunner.gravity))
    pixel = mymap.get_at((mx,my))
    if pixel[0] > 0:
        gunner.y += (5*gunner.gravity)
        gunner.onground = False
    else:
        gunner.onground = True
        if (gunner.y+(37*gunner.gravity))%75 != 0:
            gunner.y -= gunner.gravity
    if gunner.jump > 0:
        pixel = mymap.get_at((mx,my-(1*gunner.gravity)))
        if pixel[0] > 0:
            gunner.y -= (gunner.jump*gunner.gravity)
            gunner.jump -= 1
        else:
            gunner.jump = 0
    
pgzrun.go()
