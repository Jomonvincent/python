#!/usr/bin/env python
# coding: utf-8

# In[2]:


f1=open("secfile.txt","r")
ff=f1.readlines()
with open("odd.txt","w")as f2:
    for i in range(0,len(ff)):
        if(i%2!=0):
            f2.write(ff[i])


# In[ ]:




