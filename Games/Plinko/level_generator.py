from ball_obstacle import Circle
from tkinter import *
from collision import Collision_2D as collider
from levels import levels

class Level:

    def __init__(self, canvas, create=False):

        self.canvas = canvas
        self.obstacles = []
        if create:
            self.canvas.bind('<Button-1>', self.place)
            self.canvas.bind('<Shift_L>', self.delete)
            self.canvas.bind('<Motion>', self.prev)
            self.preview = Circle(canvas, 600, 300)
            return
        self.create_obstacles()   

    def create_obstacles(self):
        obstacles = levels[0]
        self.obstacles = [
            Circle(self.canvas, coord[0], coord[1]) for coord in obstacles
        ]

    def delete(self, event=None):
        arena_coords = self.canvas.coords(arena)

        event.x = min(max(event.x + 4, arena_coords[0]), arena_coords[2]-2-5*2)
        event.y = min(max(event.y + 4, arena_coords[1]), arena_coords[3]-2-5*2)

        event.x -= event.x%10
        event.y -= event.y%10
        
        for o in self.obstacles:
            if collider.is_overlapping_2CircleGeneral([10, o.center], [10, (event.x, event.y)]):
                self.obstacles.remove(o)
                self.canvas.delete(o.p)
                break

    def prev(self, event=None):
        arena_coords = self.canvas.coords(arena)

        event.x = min(max(event.x + 4, arena_coords[0]), arena_coords[2]-2-5*2)
        event.y = min(max(event.y + 4, arena_coords[1]), arena_coords[3]-2-5*2)

        event.x -= event.x%10
        event.y -= event.y%10

        self.canvas.moveto(self.preview.p, event.x-10, event.y-10)

    def place(self, event=None):
        arena_coords = self.canvas.coords(arena)

        event.x = min(max(event.x + 4, arena_coords[0]), arena_coords[2]-2-5*2)
        event.y = min(max(event.y + 4, arena_coords[1]), arena_coords[3]-2-5*2)

        event.x -= event.x%10
        event.y -= event.y%10
        
        for o in self.obstacles:
            if collider.is_overlapping_2CircleGeneral([10, o.center], [10, (event.x, event.y)]): 
                return
        self.obstacles.append(Circle(self.canvas, event.x, event.y))

    def update(self):
        self.canvas.after(15, self.update)
 
def create_arena(canvas):
        # Left Wall
        width = 50
        a = arena_w/2
        h = arena_h/2
        return canvas.create_rectangle(WIDTH/2 - a, HEIGHT/2 - h, WIDTH/2 + a, HEIGHT/2 + h, width=width, outline="", fill="navy")

if __name__ == "__main__":
    WIDTH, HEIGHT = 1200, 800
    arena_w, arena_h = 600, 700
    CLOCK_RATE = 15

    tk = Tk()
    tk.title('Plinko Level builder')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)

    # Create Background
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="RosyBrown1")

    canvas.config(cursor="plus")

    # Create Arena
    arena = create_arena(canvas)
    game = Level(canvas, True)
    canvas.pack()
    canvas.focus_force()
    mainloop()
    print([o.center for o in game.obstacles])
