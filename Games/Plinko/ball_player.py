from collision import Collision_2D as collider
from math import sqrt
class Player:

    def __init__(self, canvas, x, y, arena):

        self.canvas = canvas
        self.center = (x, y)
        self.radius = 10
        self.y = 0
        self.x = 0

        self.last_position = (0, 0)

        # Arena is the sides of the wall which have a different collision calculation
        self.arena = arena

        # Control the ball at the top using cursor
        self.cursor_move = True
        self.canvas.bind('<Motion>', self.cursor)
        self.canvas.bind('<Button-1>', self.cursor)

        # Ball at the top is created and moved with cursor
        self.p = self.canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, fill="Magenta2", outline="Magenta4", width=3)
    
    # When cursor event is true - ball controlled by cursor position
    def cursor(self, event=None):
        # If Mouse button detected then remove the cursor move event
        # Let the ball fall
        if int(event.type) == 4:
            self.cursor_move = False
            return
        
        # Compensate for the radius
        self.last_position = (event.x-self.radius, event.y)
        
        if not self.cursor_move:
            return
        
        arena_coords = self.canvas.coords(self.arena)
        self.canvas.moveto(self.p, min(max(event.x - self.radius, arena_coords[0]), arena_coords[2]-2-self.radius*2), 100)

    def check_collision(self, obstacles):
        conversion = 0.8 # Amount of energy passed on
        for obstacle in obstacles:
            if obstacle.type == "circle" and collider.is_overlapping_2Circle(self, obstacle):

                # Magnitude of velocity (Velocity conserved)
                magnitude = sqrt(self.x**2 + self.y**2) * conversion
                # direction_momentum = (self.y/magnitude) / (self.x/magnitude)
                # Direction in which the centers of both lie
                ratio = (self.center[0]-obstacle.center[0], self.center[1]-obstacle.center[1])
                ratio_total = abs(ratio[0]) + abs(ratio[1])

                # I think here is the problem - if the direction (self.x and self.y) the ball is going
                # is AWAY from the ball it is in collision with, then skip
                # NAH CHECK THE SLOPE
                # Previous issue was that I checked individual component for some reason

                #SO # PERFECT SOLUTION WORKED
                try:
                    if abs((self.y/self.x) - (ratio[1]/ratio[0])) < 0.01:
                        return
                except:
                    pass # Straight case

                # Redistribute magnitude to both directions
                self.x = (magnitude)*ratio[0]/ratio_total
                self.y = (magnitude)*ratio[1]/ratio_total

                
        
        arena_coords = self.canvas.coords(self.arena)
        player_coords = self.canvas.coords(self.p)
        if player_coords[0] < arena_coords[0] and self.x < 0:
            self.x = -self.x*0.8
        if player_coords[2] > arena_coords[2] and self.x > 0:
            self.x = -self.x*0.8
        if player_coords[1] > arena_coords[3]:
            self.replace()
    
    def replace(self):
        self.canvas.delete(self.p)
        lx, ly = self.last_position
        ly = 100
        self.p = self.canvas.create_oval(lx-self.radius, ly-self.radius, lx+self.radius, ly+self.radius, fill="Magenta2", outline="Magenta4", width=3)
        self.y = 0
        self.x = 0
        self.cursor_move = True

    def calc_center(self):
        # Get cords and then return the midpoint of both
        coords = self.canvas.coords(self.p)

        mid = lambda a, b: (a+b)/2
        self.center = (mid(coords[0], coords[2]), mid(coords[1], coords[3]))

    def update(self, obstacles):
        if self.cursor_move:
            return
        self.y+=0.2
        self.check_collision(obstacles)
        self.canvas.move(self.p, self.x, self.y)
        self.calc_center()
