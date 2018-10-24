def bubble_sort(a[]):
    length = len(a)
    for i in range(length):
        swapped=False
        for j in range(length-1):
            if a[j] > a[j+1]:
                swapped = True
                # swap here
            if not swapped:
                break
    return a

