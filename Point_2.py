
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def deplacement(self,x,y):
        self.x+=x
        self.y+=y
        return Point(self.x,self.y)
    def add(self,autre):
        self.x+=autre.x
        self.y+=autre.y
        return Point(self.x,self.y)
    
    def rotation(self, angle):
        import math
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x*cos_theta - self.y*sin_theta
        y_new = self.x*sin_theta + self.y*cos_theta
        return Point(int(round(x_new)), int(round(y_new)))
   
m=Point(5,6)
'''b=Point(5,7)
o=Point(1,1)
e=m.add(b)
z=b.deplacement(4,8)
print(z)
print(e)
a=180'''
p=m.rotation(90)
print(p)
liste_tetra_possible= [
                    [Point(0, 0), Point(0, 1), Point(-2, 1), Point(2, 0)],
                    [Point(0, 0), Point(-2, 0), Point(0, 1), Point(2, 1)],
                    [Point(0, 0), Point(-2, 0), Point(-2, 1), Point(2, 0)],
                    [Point(0, 0), Point(2, 0), Point(0, 1), Point(2, 1)],
                    [Point(0, 0), Point(-2, 0), Point(2, 0), Point(4, 0)],
                    [Point(0, 0), Point(-2, 0), Point(2, 0), Point(2, 1)],
                    [Point(0, 0), Point(-2, 0), Point(2, 0), Point(0, 1)]]

