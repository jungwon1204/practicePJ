data = list(map(float, input().split(" ")))[:-1]

value = 0
for i in data:
    value += i

print(f"과목수:{len(data)}\n평균점수:{(value/len(data)):.2f}")
