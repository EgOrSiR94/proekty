z =1
x =1
c =1
def setup():
    size(1000,1000)
def draw():
    global z,x,c
    background(70, 130, 180)
    ellipse(z,x,c,z)
    img = loadImage("j.jpg")
    image(img,mouseX ,mouseY, 300, 200 )
    print("%d : %d" % (mouseX, pmouseY))
    z +=1
    x -=1
    c +=1
