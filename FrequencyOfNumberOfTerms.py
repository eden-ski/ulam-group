from matplotlib import pyplot as plt
import json

file = open('ulamr10000_1_2.json',)
data = json.load(file)
file.close()
freqs = {}
y = []
xx = []
index = 0

# checks how frequently a number of sums shows up
for i in range(0, data[len(data)-1][0]):
    if(data[index][0] == i):
        x = str(data[index][1])
        index += 1
        if(x in freqs):
            freqs[x] = freqs.get(x) + 1
        else:
            freqs[x] = 1
    else:
        if('1' in freqs):
            freqs['1'] = freqs.get('1') + 1
        else:
            freqs['1'] = 1

for i in range(0,data[len(data)-1][0]):
    x = str(i)
    if(x in freqs):
        xx.append(i)
        y.append(freqs[x])

print(freqs)

plt.plot(xx,y)
plt.show()
