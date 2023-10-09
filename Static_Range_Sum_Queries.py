n,q = map(int, input().split())
arr = list(map(int,input().split()))
prefix = {0:0}
Sum = 0
for i in range(n):
    Sum += arr[i]
    prefix[i+1] = Sum
#print(prefix)
for i in range(q):
    a,b = map(int, input().split())
    print(prefix[b]-prefix[a-1]) 