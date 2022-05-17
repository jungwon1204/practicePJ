import csv
import pandas as pd
rute = f"E:\\document\\Study\\학교\\고등\\고_3학년_1학기\\인공지능\\1차시 수행평가 re\\통합.csv"

csvData = []
with open(rute, newline="") as file:
    data = csv.reader(file)
    next(data)
    for i in data:
        csvData.append(i)

d = pd.DataFrame(csvData)
a = pd.DataFrame(d[[0,2]])
#print(a.index[0:37])
for i in range(37):
    print(a.index[i])

#print(a)
