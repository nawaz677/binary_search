def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right :
        mid = (left + right) // 2
        if target == arr[mid] : 
            return mid 
        elif target < arr[mid] :
            right = mid - 1
        else : 
            left = mid + 1
    return -1

arr = [11,12,13,14,15,16,17,18,19,20,21,22,23]
target = int(input("Enter a target value : "))
print(binary_search(arr, target))