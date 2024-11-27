#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[9]:


df=pd.read_csv('titanic.csv')
df


# In[10]:


df.info()


# In[12]:


df.describe()


# In[13]:


df.describe(include='object')


# In[14]:


df['Pclass'].unique()


# In[18]:


df['Pclass'].value_counts()


# In[20]:


df.describe(include='all')


# In[22]:


df['PassengerId']


# In[26]:


df[['PassengerId', 'Survived', 'Age']]


# In[28]:


df['Survived'][3]


# In[29]:


df['Name'][2]


# In[30]:


df


# In[31]:


df.tail(2)


# In[32]:


df['Ticket'].head(10)


# NORMAL SCLICING

# In[33]:


df[3:6]


# In[34]:


df[1:8:2]


# ADDING AND DELETION OF COLUMN

# In[45]:


df=pd.read_csv('test.csv')
df


# In[43]:


df=pd.read_csv('test(1).csv')
df
df.to_csv('test.csv',index= False) 
df


# In[53]:


df['Organization series']=2
df


# In[50]:


df['Col_3']=[23,24,34.45,23,34,45]


# In[70]:


df


# In[71]:


del df['Organization']
df


# In[79]:


df['year']=[1993,1998,1997,1999,2004,2006]
df


# In[80]:


df.drop(columns=['year'])


# In[81]:


df.drop(index=[2,4,5])


# In[75]:


import seaborn as sns
print(sns.get_dataset_names())


# In[76]:


df.isnull().sum()


# In[78]:


g=df.groupby('Headquater')
list(g)


# In[ ]:


g.get_group(1)['sex'].value_counts()
g=df.groupby(['sex','survived'])
list (g)

