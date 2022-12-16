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
    i = recursion_depth-1
    j = 0
    k = 0
    while k<pow(4,recursion_depth-1):
        while j < 4 and k<pow(4,recursion_depth-1):
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
        while i == 0:
            draw_circle(radius/pow(2,i+1),90)
            i+=1
        i = recursion_depth-1

def recurse_circle2(radius,recursion_depth):
    i = []
    while len(i)<recursion_depth:
        i.append(0)
    j = recursion_depth-1
    while i[0]<1:
        while i[j]<4:
            draw_circle(radius/pow(2,j),360)
            i[j]+=1
            if i[0]==1:
                break
            j-=1
            draw_circle(radius/pow(2,j),90)
            j+=1
        i[j]=0
        j-=1
        i[j]+=1
    #if turtle.ycor() != y-radius:
        #draw_circle(radius/pow(2,i),90)

def recurse_circle3(radius,recursion_max,recursion_depth):
    r = recursion_depth
    i = 0
    if recursion_max == 0:
        draw_circle(radius,360)
        return 0
    while i < 4:
        if r < recursion_max:
            r+=1
            recurse_circle3(radius,recursion_max,r)
            r-=1
        draw_circle(radius/pow(2,r),360)
        draw_circle(radius/pow(2,r-1),90)
        i+=1
    
        

def main():
    starting_x = 0
    starting_y = 0
    radius = 300
    recursion_max = 4
    initalize(radius,0,0)
    # draw_circle(radius,2,0,0,0,0)
    # recurse_circle(radius,recursion_max,starting_x,starting_y)
    # recurse_circle2(radius,recursion_max)
    recurse_circle3(radius,recursion_max,1)
    input('Type to end program: ')

main()