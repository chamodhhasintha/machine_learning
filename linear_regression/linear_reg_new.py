import matplotlib.pyplot as plt
import numpy as np

def read_file(filename):
    handler = open(filename,'r') 
    years = []
    prices = []
    for line in handler:
        year,price = line.strip().split(' ')
        years.append(int(year))
        prices.append(float(price))
    handler.close()
    return years,prices

def calcParm_LMS(years,prices):
    xmean = sum(years)/len(years)
    ymean = sum(prices)/len(prices)
    xdiff = map(lambda x:x-xmean,years)
    ydiff = map(lambda y:y-ymean,prices)
    ixx=sum(map(lambda x:x*x,xdiff))
    ixy=sum(map(lambda x,y:x*y,xdiff,ydiff))
    b1 = ixy/ixx
    b0=ymean-b1*xmean
    return b0,b1

def hypothesis(x,theta):
    mx=np.matrix(x)
    return (mx*theta.T)[0,0]

def gradient(x,y,theta):
    n=len(y)
    res=np.matrix(np.zeros_like(x[0]))
    for i in range(n):
        error=hypothesis(x[i],theta)-y[i]
        mx=np.matrix(x[i],dtype=float)
        res=res+error*mx
    return res/n

def gradient_random(x,y,theta):
    n=len(y)
    i=np.random.randint(n)
    mx=np.matrix(x[i])
    error=hypothesis(mx, theta)-y[i]
    res=error*mx
    return res

def calcParam_GD(years,prices):
    alpha = 0.005
    iterNums = 1000
    x=map(lambda year:(1,year-2000),years)
    y=prices
    theta=np.matrix(np.ones(2,dtype=float))
    while(iterNums!=0):
        grad=gradient(x,y,theta)
        theta=theta-alpha*grad
        iterNums-=1
    theta[0,0]-=2000*theta[0,1]
    return theta    
    
def calcParam_GD_random(years,prices):
    alpha = 0.005
    iterNums = 5000
    x=map(lambda year:(1,year-2000),years)
    y=prices
    theta=np.matrix(np.ones(2,dtype=float))
    while(iterNums!=0):
        grad=gradient_random(x,y,theta)
        theta=theta-alpha*grad
        iterNums-=1
    theta[0,0]-=2000*theta[0,1]
    return theta    


def plot_line(years,prices):
    year2014,year2015=2014,2015
    
    b0,b1=calcParm_LMS(years,prices)
    print b0,b1
    y1,y2=b0+b1*year2014,b0+b1*year2015
    print "Least Mean Square predict result:"
    print "The house price of %d is estimated %f"%(year2014,y1)
    print "The house price of %d is estimated %f"%(year2015,y2)
    x=years
    y=map(lambda x:b0+b1*x,x)
    
    fig=plt.figure(figsize=(10,10))
    ax1=fig.add_subplot(2,2,1)
    ax1.plot(years,prices,'g*')
    ax1.plot(x,y,'bo-')
    ax1.set_xlabel("years")
    ax1.set_ylabel("prices")
    ax1.set_title("Least Mean Square")
    
    theta=calcParam_GD(years,prices)
    b1=theta[0,1]
    b0=theta[0,0]
    print b0,b1
    x1,x2=year2014,year2015
    y1,y2=b0+b1*x1,b0+b1*x2
    print "Gradient Descent predict result:"
    print "The house price of %d is estimated %f"%(year2014,y1)
    print "The house price of %d is estimated %f"%(year2015,y2)
    x=years
    y=map(lambda x:b0+b1*x,x)    
    ax2=fig.add_subplot(2,2,2)
    ax2.plot(x,prices,'g*')
    ax2.plot(x,y,'bo-')
    ax2.set_xlabel("years")
    ax2.set_ylabel("prices")
    ax2.set_title("Gradient descent")  
    

    theta=calcParam_GD_random(years,prices)
    b1=theta[0,1]
    b0=theta[0,0]
    print b0,b1
    x1,x2=year2014,year2015
    y1,y2=b0+b1*x1,b0+b1*x2
    print "Gradient Random Descent predict result:"
    print "The house price of %d is estimated %f"%(year2014,y1)
    print "The house price of %d is estimated %f"%(year2015,y2)
    x=years
    y=map(lambda x:b0+b1*x,x)    
    ax3=fig.add_subplot(2,2,3)
    ax3.plot(x,prices,'g*')
    ax3.plot(x,y,'bo-')
    ax3.set_xlabel("years")
    ax3.set_ylabel("prices")
    ax3.set_title("Gradient random descent") 
    
    ax4=fig.add_subplot(2,2,4)
    ax4.plot(years,prices,'g*')
    ax4.set_xlabel("years")
    ax4.set_ylabel("prices")
    #ax4.set_title("Least Mean Square")
    
    plt.subplots_adjust(wspace=0.3,hspace=0.3)
    plt.show()


if __name__ == "__main__":
    rf = 'linear_regression_data.txt'
    years,prices = read_file(rf)
    plot_line(years,prices)