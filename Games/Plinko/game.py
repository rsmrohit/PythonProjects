from tkinter import *
import tkinter.font as font
import time
from ball_player import Player
from level_generator import Level
from PIL import Image, ImageTk

WIDTH, HEIGHT = 1200, 800
arena_w, arena_h = 600, 700
CLOCK_RATE = 15

class Game:
    images = []

    def __init__(self, canvas):
        self.starttime = time.time()
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        
        # Create Background
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="RosyBrown1")

        # Create Arena
        self.arena = self.create_arena(self.canvas)

        # Checking Pause
        self.pause = False
        self.pause_text = None
        self.pause_rect = None
        
        self.level = Level(self.canvas)
        self.player = Player(self.canvas, 599, 100, self.arena)
        self.canvas.after(CLOCK_RATE, self.update)
        self.button = Button(self.canvas, width=10, height=5, text="Next Stage", bg="white")
        self.button.place(x=100, y=100)
    
    def create_arena(self, canvas):
        # Left Wall
        width = 50
        a = arena_w/2
        h = arena_h/2
        return canvas.create_rectangle(WIDTH/2 - a, HEIGHT/2 - h, WIDTH/2 + a, HEIGHT/2 + h, width=width, outline="", fill="navy")

    def pause(self, event=None):
        self.pause = (self.pause == False)
        if not self.pause:
            self.canvas.delete(self.pause_text)
            self.canvas.delete(self.pause_rect)
            Game.images.pop()
            self.canvas.after(CLOCK_RATE, self.update)

    def update(self):
        # If paused just return dont do anything
        if self.pause:
            self.pause_rect = self.create_rectangle(0, 0, WIDTH, HEIGHT, alpha=0.5, fill="white")
            self.pause_text = self.canvas.create_text(300, 200, text = "PAUSED", font = font.Font(family='Helveca', size='100', weight='bold'))
            return
        self.player.update(self.level.obstacles)
        self.canvas.after(CLOCK_RATE, self.update)

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = canvas.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            Game.images.append(ImageTk.PhotoImage(image))
            return canvas.create_image(x1, y1, image=Game.images[-1], anchor='nw')
        else:
            kwargs.pop('alpha')
        return self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
        

if __name__ == '__main__':
    tk = Tk()
    tk.title('Plinko')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    game = Game(canvas)
    canvas.focus_force()
    mainloop()