class Rectangle:

    def __init__(self, x, y, width=1, height=1, color=[0, 0, 0]) -> None:
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x+self.width, self.y:self.y+self.height] = self.color