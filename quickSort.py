def quicksort(a):
    # define a helper funtion to partition the list
    # Pass the array, start index, end index to the partition
    # Set the first element as pivot_elem

    def partition(a,start=0,end=len(a)-1):
        print(f'newrecursion, start = {start} and end={end}')

        if start >= end:
            return a

        pivot_index = start
        pivot_elem = a[pivot_index]

        i = pivot_index+1
        j = end

        print(f'pivot_index = {pivot_index}; pivot_elem = {pivot_elem}; i = {start+1}')
        while i <= j:

            print(f'In the while loop:')
            print(f'i = {i}; j = {j}')

            if a[i] <= pivot_elem:
                i += 1
                print(f'In if: i = {i}')
                print(a)
            elif a[j] >= pivot_elem:
                j -= 1
                print(f'In elif: j = {j}')
                print(a)
            else:
                a[i],a[j] = a[j],a[i]
                print(f'In else: a = {a}')
                print(a)

        a[pivot_index],a[j] = a[j],a[pivot_index]
        print(f'swapped, now a={a}')

        pivot_index = j
        print(f'pivot_index={pivot_index}')

        partition(a,start,pivot_index-1)
        partition(a,pivot_index+1,end)

        return a
    return partition(a)


if __name__ == '__main__':
    arrA = [3,44,38,5,5,47,15,36,26,27,2,46,4,19,50,48]
    print(f'Input array: {arrA}')
    print(quicksort(arrA))
    #sortedA = quicksort(arrA)
    #print(sortedA)