data = []
for i in range(3):
    data.append(int(input()))
data = list(str(data[0]*data[1]*data[2]))
data = list(map(int,data))

base = []
for i in range(10):
    if i == data[i]:
        
