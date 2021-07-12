def selectionSort(a):
    # set the fist element of the list as the true minimum
    # iterate through the remaining unsorted list and set the minimum value
    # end of the loop, swap the minimum with first unsorted position

    for i in range(0,len(a)-1):

        minElem = a[i]
        j=i+1
        index = None

        while j < len(a):
            if a[j] < minElem:
                minElem = a[j]
                index = j
            j+=1
        if index:
            a[i],a[index] = minElem,a[i]

    return a



if __name__ == '__main__':
    arrA = [1,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
    print(f'Input array: {arrA}')
    # selectionSort(arrA)
    sortedA = selectionSort(arrA)
    print(sortedA)