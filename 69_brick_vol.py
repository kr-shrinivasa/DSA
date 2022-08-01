# You should fill this functions using the volume and calculate_price functions defined below this.
# dimensions is a list with 2 values width and height respectively
# brick_count is int representing total bricks
def calculate_total_price_of_bricks(dimensions, brick_count):
    if dimensions[0]>0:
        w=dimensions[0]
    else:
        w=60
    if dimensions[1]>0:
        h=dimensions[1]
    else:
        h=40
    vol=brick_count*volume(width=w,height=h)
    p=calculate_price(vol)
    return round(p)








### Do not change anything below this line
def volume(length=100,width=60,height=40):
	return length*width*height

def calculate_price(volume, price=0.00005):
	return round(volume*price)

if __name__ == "__main__":
    brick_count = int(input())
    dimensions = [int(i) for i in input().split(' ')]
    total_price = calculate_total_price_of_bricks(dimensions, brick_count)
    print(total_price)