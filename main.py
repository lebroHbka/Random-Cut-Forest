import matplotlib.pyplot as plt
import csv
import datetime as dt
from code.random_cut_forest import RandomCutForest
import numpy as np
import math

def open_csv():
    x1 = []
    y1 = []
    with open('data/dataset.csv') as fil:
        data = csv.reader(fil)
        for i in data:
            t = dt.datetime.strptime(i[0], '%Y-%m-%d %H:%M:%S')
            x1 += [t]
            y1 += [i[1]]
    return x1, y1


x, y = open_csv()
data = list(zip(x, y))

r = RandomCutForest(data)

a = []
b = []
for i in r.get_result:
    a += [i[0]]
    b += [i[1]]


plt.subplot(2, 1, 1)
plt.plot(x, y)
# plt.ylim(-.5,1.1)
# plt.ylim(-300,300)
plt.title('Incoming data')
plt.ylabel('Temperature(x/15)')

plt.subplot(2, 1, 2)
plt.plot(a, b)
# plt.ylim(0,1)
plt.title('Anomaly')
plt.xlabel('Abstract time')
plt.ylabel('Anomaly value')
plt.show()





# x = np.arange (-20.0, 20, 0.1)
# y = np.sinc (x)
# plt.plot(x, y)
# plt.ylim(0, 5)
# plt.xlim(-5, 45)
# plt.show()
# print(len(x))


x3 = [(-9, 10), (-8, 11), (-5, 0), (-4, 21), (-3, 10), (4, 15), (5, 0), (6, 11), (7, .1), (10, 10.7)]


# x3 = [(-9, 10), (-9, 11), (-5, 0), (-4, 21)]


# r = RandomCutForest(x3)
# print(len(r.get_result))
# print(r.get_result)



# tree = x[x.leafs_positions[0]]
# for i in tree:
#     print(i.show_node(), end='***')




