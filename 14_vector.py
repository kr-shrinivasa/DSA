a1, a2, a3 = map(int,input().split())
b1, b2, b3 = map(int,input().split())
dotpr = a1*b1 + a2*b2 + a3*b3
crosspr = int( (a2 * b3 - a3 * b2)*(a2 * b3 - a3 * b2)  + (a1 * b3 - b1 * a3)*(a1 * b3 - b1 * a3)  + (a1 * b2 - a2 * b1)*(a1 * b2 - a2 * b1) )
if dotpr == 0:
    print('2')
elif crosspr == 0:
    print('1')
else:
    print('0')