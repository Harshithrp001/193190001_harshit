#!/usr/bin/env python
# coding: utf-8

# In[32]:


repeat_keywords = {'Once':1,'Double':2, 'Triple':3,'once':1,'double':2, 'triple':3}


# In[55]:


replace_keywords = {'Dollars':'$', 'dollars':'$', 'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Zero':0,'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,'eight':8, 'nine':9, 'zero':0, 'C M': 'CM', "P M": "PM","D M": "DM","A M": "AM"}


# In[ ]:





# In[56]:


def repeat(s):
    repeats = 0
    s = [ss.strip() for ss in s.split()][::-1]

    for i in range(len(s) - 1):
        if s[i - repeats + 1] in repeat_keywords:
            s[i - repeats] *= repeat_keywords[s[i - repeats + 1]]

            del s[i - repeats + 1]
            repeats += 1

    return ' '.join(s[::-1])


# In[57]:


def replace(s):
        s=s.split()
        ll= s[:]
        for i in range(len(s)):
                if s[i] in replace_keywords:
                        ll[i]=str(replace_keywords[s[i]])

        return repeat( ' '.join(ll)) 


# In[58]:


def conversion_to_num(s):
        return replace(s)


# In[ ]:





# In[ ]:




