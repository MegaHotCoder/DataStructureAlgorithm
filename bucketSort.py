def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]
    
    for name in arr:
        if name: 
            index = ord(name[0].lower()) % len(arr)
            bucket[index].append(name)

    for b in bucket:
        insertion_sort(b)

    return [name for sublist in bucket for name in sublist]

arr = []


with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

sorted_names = bucket_sort(arr)
print("[Sorted array is]")
for i in range(len(sorted_names)):
    print("[%04d] %s" % (i, sorted_names[i]))