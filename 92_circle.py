class Circle:
        def __init__(self,w):
        
            self.width=w
        def getArea(self):
            res1=3.14*self.width*self.width
            res1="{:.1f}".format(res1)
            return res1
        def getCircumference(self):
            res=3.14*2*self.width
            res="{:.1f}".format(res)
            return res



	
if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))