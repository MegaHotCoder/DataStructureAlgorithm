def counting_sort_names(arr):
    output = [0] * len(arr)
    count = [0] * 256 

    for name in arr:
        if name:
            count[ord(name[0])] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for name in reversed(arr):
        if name:
            output[count[ord(name[0])] - 1] = name
            count[ord(name[0])] -= 1

    return output

arr = []

with open('name.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        arr.append(line.strip('\n'))

sorted_names = counting_sort_names(arr)
for i in range(len(sorted_names)):
    print("[%04d] %s" % (i, sorted_names[i]))