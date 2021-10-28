import numpy as np
import scipy.spatial
import sys
sys.path.append('/Users/tabel/Research/codes/SEdist/')
from SEdist import SE_distribution

def VolumekNN(xin, xout, k=1, periodic=0):
    if isinstance(k, int): k = [k] # 
    dim = xin.shape[1]
    xtree = scipy.spatial.cKDTree(xin, boxsize=periodic)
    dis, disi = xtree.query(xout, k=k, n_jobs=-1)
    vol = np.empty_like(dis) # same shape as distance including all k values
    Cr = [2, np.pi, 4 * np.pi / 3][dim - 1]  # Volume prefactor for 1,2, 3D
    for c, k in enumerate(np.nditer(np.array(k))):
        vol[:,c] = Cr * dis[:,c]**dim
    return vol
    
def CDFkNN(xin, xout, kneighbors=1, periodic=0,compress="none",Ninterpolants=500):
    vol = VolumekNN(xin, xout, k=kneighbors, periodic=periodic)
    cdfs = {k: SE_distribution(vol[:,c],compress=compress,Ninterpolants=Ninterpolants) \
        for c,k in enumerate(kneighbors)}
    return cdfs

def CDFkNNDD(xin, kneighbors=1, periodic=0,compress="none",Ninterpolants=500):
    vol = VolumekNN(xin, xin, k=kneighbors, periodic=periodic)
    cdfs = {(k): SE_distribution(vol[:,c],compress=compress,Ninterpolants=Ninterpolants) \
        for c,k in enumerate(kneighbors)}
    return cdfs

