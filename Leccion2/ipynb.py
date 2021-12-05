#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np


# In[40]:


url = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"

df = pd.read_csv(url)


# In[46]:


#df["Number"] = df["Number"] - 1
df.rename(columns={"Name": "Full name"},inplace=True)


# In[58]:


bins = np.linspace(min(df["Age"]),max(df["Age"]),3) 
#El ultimo parametro es group_names+1


# In[59]:


bins


# In[60]:


group_names = ["Low","High"]


# In[61]:


df["Age-binded"] = pd.cut(df["Age"],bins, labels = group_names, include_lowest = True)


# In[63]:


df


# In[65]:


pd.get_dummies(df["Position"])


# In[ ]:




