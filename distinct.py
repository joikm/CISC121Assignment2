def solution(A):
    distinct = set() #create empty set to store distinct values

    for number in A: #loop through each number of given array and add number to the set
        distinct.add(number)

    return len(distinct) #return the length of distinct numbers set
