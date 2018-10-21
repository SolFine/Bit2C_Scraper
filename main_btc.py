
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import sys
import time
import os
from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,"#")
sheet1.write(0,1,"time [s]")
sheet1.write(0,2,"Buying price [ILS]")
sheet1.write(0,3,"Selling price [ILS]")
sheet1.write(0,4,"Selling Total [ILS]")
sheet1.write(0,5,"Selling Amount [BTC]")
bias_time = time.time()
line = 1

while(True):
    page = requests.get("https://www.bit2c.co.il/exchanges/BtcNis/orderbook.html")
    if page.status_code==requests.codes.ok: print "\nPage loaded successfully.\n----------\n"
    else: sys.exit("Page loading encountered a problem")

    soup = BeautifulSoup(page.content, 'html.parser')
    buy_sell_script = soup.find_all('script')[10].prettify()

    uni_buy_price = buy_sell_script[1480:1486]
    uni_sell_price = buy_sell_script[1529:1535]
    uni_buy_amount = buy_sell_script[1489:1499]
    uni_sell_amount = buy_sell_script[1544:1554]

    sell_price = int(uni_sell_price[:2])*1000+int(uni_sell_price[3:])
    buy_price = int(uni_buy_price[:2])*1000+int(uni_buy_price[3:])
    buy_amount = float(uni_buy_amount)
    sell_amount = float(uni_sell_amount)
    total_buy = buy_price*buy_amount
    total_sell = sell_price*sell_amount

    print "Sell\n----"
    print "price:", sell_price, "\namount:", sell_amount, "\ntotal:", total_sell
    print "\nBuy\n----"
    print "price:", buy_price, "\namount:", buy_amount, "\ntotal:", total_buy

    row = sheet1.row(line)
    row.write(0,line)
    row.write(1,time.time()-bias_time)
    row.write(2,buy_price)
    row.write(3,sell_price)
    row.write(4,total_sell)
    row.write(5,sell_amount)
    book.save("log.xls")
    line=line+1

