## Following function takes integer and should return True if it's prime 
## otherwise  should return False.
import math
def is_prime(input_number):
    if input_number<2:
        return False
    if input_number==2:
        return True
    for i in range(2,int(math.sqrt(input_number))+1):
        if input_number%i==0:
            return False
    return True
    

    # You can start below this




### Please don't change anything below this line.
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))