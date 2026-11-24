def solution(A):
    A.sort() #sort A in ascending order

    product1 = A[-1] * A[-2] * A[-3] #multiply last 3 values in array
    product2 = A[0] * A[1] * A[-1] #multiply first 3 values in array

    if product1 > product2: #compare the 2 products and return the greatest value
        return product1
    else:
        return product2
