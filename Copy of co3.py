#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
print("Current time in sec:",time.time())
print("Current time:",time.ctime())
print("Time After 30 sec:",time.ctime(time.time()+30))
t=time.localtime()
print("Time:",t)

print("Time-current year:",t.tm_year)
print("Time:-current month",t.tm_mon) 
print("Time:-currentday",t.tm_mday)
print("Time:-current hour",t.tm_hour)
print("Time:-current minute",t.tm_min) 
print("Time:-currentsec",t.tm_sec) 
print("Time:-currentweek day",t.tm_wday)
print("Time:-current year day",t.tm_yday)


# In[ ]:





# In[ ]:




