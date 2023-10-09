n,q = map(int, input().split())
arr = list(map(int,input().split()))
prefix = {0:0}
Sum = 0
for i in range(n):
    Sum += arr[i]
    prefix[i+1] = Sum
def change(prefix,b,c):
    ch = c - arr[b-1]
    for i in range(b,n+1):
        prefix[i] += ch

for i in range(q):
    a,b,c = map(int, input().split())
    if a==1:
        change(prefix,b,c) 
    else:
        print(prefix[c]-prefix[b-1])
