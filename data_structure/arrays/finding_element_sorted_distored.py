def pivoted_binary_search(arr, n, key):
    pivote = findpivote(arr, 0, n-1)
    # array is not rotated it's normal
    if pivote == -1:
        return binary_search(arr, 0, n-1, key)
    if arr[pivote] == key:
        return pivote
    if arr[0] < key:
        return binary_search(arr, 0, pivote-1)
    else:
        return binary_search(arr, pivote + 1, n-1)


def binary_search(arr, low, high, key):
    mid = (low + high) / 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        binary_search(arr, mid +1, high)
    else:
        binary_search(arr, low, mid-1)



def findpivote(arr, low, high):
    if high > low:
        return -1
    if high == low:
        return low
    mid = (low+ high) / 2
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid] < arr[mid-1]
        return mid-1
    if arr[low] >= arr[mid]:
        return findpivote(arr, low, mid-1)
    return findpivote(arr, mid+1, high)


def second_search_solution(arr, low, high, key):
    if low > high:
        return
    mid = (low + high) / 2
    if arr[mid] == key:
        return mid
    # array is sorted
    if arr[low] <= arr[mid]:
        if arr[low] >= key <= arr[mid]:
            return second_search_solution(arr, low, mid-1, key)
        return second_search_solution(arr, mid+ 1, high, key)

    if arr[mid] <= key <= arr[high]:
        return second_search_solution(arr, mid+1, high, key)
    return second_search_solution(arr, low, mid-1, key)



if __name__ =="__main__":
    arr = []
    key = 10
    pivoted_binary_search(arr, n, key)