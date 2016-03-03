import numpy as np
import matplotlib.pyplot as plt
import random

class dataMinning:
    datasets = []
    labelsets = []
    
    npDatasets = np.zeros(1)
    npLabelsets = np.zeros(1)
    
    cost = []
    numIterations = 0
    alpha = 0
    theta = np.ones(2)
    #pCols = 0
    #dRows = 0
    def __init__(self,theta,numIterations,alpha,datasets=None):
        if datasets is None:
            self.datasets = []
        else:
            self.datasets = datasets
        self.theta = theta
        self.numIterations = numIterations
        self.alpha = alpha
        
    def genData(self,numPoints):
        self.genx = np.zeros(shape = (numPoints,2))
        self.geny = np.zeros(shape = numPoints)
        i=0
        for year,price in self.datasets:
            self.genx[i][0] = 1
            self.genx[i][1] = year
            self.geny[i] = price
            i=i+1

    def gradientDescent(self):
        xTrans = self.genx.transpose() #
        i = 0
        while i < self.numIterations:
            hypothesis = np.dot(self.genx,self.theta)
            loss = hypothesis - self.geny
            #record the cost
            self.cost.append(np.sum(loss ** 2))
            #calculate the gradient
            gradient = np.dot(xTrans,loss)
            #updata, gradientDescent
            self.theta = self.theta - self.alpha * gradient
            i = i + 1
            
    
    def show(self):
        print 'yes'

def read_file(filename):
    handler = open(filename,'r')
    years = []
    prices = []
    for line in handler:
        year,price = line.strip().split(' ')
        years.append(int(year)-2000)
        prices.append(float(price))
    handler.close()
    datas = zip(years,prices)
    return datas        


if __name__ == "__main__":
    rf = 'linear_regression_data.txt'
    datas = read_file(rf)    
    c = dataMinning(np.ones(2),100000,0.000005,datas)
    c.genData(len(datas))
    c.gradientDescent()
    print c.theta
    #cx = range(len(c.cost))
    #plt.figure(1)
    #plt.plot(cx,c.cost)
    #plt.ylim(0,25000)
    plt.figure(2)
    plt.plot(c.genx[:,1],c.geny,'b.')
    x = np.arange(1999,2016,1)
    y = x * c.theta[1] + c.theta[0]-2000
    plt.plot(x,y)
    plt.margins(0.2)
    plt.show()