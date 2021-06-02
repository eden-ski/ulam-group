# WXML: growth of Ulam sequence
# Spring 2021
# Maxim Klyuchko

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# define the first two elements of the sequence, as well as the
# upper bound. The generation will stop as soon as it reaches
# a term that is greater than maxVal
t0 = 1
t1 = 2
maxVal = 10000

#def genUlamSeq(t0, t1, maxVal):
seqTerms = [] # contains the terms on the sequence
smallTerms = [] # the n-th element contains the smaller term of the sum that generates the n-th element of seqTerms
largeTerms = [] # the n-th element contains the larger term of the sum that generates the n-th element of seqTerms
smallInd = [] # the n-th element contains the index of the n-th element of smallTerms
largeInd = [] # the n-th element contains the index of the n-th element of largeTerms
# every term of the sequence can be represented as a linear combination of t0's and t1's
num1s = [] # the n-th element contains the number of t0's in the n-th element of seqTerms
num2s = [] # the n-th element contains the number of t1's in the n-th element of seqTerms

# initialization
setOfTerms = set() # set allows to check if 2nd num exists in seq, speeds code up
setOfTerms.add(t0)
setOfTerms.add(t1)
seqTerms.append(t0)
seqTerms.append(t1)
smallTerms.append(0)
largeTerms.append(0)
smallTerms.append(0)
largeTerms.append(0)
num1s.append(1)
num1s.append(0)
num2s.append(0)
num2s.append(1)

for target in range(3, maxVal):
    numUniqueSums = 0
    for i in range(0, len(seqTerms)):
        k = seqTerms[i]
        if (target - k > k and (target - k) in setOfTerms):
            if (numUniqueSums ==  1):
                numUniqueSums = 2
                break
            else:
                numUniqueSums = 1
                tSmall = k
                tLarge = target - k
    if (numUniqueSums == 1):
        smallTerms.append(tSmall)
        largeTerms.append(tLarge)
        seqTerms.append(tSmall + tLarge)
        setOfTerms.add(tSmall + tLarge)
        smallInd.append(seqTerms.index(tSmall))
        largeInd.append(seqTerms.index(tLarge))
        num1s.append(num1s[seqTerms.index(tSmall)] + num1s[seqTerms.index(tLarge)])
        num2s.append(num2s[seqTerms.index(tSmall)] + num2s[seqTerms.index(tLarge)])

# Graphs: uncomment a block to plot it

    # (n, n-th term of the Ulam sequence)
#plt.plot(np.arange(1, len(seqTerms)+1), seqTerms)
#plt.xlabel("n")
#plt.ylabel("n-th term of the Ulam sequence")

    # (n-th element of smallTerms, n-th element of largeTerms)
#plt.plot(smallTerms, largeTerms, '--o')
#plt.xlabel("smallTerms")
#plt.ylabel("largeTerms")

    #(n, the ratio between the number of t0's and t1's in the simplest representation of the n-th term of the Ulam seq)
plt.plot(np.arange(1, len(seqTerms)+1), np.divide(num2s,num1s))
plt.xlabel("n")
plt.ylabel("number of 2's / number of 1's in the n-th Ulam number")

    #(n, sine of the n-th term of the Ulam sequence)
#plt.scatter(np.arange(1, len(seqTerms)+1), np.sin(seqTerms), s=2)
#plt.xlabel("n")
#plt.ylabel("sine of the n-th term of the Ulam sequence")

    # Two plots: (n, the smaller term of the sum used to generate the n-th term of the Ulam sequence) and
    # (n, the larger term of the sum used to generate the n-th term of the Ulam sequence)
#plt.plot(np.arange(1, len(smallTerms)+1), smallTerms)
#plt.plot(np.arange(1, len(largeTerms)+1), largeTerms)
#plt.plot(np.arange(1, len(largeTerms)+1), 6 * np.arange(1, len(largeTerms)+1))
#plt.xlabel("n")
#plt.ylabel("term used to generate the n-th term of the Ulam sequence")

    # Two plots: (n, the index of the smaller term of the sum used to generate the n-th term of the Ulam sequence) and
    # (n, the index of the larger term of the sum used to generate the n-th term of the Ulam sequence)
#plt.scatter(np.arange(1, len(smallInd)+1), smallInd, s=2)
#plt.scatter(np.arange(1, len(largeInd)+1), largeInd, s=2)
#plt.xlabel("n")
#plt.ylabel("index of the term used to generate the n-th term of the Ulam sequence")


    # uncomment to save the Ulam sequence as a csv file
#DF = pd.DataFrame(seqTerms)
#DF.to_csv("ulamTerms.csv")


plt.show() # displays the graphs