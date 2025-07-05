from collections import deque

n = int(input())
x = list(map(int, input().split()))
y = [i for i in range(1,n+1)]
x = [{k: v} for k, v in zip(y, x)]
x = deque(x) # move number
ans = []
ind = 1

for _ in range(n):
    current = x.popleft()
    k, v = list(current.items())[0]
    ans.append(k)

    if not x:
        break 

    if v > 0:
        x.rotate(-(v - 1))  
    else:
        x.rotate(-v) 
        
print(' '.join(map(str, ans)))

    
