r=500
k=0
s=0

def setup():
    size(r*2+10,r*2+10)
    stroke(255)
    background(255)
    tot=0
    

    
    
def draw():
    
    global k
    global s
    
    translate(width/2, height/2)
    stroke(225)
    strokeWeight(3)
    noFill()
    circle(0,0,r*2)
    
    rectMode(CENTER)
    rect(0,0,r*2,r*2)
    
    for i in range(10000):
        x=random(-r,r)
        y=random(-r,r)
        point(x,y)
        k+=1.0  
        if x*x+y*y<=r*r:
            stroke(255,0,0)
            s+=1.0
        else:
            stroke(0)
        point(x,y)    
    
    print(4*(s/k))
    
