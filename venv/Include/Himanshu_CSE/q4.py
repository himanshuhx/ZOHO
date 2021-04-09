def check(a,r,n,seq):
    if n==0:
        return
    seq.append(a*(n**r))
    n-=1
    check(a,r,n,seq)

a, r, n, d = map(int,input().split())
seq = []
check(a,r,n,seq)
#print(seq)
res = 0
for x in seq:
    if x%d==0:
        res+=x
    else:
        res-=x
print(res)