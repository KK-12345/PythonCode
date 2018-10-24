def pair_sum_sorted_rotated(arr, n, key):
    # find pivote
    for i in range(n):
        if arr[i] > arr[i+1]
            break
    # minimum index
    l = (i+1) #as i is pivote so next one will be small
    r = i
    while l != r:
        if arr[l] + arr[r] == key:
            return True
        if arr[l] + arr[r] < key:
            l = (l + 1) % n
        else:
            r = (n + r -1 ) % n
    return False


if __name__ == '__main__':
    pair_sum_sorted_rotated(arr, n, key)