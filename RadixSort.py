def counting_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 256  

    for name in arr:
        index = ord(name[exp]) if exp < len(name) else 0 
        count[index] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        name = arr[i]
        index = ord(name[exp]) if exp < len(name) else 0
        output[count[index] - 1] = name
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_len = max(len(name) for name in arr)  
    for exp in range(max_len - 1, -1, -1): 
        counting_sort(arr, exp)  
    return arr

arr = []

with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

sorted_names_radix = radix_sort(arr)

for i in range(len(sorted_names_radix)):
    print("[%04d] %s" % (i, sorted_names_radix[i]))