# You should name your function as difference_sum_even_odd_index
# It should take a list of integers
# Return an integer
def difference_sum_even_odd_index(numbers):
    odd=0
    even=0
    for i in range(len(numbers)):
        if i%2==0:
            even+=numbers[i]
        else:
            odd+=numbers[i]
    return even-odd


# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))