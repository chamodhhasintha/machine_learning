import os.path

def read_file(filename):
    handler = open(filename,'r')
    line = handler.readline().strip().split(',')
    years = []
    for year in line:
        years.append(int(year.strip()))
    line = handler.readline().strip().split(',')
    prices = []
    for price in line:
        prices.append(float(price.strip()))
    datas = zip(years,prices)
    return datas
def write_file(filename,datas):
    handler = open(filename,'w')
    for year,price in datas:
        handler.write("%s %s\n"%(year,price))
    
if __name__ == "__main__":
    path = 'D:\Source\machine_learning'
    rf = 'linear_regression_data.txt'
    wf = 'linear_regression_data_1.txt'
    datas = read_file(os.path.join(path,rf))
    for year,price in datas:
        print "%s %s"%(year,price)
    write_file(os.path.join(path,wf),datas)