#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


ant1=pd.DataFrame(pd.read_csv('ant1.txt',header=None,delimiter=' '))
ant2=pd.DataFrame(pd.read_csv('ant2.txt',header=None,delimiter=' '))


# In[ ]:


t_0=pd.DataFrame(np.transpose([ant1[:][0],ant2[:][0]]))


# In[ ]:


phase_total=pd.DataFrame(pd.read_csv('phase.txt',header=None,delimiter=' '))


# In[ ]:


phase = phase_total.iloc[:,20:]


# In[ ]:


def baseline(m,n):
    if m>n:
        m,n=n,m
    return np.intersect1d(t_0[t_0.iloc[:,0]==m].index,t_0[t_0.iloc[:,1]==n].index)[0]


# In[ ]:


def closurephase(m,n,time,N):
    total=phase.iloc[baseline(m,n),time]
    for j in range(N):
        if(j!=m and j!=n):
            total+=(phase.iloc[baseline(j,n),time]-phase.iloc[baseline(j,m),time])
    total/=(N-1)
    return total


# In[ ]:


p=np.zeros((30,phase.shape[1]))
n=6
for t in range(phase.shape[1]):
    for i in range(30):
        m=i
        if(m!=n):
            p[i,t]=closurephase(m,n,t,30) 


# In[ ]:


np.savetxt('out_n_6.txt',p)


# In[ ]:


q=np.zeros((30,phase.shape[1]))
n=10
for t in range(phase.shape[1]):
    for i in range(30):
        m=i
        if(m!=n):
            q[i,t]=closurephase(m,n,t,30) 


# In[ ]:


np.savetxt('out_n_10.txt',q)


# In[ ]:


r=np.zeros((30,phase.shape[1]))
n=21
for t in range(phase.shape[1]):
    for i in range(30):
        m=i
        if(m!=n):
            r[i,t]=closurephase(m,n,t,30) 


# In[ ]:


np.savetxt('out_n_21.txt',r)

