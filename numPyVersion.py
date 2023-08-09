import numpy as np
from executionTime import timeit

ng=4
p=np.random.randint(ng, size=(ng,ng))
print(p)

@timeit
def f1():
    f1=np.sum(p**2)
    print("f1=",f1)

@timeit
def f2():
    f2=0
    for n in range(ng):
        f2+=(n**2)*(np.trace(p,offset=n)+np.trace(p, offset=-n))
    print("f2=",f2)

@timeit
def f2NoFor():
    nValues=np.arange(ng)
    indices=np.indices(p.shape)
    difference=np.abs(indices[0]-indices[1])

    #mask=difference[:,:,np.newaxis]==nValues
    mask=difference[...,np.newaxis]==nValues

    f2=np.sum(nValues[np.newaxis,np.newaxis,:]**2*p[...,np.newaxis]*mask,axis=(0,1,2))
    #f2=np.einsum('ij,n->',p,nValues**2)
    print("f2NoFor=",f2)


@timeit
def f3():
    f3=0
    px=np.sum(p,axis=1)
    py=np.sum(p,axis=0)
    sigmax=np.std(px)
    sigmay=np.std(py)
    mix=np.mean(px)
    miy=np.mean(py)
    for index, x in np.ndenumerate(p):
        i,j=index
        f3+=i*j*p[i,j]
    f3-=mix*miy
    f3/=sigmax*sigmay
    print("f3=",f3)

@timeit
def f3NoFor():
    px=np.sum(p,axis=1)
    py=np.sum(p,axis=0)
    sigmax=np.std(px)
    sigmay=np.std(py)
    mix=np.mean(px)
    miy=np.mean(py)
    indices=np.indices(p.shape)
    f3=np.sum(indices[0]*indices[1]*p)
    f3-=mix*miy
    f3/=sigmax*sigmay
    print("f3NoFor=",f3)

@timeit
def f5():
    indices=np.indices(p.shape)
    f5=np.sum(1/(1+(indices[0]-indices[1])**2)*p)
    print("f5=",f5)
@timeit
def f9():
    pl=np.ma.log(p)
    pl=pl.filled(0)
    #pl=np.where(p != 0, np.log2(p), 0)
    f9=0-np.sum(pl*p)
    print("f9=",f9)
f1()
f2()
f2NoFor()
f3()
f3NoFor()
f5()
f9()