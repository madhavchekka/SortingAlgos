def insertionSort(a):
    # Assume that the first element in the given list is sorted
    # Compare all the other elements with sorted list from end to start index
    # If the element is less than sorted list element, then move the sorted elements by one index and place element at that index
    # Repeat the above process till the end of the list

    for k in range(1,len(a)):
        elem = a[k]

        for j in range(k-1,-1,-1):
            if elem < a[j]:
                a[j+1] = a[j]
                a[j] = elem
            else:
                break
    return a


if __name__ == '__main__':
    arrA = [3,2,1,1,1,23]
    print(f'Input array: {arrA}')
    sortedA = insertionSort(arrA)
    print(sortedA)