n,m,k = input().split()
n,m,k = int(n),int(m),int(k)
appl = list(map(int, input().split()))
apart = list(map(int, input().split()))
done = set()
count = 0
for i in appl:
    for j in range(len(apart)):
        if j not in done:
            if apart[j] in range(i-k,i+k+1):
                count += 1
                done.add(j)
print(count)
