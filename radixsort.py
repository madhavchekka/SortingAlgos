from collections import deque,defaultdict
import numpy as np

def get_digit(num,digit_place):
    # To get the least significant digit, use modulus operator with 10
    # To get the next least significant digit, use the previous quotient and divide it by 10
    while num:
        if digit_place == 1:
            reminder = num % 10
            return reminder
        else:
            num = num//10
        digit_place -= 1
    return 0

# Implement get_digits recursively

def radixsort(a):
    temp = a.copy()
    buckets = defaultdict(deque)

    # To set the value of number of iterations to cover all the digit places
    maxlen = len(str(max(a)))
    #print(maxlen)

    for digit_place in range(1,maxlen+1):

        for elem in temp:
            digit = get_digit(elem,digit_place)
            buckets[digit].append(elem)

        temp = list()

        for i in sorted(buckets.keys()):
            for _ in range(len(buckets[i])):
                temp.append(buckets[i].popleft())

    return temp













if __name__ == '__main__':
    arrA = [3, 440, 38145, 5, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print(arrA)
    sortedarrA = radixsort(arrA)
    print(sortedarrA)
    #print(get_digit(38145,5))