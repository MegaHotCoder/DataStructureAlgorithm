def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = []

with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

sorted_names = selection_sort(arr) 

for i in range(len(sorted_names)):
    print("[%04d] %s" % (i, sorted_names[i]))