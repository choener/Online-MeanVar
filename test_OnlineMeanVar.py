
import numpy as np
import math

import OnlineMeanVar as omv

def test_LocShift():
    # create random data with strong differences in mean and "local" variance, to make life harder
    # for numeric accuracy. We do this by distorting the mean of the first 10 nucleotides.
    l = np.random.randint(10000,1000000)
    d = np.random.exponential(scale = 20)
    xs = np.append( np.random.gumbel(loc=d, scale = 10, size = 10)
                  , np.random.gumbel(loc=0, scale = 10, size=l) )
    ls = omv.LocShift()
    ys = np.array_split(xs, l / 10)
    print("size xs: {}, num splits: {}".format(xs.size, len(ys)))
    for y in ys:
        ls.append(y)
    mean = np.mean(xs)
    var = np.var(xs)
    kmean, kvar = ls.meanVar()
    meankmean = math.log(mean) - math.log(kmean)
    varkvar = math.log(var) - math.log(kvar)
    print("mean: {}, var: {}, k-mean: {}, k-var: {}, loc (first 10): {}, mean/kmean: {}, var/kvar: {}".format(mean, var, kmean, kvar, d, meankmean, varkvar))
    assert (meankmean < 0.01)
    assert (varkvar < 0.1)

