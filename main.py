from turtle import *
color('green')
bgcolor('black')
b = 200
s = 1
speed(s)
while b > 0:
    left(b)
    forward(b*3)
    b -= 1
    s += 5
    if s >= 10:
        speed(s)
mainloop()