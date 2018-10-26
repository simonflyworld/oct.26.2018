x=0
slide = 0
def setup():
    global gallo_img
    global 
    size(640+x,480)
    gallo_img = loadImage("two ball.jpg")
    
def draw():
    background(255)
    fill(0)
    ellipse(100,100,30,30)
    image(gallo_img,50,50,100,100)
