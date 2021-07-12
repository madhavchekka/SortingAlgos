
    # splits the given array into two sub arrays
    # Call this function only if the array size is >=2

def split(a):
    arrLen = len(a)
    return a[:arrLen//2],a[arrLen//2:]


def merge(a,b):
    temp=list()
    i,j = [0,0]

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            temp.append(a[i]); i += 1
        else:
            temp.append(b[j]); j += 1

    temp = temp + a[i:] + b[j:]
    return temp


def mergeSort(a):
    if len(a) ==1:
        return a
    elif len(a) >=2:
        left,right = split(a)
        result = merge(mergeSort(left),mergeSort(right))
    return result

if __name__ == '__main__':
    arrA = [3,5,2,10,1,-10,1000,1,0,23]
    print(f'Input array: {arrA}')
    mergeSort(arrA)
    sortedA = mergeSort(arrA)
    print(sortedA)