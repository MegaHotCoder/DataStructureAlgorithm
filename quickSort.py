def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  
    left = [x for x in arr[1:] if x <= pivot]   
    right = [x for x in arr[1:] if x > pivot]  

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = []

with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

sorted_names = quick_sort(arr)
for i in range(len(sorted_names)):
    print("[%04d] %s" % (i, sorted_names[i]))
