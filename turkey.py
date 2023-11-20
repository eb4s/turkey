speed(0)
penup()
left(90)
setpos(0,-200)




bgcolor("orange")


feather_up = 5
def draw_feather():
    pensize(1)
    pendown()
    for i in range(10):
        pendown()
        forward(feather_up)
        left(45)
        color(feather_color)
        forward(10)
        backward(10)
        right(45)
        penup()
        backward(feather_up)
        pendown()
        forward(feather_up)
        right(45)
        color(feather_color)
        forward(10)
        backward(10)
        left(45)
        penup()
    pensize(30)
    backward(50)
    color("brown")
    forward(50)
    backward(50)




def feather2():
    draw_feather()
    right(90)
    draw_feather()
    left(180)
    draw_feather()
def feather1():
    draw_feather()
def feather3():
    for i in range(3):
        draw_feather()
        forward(50)
   
    
def draw_turkey():
    
    #make body
    
    right(90)
    pensize(30)
    color("brown")
    begin_fill()
    circle(75)
    end_fill()
    left(90)
    penup()
    forward(145)
    right(90)
    pendown()
    begin_fill()
    circle(25)
    end_fill()
    pensize(5)
    penup()
    
    #make eyes
    
    color("white")
    left(90)
    forward(25)
    right(90)
    forward(15)
    begin_fill()
    circle(15)
    end_fill()
    left(90)
    forward(5)
    right(90)
    color("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()
    right(90)
    forward(5)
    left(90)
    color("white")
    backward(25)
    begin_fill()
    circle(15)
    end_fill()
    left(90)
    forward(5)
    right(90)
    color("black")
    begin_fill()
    circle(5)
    end_fill()
    penup()
    
    #draw the nose
    right(90)
    forward(25)
    left(90)
    forward(10)
    color("orange")
    pendown()
    begin_fill()
    circle(10, 360, 3)
    end_fill()
    
        




draw_turkey()

penup()
setpos(0,0)
left(90)




feather_color = input("what color would you like your feather?")
feather_pattern = input("what pattern would you like your feathers?, onehair, cross, long:")

if feather_pattern == "onehair":
    feather1()
if feather_pattern == "cross":
    feather2()
if feather_pattern == "long":
    feather3()


