class Circle:

    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.center = (x, y)
        self.radius = 10
        self.type = "circle"

        self.p = self.canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, fill="PaleVioletRed1", outline="")

    def update(self):
        pass