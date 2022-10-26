n = int(input()); m = int(input())
cnt = []
test = 0
for i in range(n, m+1):
    print(i)
    for x in range(2, i):
        if i%x == 0:
            test = 1
            break
    if test == 0:
        cnt.append(i)
    test = 0
a = print(-1) if cnt == [] else print(f"{sum(cnt)}\n{cnt[0]}")