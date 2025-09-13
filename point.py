# kenmegne kamdem yvan junior 

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
    
    def rotation(self,teta):
        if teta==90:
            M1=[[0,-1],[1,0]]
            MR=self.multiplication(M1)
            return Point(MR[0],MR[1])
        elif teta==0:
            M1=[[1,0],[0,1]]
            MR=self.multiplication(M1)
            return Point(MR[0],MR[1])
        elif teta==180:
            M1=[[-1,0],[0,-1]]
            MR=self.multiplication(M1)
            return Point(MR[0],MR[1])
        elif teta==270:
            M1=[[0,1],[-1,0]]
            MR=self.multiplication(M1)
            return Point(MR[0],MR[1])
        
    def multiplication(self,M):
        R=[]
        R.append(M[0][0]*self.x+M[0][1]*self.y)
        R.append(M[1][0]*self.x+M[1][1]*self.y)
        return R