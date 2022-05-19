
import numpy as np;

import OnlineMeanVar as omv

def test_LocShift():
    l = np.random.randint(10000,1000000)
    xs = np.random.random(l)
    ls = omv.LocShift()
    ys = np.array_split(xs, l / 10)
    print("size xs: {}, num splits: {}".format(xs.size, len(ys)))
    for y in ys:
        ls.append(y)
    mean = np.mean(xs)
    var = np.var(xs)
    kmean, kvar = ls.meanVar()
    print("mean: {}, var: {}, k-mean: {}, k-var: {}, diff-mean: {}, diff-var: {}".format(mean, var, kmean, kvar, mean-kmean, var-kvar))
    assert (abs(mean-kmean) < var)
    assert (abs(var-kvar) < 0.001)

