def solution(A):
    A.sort() #sort array in ascending order
    N = len(A) #get length of array

    #create two pointers
    left = 0
    right = N-1

    smallest = abs(A[0] + A[0]) #initialize the smallest absolute sum

    while left <= right: #loop until pointers cross
        total = A[left] + A[right] #calculate sum of the two numbers

        if abs(total) < smallest: #update the smallest absolute sum
            smallest = abs(total)

        if total < 0: #increase the sum if it is negative
            left += 1

        elif total > 0: #decrease the sum if its positive
            right -= 1

        else: #0 is the smallest possible absolute sum
            return 0

    return smallest #return smallest absolute sum found
