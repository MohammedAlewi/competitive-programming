def insertionSort(arr):
    numArr = [ (value, index) for index, value in enumerate(arr) ]
    
    _, totalCount = mergeSort(numArr, 0, len(arr) - 1)
    # print(shiftArr, result)
    
    return totalCount


def mergeSort(arr, left, right):
    if left == right:
        return [ arr[left] ], 0
    
    mid = (left + right)//2
    
    leftArr, countLeft = mergeSort(arr, left, mid)
    rightArr, countRight = mergeSort(arr, mid + 1, right)
    
    result = []
    totalCount = countLeft + countRight
    leftCounter = rightCounter = 0
    
    while leftCounter < len(leftArr) and rightCounter < len(rightArr):
        if leftArr[ leftCounter ][0] > rightArr[ rightCounter ][0]:
            
            result.append( rightArr[rightCounter] )
            totalCount += len(leftArr) - leftCounter
            
            rightCounter += 1
        else:
            result.append( leftArr[ leftCounter ] )
            leftCounter += 1
            
    while leftCounter < len(leftArr):
        result.append( leftArr[ leftCounter ] )
        leftCounter += 1
        
    while rightCounter < len(rightArr):
        result.append( rightArr[rightCounter] )
        rightCounter += 1
        
    return result, totalCount
