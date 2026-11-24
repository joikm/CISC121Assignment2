def solution(A):
    A.sort() #sort array in ascending order
    N = len(A) #get length of array

    for i in range(N-2): #loop through groups of 3 numbers

        if A[i] + A[i+1] > A[i+2]: #check condition a + b > c and if true, then return 1
            return 1

    return 0 #return 0 if the condition is not met
