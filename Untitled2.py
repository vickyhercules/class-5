#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##loop
##if--conditional statement
##while
##for


# In[1]:


name="kiran"

if name =="kiran":
    print("yes")
else:
    print("no")


# In[3]:


police = "no"
signal ="no"

if police =="yes" or signal =="red":
    print("stop")
elif police == "no" and signal == "red":
    print("go")
else :
    if signal == "green" :
        print("green")
    print("normal")


# In[ ]:


#if else
#if -- conditional
## while
##for


# In[4]:


# while condition eg
a=1
while a<5 : #Will run untill a becomes equal or greater than 5. So this condition should be used when we are sure that the data will bcome false at any point.
    print(a)
    a=a+1


# In[5]:


for i in range(5):
    print(i)


# In[6]:


a={"hello","welcome","today"}
for i in a:#range will be used only with numbers.
    print(i)


# In[7]:


[0,2,4,6,8]


# In[8]:


l=[]
for i in range(10):
    if i % 2 ==0:
        l.append(i)
        #print(l)
    #print(l)
print(l)


# In[10]:


l=[]
for i in range(0,10,2):
    l.append(i)
print(l)


# In[11]:


#input :["dinesh@gmail.com" , "kumar@gmail.com" , "kiran@yahoo.com"]
#output :["dinesh" ,"kumar" ,"kiran"]
#output : ["gmail", "yahoo"]


# In[12]:


# a=["apple" , "apple" , "mango" , "orange" , "lemon" , "apple"]
#output {"apple" :3 , "mango" : 2 , "orange" : 1 , "lemon" : 1}


# In[13]:


# output : ["apple" , "mango"]
#output  ["apple", "mango" , "lemon" , "orange"]


# In[18]:


a=["dinesh@gmail.com" , "kumar@gmail.com" , "kiran@yahoo.com"]
print(a.split["@"])


# In[19]:


a="dineshkumar@gmail.com"
print(a.split("@"))


# In[ ]:




