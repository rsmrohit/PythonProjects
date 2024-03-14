from math import sqrt
class Collision_2D:

    def distance(coord1, coord2):
        return sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)

    # Helper class where objects are tuples with coords x1, y1, x2, y2
    # Or top left corner top right corner will tell you if given object is in the bounding box of the other
    def is_overlapping_2Rect(obj1, obj2):
        overlap = True
        x1, y1, x2, y2 = obj1
        X1, Y1, X2, Y2 = obj2

        # If one rectangle is on left or right side
        if (x1 >= X2) or (X1 >= x2):
            overlap = False
        
        # If one rectangle is on top or bottom
        if (y1 >= Y2) or (Y1 >= y2):
            overlap = False
        
        return overlap
    
    def is_overlapping_2Circle(circ1, circ2):
        overlap = False
        min_distance = circ1.radius + circ2.radius
        
        if Collision_2D.distance(circ1.center, circ2.center) < min_distance:
            overlap = True
        return overlap
        
    def is_overlapping_2CircleGeneral(circ1, circ2):
        overlap = False
        min_distance = circ1[0] + circ2[0]
        
        if Collision_2D.distance(circ1[1], circ2[1]) < min_distance:
            overlap = True
        return overlap
