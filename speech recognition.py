#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[2]:


r = sr.Recognizer()


# In[3]:


with sr.Microphone() as source:
    print("start say.....")
    audio = r.listen(source)
    print("speech is done......")
    


# In[4]:


type(audio)


# In[5]:


audio.frame_data


# In[6]:


data=r.recognize_google(audio)


# In[7]:


data


# In[ ]:




