
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import sys
import time
from sell_line_values import sell_line_values
from buy_line_values import buy_line_values

rate0index = 1529
btc_quantity0index = 1544
rate_str_length = 6
btc_quantity_str_length = 10
d_line = 47

def get_sell_lines(script, amount_trshd, total_lines):
    
    sell = []
    saved_lines = 1
    curr_line = 1


    while saved_lines<=total_lines:
        line_val = sell_line_values(script,curr_line)
        if line_val[2]>amount_trshd:
            sell.append(line_val)
            saved_lines = saved_lines+1
            curr_line = curr_line+1
        else:
            curr_line = curr_line+1
        
    return sell

def get_buy_lines(script, amount_trshd, total_lines):
    
    buy = []
    saved_lines = 1
    curr_line = 1


    while saved_lines<=total_lines:
        line_val = buy_line_values(script,curr_line)
        if line_val[2]>amount_trshd:
            buy.append(line_val)
            saved_lines = saved_lines+1
            curr_line = curr_line+1
        else:
            curr_line = curr_line+1
        
    return buy


page = requests.get("https://www.bit2c.co.il/exchanges/BtcNis/orderbook.html")
soup = BeautifulSoup(page.content, 'html.parser')
buy_sell_script = soup.find_all('script')[10].prettify()

a = get_sell_lines(buy_sell_script,8000,3)
for 

