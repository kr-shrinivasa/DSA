# Your class should be named as `Rectangle`. 
# Method to get area should be named as `rectangle_area`.
# Method to get perimeter should be named as `rectangle_perimeter`.
# You should be taking `length` and `width` as inputs when creating the object for your class.
class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        if self.width<=0 or self.length<=0:
            return 0
        return self.width*self.length
    def rectangle_perimeter(self):
        if self.width<=0 or self.length<=0:
            return 0
        return 2*self.length +2*self.width 

if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())