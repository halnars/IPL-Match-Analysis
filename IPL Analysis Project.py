#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[3]:


from matplotlib import pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


ipl = pd.read_csv("iplmatches.csv")


# In[6]:


ipl.head()


# In[8]:


ipl.shape


# In[9]:


ipl["player_of_match"].value_counts()


# In[10]:


ipl["player_of_match"].value_counts()[0:10]


# In[11]:


ipl["player_of_match"].value_counts()[0:5]


# In[12]:


list(ipl["player_of_match"].value_counts()[0:5].keys())


# In[13]:


plt.figure(figsize=(8,5))
plt.bar(list(ipl["player_of_match"].value_counts()[0:5].keys()),list(ipl["player_of_match"].value_counts()[0:5]),color="g")
plt.show()


# In[14]:


ipl["result"].value_counts()


# In[15]:


ipl["toss_winner"].value_counts()


# In[17]:


batting_first=ipl[ipl["win_by_runs"]!=0]


# In[18]:


batting_first.head()


# In[21]:


plt.figure(figsize=(5,5))
plt.hist(batting_first["win_by_runs"])
plt.title("Distribution of runs")
plt.xlabel("runs")
plt.show()


# In[23]:


batting_first["winner"].value_counts()


# In[33]:


plt.figure(figsize=(12,6))
plt.bar(list(batting_first["winner"].value_counts()[0:5].keys()),list(batting_first["winner"].value_counts()[0:5]),color=["yellow","blue","orange","green","red"])
plt.show()


# In[34]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_first["winner"].value_counts()),labels=list(batting_first["winner"].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[35]:


batting_second=ipl[ipl["win_by_wickets"]!=0]


# In[36]:


batting_second.head()


# In[39]:


plt.figure(figsize=(5,5))
plt.hist(batting_second["win_by_wickets"],bins=30)
plt.show()


# In[40]:


batting_second["winner"].value_counts()


# In[44]:


plt.figure(figsize=(12,5))
plt.bar(list(batting_second["winner"].value_counts()[0:5].keys()),list(batting_second["winner"].value_counts()[0:5]),color=["red","green","purple","yellow","blue"])
plt.show()


# In[45]:


plt.figure(figsize=(7,7))
plt.pie(list(batting_second["winner"].value_counts()),labels=list(batting_second["winner"].value_counts().keys()),autopct="%0.1f%%")
plt.show()


# In[46]:


ipl["season"].value_counts()


# In[47]:


ipl["city"].value_counts()


# In[48]:


import numpy as np


# In[49]:


np.sum(ipl["toss_winner"]==ipl["winner"])


# In[50]:


291/577


# In[ ]:





# In[ ]:




