# Plot some graphs related to ulam

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import sys
import json

x = []
y = []

# return json file as array of ulam numbers
def importUlam(fileName):
	file = open(fileName,)
	seq = json.load(file)
	file.close()
	return seq

# The limit an/a_{n+1} does seem to go to 1
def limit_an():
    data = importUlam('ulam1000_1_2.json')
    index = 0
    for i in range(1, len(data)-1):
        y.append(data[i+1][0]/data[i][0])
    x = np.arange(1, len(y)+1)
    return x,y

# returns an array of the non ulam number for x and
# how many sums can make that number
def plot_rulam_reps():
    data = importUlam('ulamr10000_1_2.json')
    for i in range(1, int(len(data)/6)):
        x.append(data[i][0])
        y.append(data[i][1])
    return x,y

# returns natural numbers and non cos(2.571447*u_n) where u_n is the non ulam numbers
def plot_rulam():
    data = importUlam('ulamr10000_1_2.json')
    for i in range(1, len(data)):
        x.append(i)
        y.append(np.cos(data[i][0] * 2.571447))
    return x,y

# returns natural numbers and cos(2.571447*u_n) where u_n is the ulam numbers
def plot_ulam():
    data = importUlam('ulam10000_1_2.json')
    for i in range(1, len(data)):
        x.append(i)
        y.append(np.cos(2.571447*data[i][0]))
    return x,y

# return natural numbers and array of list non ulum numbers that can be
# made with a certain number of pairs
def plot_rulam_sum_count():
    data = importUlam('ulamr10000_1_2.json')
    x = []
    y = []
    for j in range(0,7):
        xt = []
        yt = []
        count = 0
        for i in range(0, len(data)):
            if data[i][1] == j:
                xt.append(count)
                # yt.append(np.sin(2.571447*data[i][0]))
                yt.append(np.cos(2.571447*data[i][0]))
                count += 1
        x.append(xt)
        y.append(yt)
    return x,y

# 3d plot of ulam numbers with the smaller of the sum as the x axis,
# the larger of the sum as the y axis, and the ulam number as the z axis
def plot_3d_ulam():
    data = importUlam('ulam10000_1_2.json')
    data2 = importUlam('ulam10000_1_3.json')
    data3 = importUlam('ulam10000_1_4.json')
    data4 = importUlam('ulam10000_1_5.json')
    data5 = importUlam('ulam10000_1_6.json')
    xt = []
    yt = []
    zt = []
    x = []
    y = []
    z = []
    for i in range(1, len(data)):
        zt.append(data[i][0])
        xt.append(data[i][1])
        yt.append(data[i][2])
    x.append(xt)
    y.append(yt)
    z.append(zt)
    xt = []
    yt = []
    zt = []
    for i in range(1, len(data)):
        zt.append(data2[i][0])
        xt.append(data2[i][1])
        yt.append(data2[i][2])
    x.append(xt)
    y.append(yt)
    z.append(zt)
    xt = []
    yt = []
    zt = []
    for i in range(1, len(data)):
        zt.append(data3[i][0])
        xt.append(data3[i][1])
        yt.append(data3[i][2])
    x.append(xt)
    y.append(yt)
    z.append(zt)
    xt = []
    yt = []
    zt = []
    for i in range(1, len(data)):
        zt.append(data4[i][0])
        xt.append(data4[i][1])
        yt.append(data4[i][2])
    x.append(xt)
    y.append(yt)
    z.append(zt)
    xt = []
    yt = []
    zt = []
    for i in range(1, len(data)):
        zt.append(data5[i][0])
        xt.append(data5[i][1])
        yt.append(data5[i][2])
    x.append(xt)
    y.append(yt)
    z.append(zt)
    xt = []
    yt = []
    zt = []
    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')
    axes.plot3D(x[0],y[0],z[0],'ro')
    axes.plot3D(x[1],y[1],z[1],'yo')
    axes.plot3D(x[2],y[2],z[2],'go')
    axes.plot3D(x[3],y[3],z[3],'bo')
    axes.plot3D(x[4],y[4],z[4],'co')

if __name__ == "__main__":
    temp = plot_rulam_sum_count()
    ax = plt.subplot(111)
    ax.plot(temp[0][0],temp[1][0], 'o', markersize='1', label='none')
    ax.plot(temp[0][2],temp[1][2], 'o', markersize='1', label='two')
    ax.plot(temp[0][3],temp[1][3], 'o', markersize='1', label='three')
    ax.plot(temp[0][4],temp[1][4], 'o', markersize='1', label='four')
    ax.plot(temp[0][5],temp[1][5], 'o', markersize='1', label='five')
    ax.plot(temp[0][6],temp[1][6], 'o', markersize='1', label='six')
    print(len(temp[1]))
    plt.title("subsequences seperated by number distinct sums")
    plt.xlabel("n")
    plt.ylabel("cos(a_n*2.571447)")
    ax.legend()
    plt.show()
