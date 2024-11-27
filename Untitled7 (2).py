#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


india_weather=pd.DataFrame({
    "city":["mumbai","delhi","bnaglore"],
    "temperature":["23","34","35"],
     "humidity":["34","45","56"]
})
india_weather


# In[10]:


us_weather=pd.DataFrame({
    "city":["george","new york","san francisco"],
    "temperature":["23","34","35"],
     "humidity":["34","45","56"]
})
us_weather


# In[11]:


pd.concat([india_weather, us_weather])


# In[12]:


pd.concat([india_weather, us_weather],ignore_index=True)


# In[13]:


pd.concat([india_weather, us_weather],axis=1)


# In[ ]:




