#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Installed once, commented out so that subsequent runs do not install again

get_ipython().system('python -m pip install yfinance')
get_ipython().system('python -m pip install pandas')
get_ipython().system('python -m pip install requests')
get_ipython().system('python -m pip install bs4')
get_ipython().system('python -m pip install plotly')


# In[2]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly


# In[4]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[7]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[8]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[9]:


Tesla = yf.Ticker('TSLA')


# In[10]:


tesla_data = Tesla.history(period = "max")


# In[11]:


tesla_data.reset_index(inplace = True)
tesla_data.head()


# In[12]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[13]:


soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')


# In[14]:


tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)


# In[15]:


tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[16]:


tesla_revenue.tail()


# In[17]:





# In[18]:





# In[ ]:





# In[20]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[21]:


tesla_revenue.dropna(axis=0, how='all', subset=['Revenue']) #drop NaN values
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""] #drop empty string values


# In[22]:


tesla_revenue.tail(5)


# In[23]:


gme = yf.Ticker('GME')


# In[24]:


gme_data = gme.history(period = "max")


# In[25]:


gme_data.reset_index(inplace=True)
gme_data.head(5)


# In[26]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[27]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[28]:


gme_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            gme_revenue = gme_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[29]:


gme_revenue.tail(5)


# In[30]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[31]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




