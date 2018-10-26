x=0
def setup():
    size(800,600)
    background(0,225,0)
def draw():
    global x
    x=x+5
    ellipse(x,100,30,89)
    ellipse(x,50,30,90)
