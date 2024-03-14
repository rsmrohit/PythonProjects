from canvas import Canvas
import shapes as Shapes

from matplotlib import colors
import numpy as np

width = int(input("What is your desired Canvas width in pixels?\n"))
height = int(input("What is your desired Canvas height in pixels?\n"))
color = [255,255,255] if input("Should the canvas be white?\n").upper() == "YES" else [0,0,0]

canvas = Canvas(width, height, color)

while True:
    try:
        int(input("Type '0' to add a shape or type 'exit'\n"))
    except Exception:
        break
    
    r = Shapes.Rectangle(0,0)
    r.x = int(input("Starting position x: "))
    r.y = int(input("Starting position y: "))

    r.width = int(input("Shape width: "))
    r.height = int(input("Shape height: "))

    r.color = list(np.array(colors.to_rgb(input("Type a color: ")))*255)
    r.draw(canvas)

canvas.make_image("Cool_Picture.png")
