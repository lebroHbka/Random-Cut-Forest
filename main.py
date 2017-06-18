import csv
import datetime as dt
from code.random_cut_forest import RandomCutForest
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


def open_csv():
    x1 = []
    y1 = []
    zip_x_y =[]
    with open('data/temp.csv') as fil:
        data = csv.reader(fil)
        for i in data:
            x1 += [int(i[0])]
            y1 += [float(i[1])]
            zip_x_y += [tuple([int(i[0]), float(i[1])])]
    return x1, y1, zip_x_y


x, y, data = open_csv()
q = time.time()
# --------------------------------------------
# data = [(0,1),
#         (1,2),
#         (2,-2),
#         (3,5),
#         (4,10),
#         (5,-12),
#         (6,7),
#         (7,20),
#         (8,1),
#         (9,2)]
# x = []
# y = []
# for q,w in data:
#     x.append(q)
#     y.append(w)

# --------------------------------------------

r = RandomCutForest(tree_count=100, sensitive=2, shingle=15, sampling_ratio=0.65, elements_count=0)
r.fit(data)
r.start()

print(time.time() - q)
a = []
b = []
for i in r.get_result():
    a += [i[0]]
    b += [i[1]]

x = list(map(lambda time: dt.datetime.fromtimestamp(time), x))
a = list(map(lambda time: dt.datetime.fromtimestamp(time), a))
sl = 10
f = -10
x = x[:-14]
y = y[:-14]
# a = a[sl:f]
# b = b[sl:f]

plt.subplot(2, 1, 1)
plt.plot(x, y)
# plt.ylim(-.5,1.1)
# plt.ylim(225,245)
plt.title('Incoming data')
plt.ylabel('Temperature(x/15)')

plt.subplot(2, 1, 2)
plt.plot(a, b)
# plt.ylim(0,0.03)
plt.title('Anomaly')
plt.xlabel('Abstract time')
plt.ylabel('Anomaly value')
plt.show()

#
#
#
#
#
# ---------------------- debuging ----------------------
# data = [(0,1),
#         (1,2),
#         (2,-2),
#         (3,5),
#         (4,10),
#         (5,-12),
#         (6,7),
#         (7,20),
#         (8,1),
#         (9,2)]

# r = RandomCutForest(data, tree_count=1, sensitive=1, shingle=1)
# r.start()
# r.get_result()

# self.l_border = min(elements, key=lambda x: x[0])[0]

# a =    [(0,1),
#         (2,-2),
#         (4,10),
#         (6,7),
#         (7,-20),
#         (9,2)]
# r = RandomCutForest(data, tree_count=1, sensitive=1, shingle=1)
# r.start()
# print(r.get_result())

