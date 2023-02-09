#!/usr/bin/env python
# coding: utf-8

# In[202]:


rangelist=list(range(30,65,5))
rangelist[::-1]
rangelist.append(65)
print(rangelist[::-1])


# In[203]:


emptylist=list()
emptylist.extend([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,])
emptylist.remove(0)
print(len(emptylist))
print(max(emptylist))
print(min(emptylist))
sum(emptylist)


# In[204]:


weatherdict= {"sunny": "play", "rainy":"watch tv","cloudy":"walk"}
for i in weatherdict:
    print("when",(i), "let us", (weatherdict[i]))
weatherdict.update({"snowy":"ski"})

