def linearsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
linearsearch([12,98,54,23,45], 23)