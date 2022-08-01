def sumOfFirstN(n):
    if n==1:
        print(n,n)
        return 1
    a=n+sumOfFirstN(n-1)
    print(n,a)
    return a
    # Implement this function

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)