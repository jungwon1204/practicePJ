import sys

a, b, c = map(int, sys.stdin.readline().split(" "))

c = c - b

cnt = 0
if a == 0:
    cnt = 1
if c > 0:
    cnt = int(a/c)# 딱 맞아떨어지는경우 +1 해줘야함
    cnt += 1
elif c <= 0:
    cnt = -1

print(cnt)
