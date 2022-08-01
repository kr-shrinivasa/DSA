def bestScore(A,B,C):
    A.sort()
    B.sort()
    C.sort()
    i,j,k=0,0,0
    mini=float('inf')
    
    while i<len(A) and j<len(B) and k<len(C):
        t=sorted([A[i],B[j],C[k]])
        mini=min(mini,abs(t[2]-t[1])+abs(t[0]-t[1]))

        if A[i]==min(t):
            i+=1
        elif B[j]==min(t):
            j+=1
        else:
            k+=1
    print(mini)   
        
       # complete the function

#DO not edit anything below this line

# Driver code 
A= [int(x) for x in input().split()] 
B= [int(x) for x in input().split()]  
C= [int(x) for x in input().split()]  
bestScore(A,B,C)