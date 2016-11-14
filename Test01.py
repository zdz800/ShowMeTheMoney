# -*- coding: utf-8 -*-
import urllib2
import re
import pandas as pd

#东方财富网资金流入数据获取
def getDongFangData(myurl):
    response = urllib2.urlopen(myurl)
    aa = response.read()
    ret = re.search(r'var \{jsname\}=(.+)', aa)
    pages = 'pages'
    data = 'data'
    date = 'date'
    text = ''
    exec 'text = ' + ret.group(1)
    csvtmp = open('data.csv', 'wb')
    for i in text['data']:
        csvtmp.write(i)
        csvtmp.write('\r\n')
    csvtmp.close()
    dF = pd.read_csv('data.csv', header=None)
    return dF


if __name__ == "__main__":
    tmpurl = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(BalFlowMainNet5)&sr=-1&p=1&ps=50&js=var%20{jsname}={pages:(pc),date:%222014-10-22%22,data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA5"
    tmp = getDongFangData(tmpurl)
    print tmp
