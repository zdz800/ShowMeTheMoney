# -*- coding: utf-8 -*-
import urllib2
import json

response1 = urllib2.urlopen("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(BalFlowMainNet5)&sr=-1&p=1&ps=50&js=var%20{jsname}={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA5")
response2 = urllib2.urlopen("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(FFSHARank)&sr=1&p=1&ps=50&js=var {jsname}={pages:(pc),data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C.2&sty=DCFFITAMSHA")
aa = response1.read()
import re
ret = re.search(r'var \{jsname\}=(.+)',aa)
pages = 'pages'
data = 'data'
date = 'date'
text = ''
# print ret.group(1)
exec 'text = ' + ret.group(1)

b = text['data'][0]
for i in text['data']:
    cols = i.split(',')
    print i
    print cols[4]
