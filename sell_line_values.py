
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup

'''
page = requests.get("https://www.bit2c.co.il/exchanges/BtcNis/orderbook.html")
soup = BeautifulSoup(page.content, 'html.parser')
script = soup.find_all('script')[10].prettify()

'''
# Input: the script (as senn above) table and the line number of the sell.
# Output: A list [ rate [NIS/BTC], quantiyty [BTC], total [NIS] ].

def sell_line_values(script, line_num): 

# Indexes for the script section string.
    rate0index = 1529
    btc_quantity0index = 1544
    rate_str_length = 6
    btc_quantity_str_length = 10
    d_line = 47

# Extracting the bitcoin quantity, because the way it's presented there's a different between the first line ans the second.
    if line_num==1:
        int_btc_quantity = float(script[btc_quantity0index:btc_quantity0index+btc_quantity_str_length])
    else:
        int_btc_quantity = float(script[btc_quantity0index+d_line*(line_num-1):btc_quantity0index+btc_quantity_str_length+d_line*(line_num-1)])
        int_last_btc_quantity = float(script[btc_quantity0index+d_line*(line_num-2):btc_quantity0index+btc_quantity_str_length+d_line*(line_num-2)])                  
        int_btc_quantity = int_btc_quantity - int_last_btc_quantity

# Extracting the rate - straight forward.       
    uni_rate = script[rate0index+d_line*(line_num-1) : rate0index+rate_str_length+d_line*(line_num-1)]
    int_rate = int(uni_rate[:2])*1000+int(uni_rate[3:])

#Return as dexcribed above - [ int, float, int ]    
    return [ int_rate, float(format(int_btc_quantity, '.8')), int(round(int_rate*int_btc_quantity)) ]

