import numpy as np
import random
import json
import matplotlib.pyplot as plt
import datetime as dt
import csv

z=[]

# x = np.arange (-10, 10, 0.05)
# # y = [0 for _ in range(len(x))]
# y = np.sinc(x)
# z = list(zip(x,y))
#
# with open('dataset.json', 'w') as fil:
#     json.dump(z, fil)

def open_csv(path):
    x = []
    y = []
    with open(path) as fil:
        data = csv.reader(fil)
        next(data)
        for i in data:
            t = dt.datetime.fromtimestamp(int(i[0]))
            x += [t]
            y += [i[1]]
    return x, y

x, y = open_csv('etherprice.csv')

a = 100
b = len(x) // 3

x = x[a:b]
y = y[a:b]
# plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Original')


with open('dataset.csv', 'w') as fil:
    writer = csv.writer(fil)
    for row in (zip(x, y)):
        writer.writerow([row[0],row[1]])

# x1 = []
# y1 = []
#
# with open('dataset.csv') as fil:
#     data = csv.reader(fil)
#     for i in data:
#         t = dt.datetime.strptime(i[0],'%Y-%m-%d %H:%M:%S')
#         x1 += [t]
#         y1 += [i[1]]
#
# plt.subplot(2, 1, 2)
# plt.plot(x1, y1)
# plt.title('Loaded')

plt.show()







# hl, = plt.plot([], [])
#
#
# def update_line(hl, new_x, new_y):
#     hl.set_xdata(np.append(hl.get_xdata(), new_x))
#     hl.set_ydata(np.append(hl.get_ydata(), new_y))
#     plt.axis([0,new_x, -2, 2])
#     plt.draw()
#
#
# for x_t, y_t in z:
#     update_line(hl, x_t, y_t)
#     plt.pause(.0001)


