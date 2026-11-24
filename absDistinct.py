def solution(A):
    distinct = set() #create empty set to store distinct values

    for number in A: # loop through A, find absolute values, add each absolute value to set
        value = abs(number)
        distinct.add(value)

    return len(distinct) #return number of distinct absolute values 
