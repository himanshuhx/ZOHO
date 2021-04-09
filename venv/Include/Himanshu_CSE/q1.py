#       6 3  9 10  8 2 1 15 7
# o/p   7 6 10 15 9 3 2  8
curr = 9
a[i] = 6
curr= 7
a[j]=7
a = list(map(int, input().split()))
max_arr = []
n = len(a)
for i in range(n):
    flag = False
    curr = 100000000
    for j in range(n):
        if a[j]>a[i] and a[j]<=curr:
            flag=True
            curr = a[j]
    if not flag:
        max_arr.append(" ")
    else:
        max_arr.append(curr)
print(max_arr)

