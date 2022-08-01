def gcd(dividend, divisor):
    if divisor==0:
        return 0
    if dividend%divisor==0:
        return divisor
    return gcd(divisor,dividend%divisor)
    # Implement this function

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    for index in range(n):
        inputInts = input().split(' ')
        dividend = int(inputInts[0])
        divisor = int(inputInts[1])
        print(gcd(dividend, divisor))