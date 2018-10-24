def generate_subarrays(a):
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(i, j+1):
                print a[k],
            print


if __name__ == '__main__':
    generate_subarrays([1,2 ,3, 4])