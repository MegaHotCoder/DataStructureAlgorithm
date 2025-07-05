def bubbleSort(arr):
        n = len(arr)
            
        for i in range(n):

            for j in range(0, n-i-1):

                if arr[j] > arr[j+1]:
                    arr[j], arr[j + 1] = arr[j+1], arr[j]

arr = []


with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

bubbleSort(arr)

print("[Sorted array is]")
for i in range(len(arr)):
    print("[%04d] %s " %(i, arr[i]), end = "\n")

