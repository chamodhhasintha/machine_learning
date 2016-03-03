#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

void printVec(vector<double>::const_iterator beg, vector<double>::const_iterator end) {
	int i = 0;
	for (vector<double>::const_iterator it = beg; it != end; it++)
		cout << i++ << ":" << *it << endl;
}

int main()
{
	string str = "abc def g";
	string filename = "datas.txt";
	ifstream input(filename);
	string line = "";
	string partten = " ";
	vector<double> years;
	vector<double> prices;
	bool flag = true;
	int lens = 0;
	while (input >> line) {
		if (flag) {
			years.push_back(atof(line.c_str())-2000);
			flag = false;
			lens++;
		} else {
			prices.push_back(atof(line.c_str()));
			flag = true;
		}
	}
/*	printVec(years.begin(), years.end());
	printVec(prices.begin(), prices.end());
*/
	double theta0 = 1.0,theta1 = 1.0;
	double alpha = 0.00005;
	int iterNum = 1000;
	int i = 0;
	while (i++ < iterNum) {
		double gradient0 = 0.0, gradient1 = 0.0;
		for (int k = 0; k < lens; k++) {
			gradient0 += theta0 + theta1*years[k] - prices[k];
			gradient1 += (theta0 + theta1*years[k] - prices[k])*years[k];
		}
		theta0 -= alpha*gradient0/lens;
		theta1 -= alpha*gradient1/lens;
	}
	cout << "theta0 = " << theta0 << endl
		<< "theta1 = " << theta1 << endl;
	int year = 14;
	double est_price = theta0 + theta1*year;
	cout << "At 2014,the house prices is about " << est_price << endl;


	//vector<string> result;
	//int index = 0,start = 0;
	//while (index != str.npos) {
	//	index = str.find_first_of(" ",start);
	//	string tmp = str.substr(start, index-start);
	//	result.push_back(tmp);
	//	cout << tmp << endl;
	//	start = index+1;
	//}
	//for (vector<string>::const_iterator it = result.begin(); it != result.end(); it++)
	//	cout << *it << "\t";
	//cout << endl;
    return 0;
}

