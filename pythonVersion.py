from statistics import stdev,mean
from executionTime import timeit
import math

p=[[2, 1, 1, 2],
 [1, 0, 2, 3],
 [0, 0, 0, 0],
 [3, 0, 2, 2]]
ng = 4

@timeit
def f1():
        f1=0
        for x in p:
                f1+=sum(s**2 for s in x)
        print("f1=",f1)

@timeit
def f2():
        f2=0
        for n in range(ng):
                for i in range(ng):
                        f2+=sum(n*n*p[i][j] for j in range(ng) if abs(i-j)==n)
        print("f2=",f2)


@timeit
def f3():
        f3=0
        px=list(map(sum,p))#sum rows
        py=list(map(sum,zip(*p)))#sum cols
        zip(*p)
        print(p)
        sigmax=stdev(px)
        sigmay=stdev(py)
        mix=mean(px)
        miy=mean(py)
        for i, x in enumerate(p,start=0):
                for j, y in enumerate(x,start=0):
                        f3+=i*j*y
        f3-=mix*miy
        f3/=sigmax*sigmay
        print("f3=",f3)
@timeit
def f5():
        f5=0
        for i, x in enumerate(p,start=0):
                for j, y in enumerate(x,start=0):
                        f5+=1/(1+(i-j)**2)*y
        print("f5=",f5)

@timeit
def f9():
        f9=0
        for i in p:
                f9+=sum(x*math.log(x) for x in i if x!=0)
        print("f9=",f9)
f1()
f2()
f3()
f5()
f9()