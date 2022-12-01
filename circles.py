import turtle

def initalize(radius,x,y):
    turtle.speed(0)
    turtle.penup()
    turtle.color('firebrick')
    turtle.pencolor("firebrick")
    turtle.goto(x,y-radius)
    turtle.setheading(0)

def draw_circle(radius,extent):
    turtle.pendown()
    turtle.circle(radius,extent)
    turtle.penup()

def recurse_circle(radius,recursion_depth,x,y):
    i = recursion_depth-2
    j = 0
    k = 0
    while k<pow(4,recursion_depth-1):
        while j < 4:
            if i == recursion_depth-1:
                draw_circle(radius/pow(2,i),360)
                j+=1
                i-=1
                k+=1
            else:
                draw_circle(radius/pow(2,i),90)
                i+=1
        j=0
        i-=1
    #if turtle.ycor() != y-radius:
        #draw_circle(radius/pow(2,i),90)

def main():
    starting_x = 0
    starting_y = 0
    radius = 300
    recursion_depth = 1
    initalize(radius,0,0)
    # draw_circle(radius,2,0,0,0,0)
    recurse_circle(radius,recursion_depth,starting_x,starting_y)
    input('Type to end program: ')

main()