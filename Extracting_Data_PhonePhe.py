#!/usr/bin/env python
# coding: utf-8

# # Extracting Data from the PhonePhe Data

# In[ ]:


# aggregated\transaction


# In[1]:


# 01 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\aggregated\transaction\country\india\state
import pandas as pd
import json
import os
#
agg_col={'State':[],'Year':[],'Quarter':[],'Transaction_type':[],'Transaction_count':[],'Transaction_amount':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\aggregated\transaction\country\india\state"

agg_content=os.listdir(path)

for i in agg_content:
    state_i=os.path.join(path,i)
    for j in os.listdir(state_i):
        year_j=os.path.join(state_i,j)
        for k in os.listdir(year_j):
            quat_k=os.path.join(year_j,k)
            with open(quat_k) as f:
                data=json.load(f)
                for L in data['data']['transactionData']:
                   Name=L['name']
                   Count=L['paymentInstruments'][0]['count']
                   Amount=L['paymentInstruments'][0]['amount']
                   agg_col['State'].append(i)
                   agg_col['Year'].append(j)
                   agg_col['Quarter'].append(int(k.strip('.json')))
                   agg_col['Transaction_type'].append(Name)
                   agg_col['Transaction_count'].append(Count)
                   agg_col['Transaction_amount'].append(Amount)
                
                    
agg_dataframe=pd.DataFrame(agg_col)       
#


# In[2]:


agg_dataframe.to_csv('agg_dataframe.csv',index=False)


# In[3]:


agg_dataframe.head()


# In[ ]:


# aggregated\user


# In[4]:


# 02 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\aggregated\user\country\india\state

agg_col={'State':[],'Year':[],'Quarter':[],'Device_Brands':[],'Counts':[],'Percentage':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\aggregated\user\country\india\state"

agg_user=os.listdir(path)

for i in agg_user:
    state_i=os.path.join(path,i)
    for j in os.listdir(state_i):
        year_j=os.path.join(state_i,j)
        for k in os.listdir(year_j):
            quat_k=os.path.join(year_j,k)
            with open(quat_k) as f:
                data=json.load(f)
                try:
                    for L in data['data']['usersByDevice']:
                       Brand=L['brand']
                       Counts=L['count']
                       Percentage=L['percentage']
                       agg_col['State'].append(i)
                       agg_col['Year'].append(j)
                       agg_col['Quarter'].append(int(k.strip('.json')))
                       agg_col['Device_Brands'].append(Brand)
                       agg_col['Counts'].append(Counts)
                       agg_col['Percentage'].append(Percentage)
                except:
                    pass
                
                    
agg_user_dataframe=pd.DataFrame(agg_col)   


# In[5]:


agg_user_dataframe.to_csv('agg_user_dataframe.csv',index=False)


# In[6]:


agg_user_dataframe.head()


# In[ ]:


# map\transaction


# In[7]:


# 03 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\transaction\hover\country\india\state

map_trans={'State':[],'Year':[],'Quarter':[],'District':[],'Counts':[],'Amount':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\transaction\hover\country\india\state"

agg_user=os.listdir(path)

for i in agg_user:
    state_i=os.path.join(path,i)
    for j in os.listdir(state_i):
        year_j=os.path.join(state_i,j)
        for k in os.listdir(year_j):
            quat_k=os.path.join(year_j,k)
            with open(quat_k) as f:
                data=json.load(f)
                try:
                    for L in data['data']['hoverDataList']:
                       Name=L['name']
                       Counts=L['metric'][0]['count'] # it is in list format in json file so calling key as 'metric' and caaling index as [0] as it is single list and caaling the key  to srore the value of it in list
                       Amount=L['metric'][0]['amount']
                       map_trans['State'].append(i)
                       map_trans['Year'].append(j)
                       map_trans['Quarter'].append(int(k.strip('.json')))
                       map_trans['District'].append(Name)
                       map_trans['Counts'].append(Counts)
                       map_trans['Amount'].append(Amount)
                except:
                    pass
                
                    
map_trans_dataframe=pd.DataFrame(map_trans)


# In[8]:


map_trans_dataframe.to_csv('map_trans_dataframe.csv',index=False)


# In[9]:


map_trans_dataframe.head()


# In[ ]:


# map\user


# In[10]:


# 04 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\user\hover\country\india\state.

map_user={'State':[],'Year':[],'Quarter':[],'District':[],'RegisteredUsers':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\user\hover\country\india\state"

agg_user=os.listdir(path)


for i in agg_user:
    state_i = os.path.join(path, i)
    for j in os.listdir(state_i):
        year_j = os.path.join(state_i, j)
        for k in os.listdir(year_j):
            quat_k = os.path.join(year_j, k)
            with open(quat_k) as f:
                data = json.load(f)
                try:
                    for L in data['data']['hoverData'].items(): # items() used to iterate key value in dict format df
                        Name = L[0] # it is in dict format so to get the key  stored used this line
                        Counts = L[1]['registeredUsers']# it is in dict format so to get the  value with particular category stored used this line
                        map_user['State'].append(i)
                        map_user['Year'].append(j)
                        map_user['Quarter'].append(int(k.strip('.json')))
                        map_user['District'].append(Name)
                        map_user['RegisteredUsers'].append(Counts)
                except:
                    pass
                    
map_user_dataframe = pd.DataFrame(map_user)


# In[11]:


map_trans_dataframe.to_csv('map_trans_dataframe.csv',index=False)


# In[12]:


map_trans_dataframe.head()


# In[ ]:


# data\map\user


# In[13]:


# 05 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\user\hover\country\india\state.

map_user={'State':[],'Year':[],'Quarter':[],'District':[],'RegisteredUsers':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\map\user\hover\country\india\state"

agg_user=os.listdir(path)


for i in agg_user:
    state_i = os.path.join(path, i)
    for j in os.listdir(state_i):
        year_j = os.path.join(state_i, j)
        for k in os.listdir(year_j):
            quat_k = os.path.join(year_j, k)
            with open(quat_k) as f:
                data = json.load(f)
                try:
                    for L in data['data']['hoverData'].items(): # items() used to iterate key value in dict format df
                        Name = L[0] # it is in dict format so to get the key  stored used this line
                        Counts = L[1]['registeredUsers']# it is in dict format so to get the  value with particular category stored used this line
                        map_user['State'].append(i)
                        map_user['Year'].append(j)
                        map_user['Quarter'].append(int(k.strip('.json')))
                        map_user['District'].append(Name)
                        map_user['RegisteredUsers'].append(Counts)
                except:
                    pass
                    
map_user_dataframe = pd.DataFrame(map_user)


# In[14]:


map_user_dataframe.to_csv('map_user_dataframe.csv',index=False)


# In[15]:


map_user_dataframe.head()


# In[ ]:


# top\transaction


# In[16]:


# 06 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\top\transaction\country\india\state
top_trans={'State':[],'Year':[],'Quarter':[],'Pincode':[],'Count':[],'Amount':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\top\transaction\country\india\state"

agg_user=os.listdir(path)


for i in agg_user:
    state_i = os.path.join(path, i)
    for j in os.listdir(state_i):
        year_j = os.path.join(state_i, j)
        for k in os.listdir(year_j):
            quat_k = os.path.join(year_j, k)
            with open(quat_k) as f:
                data = json.load(f)
                try:
                    for L in data['data']['pincodes']:
                        Name = L['entityName'] 
                        Counts = L['metric']['count']
                        Amount = L['metric']['amount']
                        top_trans['State'].append(i)
                        top_trans['Year'].append(j)
                        top_trans['Quarter'].append(int(k.strip('.json')))
                        top_trans['Pincode'].append(Name)
                        top_trans['Count'].append(Counts)
                        top_trans['Amount'].append(Counts)
                except:
                    pass
                    
top_trans_dataframe = pd.DataFrame(top_trans)


# In[17]:


top_trans_dataframe.to_csv('top_trans_dataframe.csv',index=False)


# In[18]:


top_trans_dataframe.head()


# In[ ]:


# top\user


# In[19]:


# 07 
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\top\user\country\india\state
top_user={'State':[],'Year':[],'Quarter':[],'Pincode':[],'Registered_user':[]}

path=r"C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\pulse-master\data\top\user\country\india\state"

agg_user=os.listdir(path)


for i in agg_user:
    state_i = os.path.join(path, i)
    for j in os.listdir(state_i):
        year_j = os.path.join(state_i, j)
        for k in os.listdir(year_j):
            quat_k = os.path.join(year_j, k)
            with open(quat_k) as f:
                data = json.load(f)
                try:
                    for L in data['data']['pincodes']:
                        pincode = L['name'] 
                        Counts = L['registeredUsers']
                        top_user['State'].append(i)
                        top_user['Year'].append(j)
                        top_user['Quarter'].append(int(k.strip('.json')))
                        top_user['Pincode'].append(pincode)
                        top_user['Registered_user'].append(Counts)
                      
                except:
                    pass
                    
top_user_dataframe = pd.DataFrame(top_user)


# In[20]:


top_user_dataframe.to_csv('top_user_dataframe.csv',index=False)


# In[21]:


top_user_dataframe.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




