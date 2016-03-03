import matplotlib.pyplot as plt
import numpy as np
import math

def read_files():
    path='/home/huaa/workspace/machine_learning/logistic_regression'
    fx=open('ex4x.dat','r')
    x=[]
    for line in fx:
        val=line.strip().split('   ')
        val[0]=float(val[0])
        val[1]=float(val[1])
        val.insert(0,1)#x0=1
        x.append(val)
    fx.close()
    fy=open('ex4y.dat','r')
    y=[]
    for line in fy:
        y.append(int(float(line.strip())))
    fy.close()
    return x,y

def plot_point(x,y):
    posx=[]
    posy=[]
    negx=[]
    negy=[]
    for i in range(len(y)):
        if y[i]==1:
            posx.append(x[i][1])
            posy.append(x[i][2])
        elif y[i]==0:
            negx.append(x[i][1])
            negy.append(x[i][2])
    fig=plt.figure()
    plt.plot(posx,posy,'+')
    plt.plot(negx,negy,'o')
    
    theta=calc_theta(x, y)
    print theta
    x=range(10,70)
    y=map(lambda x:(-(theta[0,0]+theta[0,1]*x))/theta[0,2],x)
    plt.plot(x,y,'b-')
    
    plt.title("logistic regression")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()
    
def sigmoid(x,theta):
    x=np.matrix(x)
    theta=np.matrix(theta)
    z=(theta*x.T)[0,0]
    z=min(100,-z)
    return 1.0/(1.0+math.exp(z))

def hession(x,theta):
    m=len(x)
    H=np.matrix(np.zeros((len(x[0]),len(x[0]))))
    for i in range(m):
        h=sigmoid(x[i],theta)
        h=h*(1-h)
        mx=np.matrix(x[i])
        H=H+h*np.dot(mx.T,mx)
    return H/m
    
def gradient(x,y,theta):
    m=len(x)
    res=np.matrix(np.zeros_like(x[0]))
    for i in range(m):
        h=sigmoid(x[i], theta)-y[i]
        mx=np.matrix(x[i])
        res=res+h*mx
    return res.T/m

def calc_theta(x,y):
    theta=np.matrix(np.zeros_like(x[0]))
    iter_num=100
    while(iter_num!=0):
        grad=gradient(x,y,theta)
        H=hession(x, theta)
        theta=theta-(H.I*grad).T
        iter_num-=1
    return theta
        
if __name__=="__main__":
    x,y=read_files()
    plot_point(x,y)
    #theta=calc_theta(x, y)
    #print theta