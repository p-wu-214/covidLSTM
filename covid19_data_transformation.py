#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv");


# In[3]:


data.head()


# In[4]:


china_data = data.loc[data['Country/Region'] == 'Mainland China'];


# In[5]:


china_data


# In[6]:


other_country_data = data.loc[data['Country/Region'] != 'Mainland China'];


# In[7]:


del other_country_data['Province/State']


# In[8]:


other_country_data.head()


# In[9]:


del china_data['Country/Region']


# In[10]:


china_data.head()


# In[11]:


del china_data['Lat'];
del china_data['Long'];


# In[12]:


china_data.head()


# In[13]:


china_data = china_data.melt(id_vars=['Province/State'], var_name='Date', value_name='Confirmed Cases');


# In[14]:


china_data.head(20)


# In[15]:


china_data_transformed = china_data.pivot(index='Date', columns='Province/State', values='Confirmed Cases');


# In[16]:


china_data_transformed


# In[ ]:




