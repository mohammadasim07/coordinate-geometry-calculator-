class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return '[x = {}, y = {}]'.format(self.x_cod,self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5


    def distance_from_origin(self):
        return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
    
    def midpoint_of_two_point(self,other):
        x_mid = (self.x_cod + other.x_cod)/2
        y_mid = (self.y_cod + other.y_cod)/2
        return (x_mid,y_mid)
    
    def reflection_across_x_axis(self):
        return (self.x_cod,-self.y_cod)
    
    def reflection_across_y_axis(self):
        return (-self.x_cod,self.y_cod)
    
    def slope(self,other):
        if other.x_cod - self.x_cod == 0:
            return "The slope is undefined (vertical line)."
        else:
            return (other.y_cod - self.y_cod)/(other.x_cod - self.x_cod)
       
    
