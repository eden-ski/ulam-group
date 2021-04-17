import json
import numpy as np
from matplotlib import pyplot as plt

# function to compute ulam Number
# MAX as max ulam number and starting numbers u,v
# returns an array [[a_1, index1, index2],...,[a_n, index1, index2]]
# a_n is the nth ulam number
# index1 is the first number in the sum to make a_n
def ulam(MAX,u,v):
	arr = []
	s = set()
	arr.append([u,0,0])
	s.add(u)
	arr.append([v,0,0])
	s.add(v)
	for i in range(v+1, MAX):
		count = 0
		index1 = 0
		index2 = 0
		for j in range(0, len(arr)):
			if (i - arr[j][0]) in s and arr[j][0] != (i - arr[j][0]):
				count += 1
				for k in range(0, len(s)):
					if(i - arr[j][0] == arr[k][0] and arr[j][0] != (i-arr[j][0])):
						index1 = k
						index2 = j
			if count > 2:
				break
		if count == 2:
			arr.append([i,index1+1,index2+1])
			s.add(i)
	return arr

def decomp(seq):

	a1 = seq[0][0]
	a2 = seq[1][0]

	seqDecomp = seq
	seqDecomp[0] = [seq[0][0], 1, 0]
	seqDecomp[1] = [seq[1][0], 0, 1]
	seqDecomp[2] = [seq[2][0], 1, 1]

	for i in range(3, len(seq)):
		m = seq[i][1]-1
		k = seq[i][2]-1
		am1 = seqDecomp[m][1]
		am2 = seqDecomp[m][2]
		ak1 = seqDecomp[k][1]
		ak2 = seqDecomp[k][2]
		seqDecomp[i] = [seq[i][0], am1+ak1, am2+ak2]

	return seqDecomp


# import sequence from json file
def importUlam(fileName):
	file = open(fileName,)
	seq = json.load(file)
	file.close()
	return seq

# plot data
data = importUlam('ulam10000_1_2.json')
y1 = []
y2 = []

decomp = decomp(data)

for i in range(0, len(data)):
    y1.append(decomp[i][1])
    y2.append(decomp[i][2])

x = np.arange(len(data))

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
