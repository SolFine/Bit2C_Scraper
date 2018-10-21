
# coding: utf-8

# In[13]:


import requests
from bs4 import BeautifulSoup
import sys
import time
from sell_line_values import sell_line_values
from buy_line_values import buy_line_values

page = requests.get("https://www.bit2c.co.il/exchanges/BtcNis/orderbook.html")
if page.status_code==requests.codes.ok: print "\nPage loaded successfully.\n----------\n"
else: sys.exit("Page loading encountered a problem")
soup = BeautifulSoup(page.content, 'html.parser')
buy_sell_script = soup.find_all('script')[10].prettify()
print sell_line_values(buy_sell_script, 1)

