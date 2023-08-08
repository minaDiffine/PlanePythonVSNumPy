from statistics import stdev,mean

p=[[2, 1, 1, 2],
 [1, 0, 2, 3],
 [0, 0, 0, 0],
 [3, 0, 2, 2]]
ng = 4

def f1():
        f1=0
        for x in p:
                f1+=sum(s**2 for s in x)
        print("f1",f1)

def f2():
        f2=0
        for n in range(ng):
                f2+=sum(n*n*p[x][abs(n-x)] for x in range(ng))
        print("f2",f2)
def f3():
        f3=0
        px=list(map(sum,p))#sum rows
        py=list(map(sum,zip(*p)))#sum cols
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
f1()
f2()
f3()
