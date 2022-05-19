
import numpy as np;

class LocShift:
    # If initlen is set >0, we collect this many objects before calculating @K@.
    def __init__(self, initlen=1):
        self.initvec = np.zeros(0)
        self.initlen = initlen
        self.k = 0
        self.n = 0
        self.ex = 0
        self.ex2 = 0
    def append(self,xs):
        # vector append until minimal length for K calculation reached
        if self.initvec.size == 0:
            self.initvec = xs;
        else:
            self.initvec = np.append(self.initvec, xs);
        # minimal length reached, lets do things
        if self.initvec.size > self.initlen:
            self.flush()
    # flush the @initvec@ and compute the moments
    def flush(self):
        # find k, if unknown
        if self.n == 0:
            self.k = np.mean(self.initvec)
        self.n += self.initvec.size
        diff = self.initvec - self.k
        self.ex += np.sum(diff)
        self.ex2 += np.sum(diff * diff)
        self.initvec = np.zeros(0)
    # Return the mean and variance from the object, finalizing if needed.
    def meanVar(self):
        # flush remaining data (on input that was too short)
        self.flush()
        var = (self.ex2 - (self.ex*self.ex) / self.n) / (self.n-1)
        mean = (self.ex / self.n) + self.k
        return (mean,var)

