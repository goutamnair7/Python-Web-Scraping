import urllib2, re

target_url = "http://www.google.com/finance/getprices?q="

names = {'AAPL':'Apple Inc.', 'GOOG':'Google Inc.', 'YHOO':'Yahoo Inc.', 'FOXA':'21st Century Fox', 'ADBE':'Adobe Systems Inc.', 'AMZN':'Amazon.com, Inc.', 'CSCO':'Cisco Systems Inc.', 'FB':'Facebook, Inc.', 'INTC':'Intel Corporation', 'MSFT':'Microsoft Corporation'}

for name in names:
    url = target_url + name + "&f=c,o"
    htmlfile = urllib2.urlopen(url)
    text = htmlfile.read()
    list1 = text.split('\n')[-1]
    if list1 == '':
        list1 = text.split('\n')[-2].split(',')
    else:
        list1 = text.split('\n')[-1].split(',')
    print names[name]+" ("+name+")"
    print "Last Closing Stock: ", float(list1[0]),"\n"
