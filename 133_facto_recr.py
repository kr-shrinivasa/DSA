def factorial(n):
    if n<0:
        return "undefined"
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

    # Implement this function

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    print(factorial(n))