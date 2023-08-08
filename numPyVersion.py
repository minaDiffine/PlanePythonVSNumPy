import numpy as np

ng=4
p=np.random.randint(ng, size=(ng,ng))
print(p)

def f1():
    f1=np.sum(p**2)
    print("f1=",f1)

def f2():
    f2=0
    for n in range(ng):
        f2=(n**2)*(np.trace(p,offset=n)+np.trace(p, offset=-n))
    print("f2=",f2)

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


f1()
f2()
f3()