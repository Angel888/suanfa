def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)
if __name__ == '__main__':
    array=[2,5,6,1,7]
    print(quickSort(array))