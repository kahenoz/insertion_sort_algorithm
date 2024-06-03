
def myFunc(A):

    for x in range(1,len(A)):
        key = A[x]
        y = x - 1
    
    while y>=0 and A[y]>key:
            A[y+1] = A[y]
            y -= 1

array = [31,41,59,26,41,58]