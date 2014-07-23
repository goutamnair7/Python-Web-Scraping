import urllib2
import json
import time

presentdate = time.strftime("%d-%m-%Y");
target_url = "http://www.bloomberg.com/markets/chart/data/1D/";

f = open("stocks.txt", "r").read();
stocklist = f.split("\n");
i = 0
l = len(stocklist)

while i < l-1:
    stocklist[i] = eval(stocklist[i])
    i += 1

for stock in stocklist:
    if stock:
        print stock[0][0], ": ",stock[0][1]
        filename = stock[0][1];
        newfile = open(presentdate+"/"+filename+".txt", "w");
        newfile.write(stock[0][0]);
	newfile.write("   Date: "+presentdate);
	newfile.write("\n");

        htmlfile = urllib2.urlopen(target_url+filename+":US");
        data = json.load(htmlfile);
        datapoints = data["data_values"]

        for point in datapoints:
            newfile.write(str(point[1]));
	    newfile.write("\n");
