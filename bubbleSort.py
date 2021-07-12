def bubbleSort(a):
    # compare each element with next element
    # swap the elements only if prev element is greater than current element
    # repeat the above steps until the whole list gets sorted

    currLen = len(a)
    while currLen !=0:
        print(f'currLen = {currLen}')
        i=0
        while i < currLen-1:
            j=i+1
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
            i+=1
            print(f'Iteration {i}: {a}')
        currLen-=1

    return a


if __name__ == '__main__':
    arrA=[2,1,5,3,1,2,4,3,2,3]
    print(f'Input array: {arrA}')
    sortedA = bubbleSort(arrA)
    print(sortedA)