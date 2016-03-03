from __future__ import division

import os.path
from matplotlib import pyplot as plt
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
    datas = zip(years,prices)
    return datas

def write_file(filename,datas):
    handler = open(filename,'w')
    for year,price in datas:
        handler.write("%s %s\n"%(year,price))
    handler.close()

def plotLine(datas):
    years = []
    prices = []
    for year,price in datas:
        years.append(float(year))
        prices.append(float(price))
    b1,b0 = calcParam_LMS(years,prices)
    print b0,b1
    x1,x2 = 2000,2013
    y1,y2 = b0+b1*x1,b0+b1*x2
 
    plt.subplot(121)
    plt.plot(years,prices,'b*')
    plt.plot([x1,x2],[y1,y2])
    x1,x2=2014,2015
    y1,y2=b0+b1*x1,b0+b1*x2
    plt.plot([x1,x2],[y1,y2],'r*')
    plt.xlabel('years')
    plt.ylabel('prices')
    plt.title('Least Mean Square')
    print "Least Mean Square algorithm predict result:"
    print "The house price of %d is estimated %f"%(x1,y1)
    print "The house price of %d is estimated %f"%(x2,y2)
   
    
    plt.subplot(122)
    b0,b1 = calcParam_GD(years,prices)
    b0=b0-2000
    print b0,b1
    x1,x2 = 2000,2013
    y1,y2 = b0+b1*x1,b0+b1*x2
    plt.plot(years,prices,'b*')
    plt.plot([x1,x2],[y1,y2])
    x1,x2=2014,2015
    y1,y2=b0+b1*x1,b0+b1*x2
    plt.plot([x1,x2],[y1,y2],'r*')
    plt.xlabel('years')
    plt.xlim(1999,2016)
    plt.ylabel('prices')
    plt.ylim(0,15)
    plt.title('Gradient Descent') 
    print "Gradient Decent Algorithm predict result:"
    print "The house price of %d is estimated %f"%(x1,y1)
    print "The house price of %d is estimated %f"%(x2,y2)

    
    #plt.legend()
    plt.show()

def calcParam_LMS(years,prices):
    xmean = sum(years)/len(years)
    ymean = sum(prices)/len(prices)
    xdiff = map(lambda x:x-xmean,years)
    ydiff = map(lambda y:y-ymean,prices)
    ixx=sum(map(lambda x:x*x,xdiff))
    ixy=sum(map(lambda x,y:x*y,xdiff,ydiff))
    #print "ixx = %f\nixy = %f\n"%(ixx,ixy)
    b1 = ixy/ixx
    b0=ymean-b1*xmean
    return b1,b0

def calcParam_GD(years,prices):
    theta = [1.0,1.0]
    alpha = 0.001
    iterNums = 1000
    lens = len(years)
    x = map(lambda x:x-2000,years)
    y = prices
    hypothesis = [0.0,0.0]
    while(0 < iterNums):
        hypothesis[0]=sum(map(lambda x,y:theta[0]+theta[1]*x-y,x,y))/lens
        hypothesis[1]=sum(map(lambda x,y:(theta[0]+theta[1]*x-y)*x,x,y))/lens
        theta=map(lambda x,y:x-alpha*y,theta,hypothesis)
        iterNums-=1
    return theta

if __name__ == "__main__":
    rf = 'linear_regression_data.txt'
    datas = read_file(rf)
    plotLine(datas)
"""
    years = []
    prices = []
    for year,price in datas:
        years.append(float(year))
        prices.append(float(price))
    theta=[(b0,b1) for b0,b1 in calcParam_GD_1(years,prices)]
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(years,prices,'b*')
    x = np.linspace(2000,2013,100)
    y = map(lambda x:theta[-1][0]+theta[-1][1]*x,x)
    line = plt.plot(x,y)
    
    
    plt.xlabel('years')
    plt.xlim(0,2016)
    plt.ylabel('prices')
    plt.ylim(0,15)
    plt.title('Gradient Descent') 
    
    
    plt.show()
"""