#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


img = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)


# In[3]:


kernal = np.ones((4,4), np.uint8)


# In[4]:


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
erosion = cv2.erode(opening, kernal, iterations=5)
dilation = cv2.dilate(erosion, kernal, iterations=1)


# In[5]:


sub = cv2.subtract(img, dilation)


# In[6]:


titles = ['image', 'dilation', 'sub']
images = [img, dilation, sub]


# In[7]:


for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

    plt.show()


# In[8]:


cv2.imwrite('Converted.png', sub)


# In[ ]:





# In[ ]:




