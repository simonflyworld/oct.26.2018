x=0
slide = 0
def setup():
    size(640,480)

def draw():
    global x
    global slide
    x+=50
    text("fuck you",x,50)
    if frameCount %(60*3)==0:
        slide += 1
        if slide>=4:
            slide=0
    if slide ==0:
       background(0,255,0)
    elif slide == 1:
        background(255,0,0)
    elif slide == 2:
        background(0,0,255)
    elif slide == 3:
        background(40,255,225)
   
def mousePressed():
    global slide
    slide += 1
    if slide >= 4:
        slide = 0
