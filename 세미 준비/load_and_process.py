#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import cv2


# In[2]:


dataset_path = 'C:/Users/YGL/Desktop/0. 여러 감정 복합/fer2013/fer2013/fer2013.csv'

image_size = (48, 48)

def load_fer2013():
    data = pd.read_csv(dataset_path)
    pixels = data['pixels'].tolist()
    w, h = 48, 48
    faces = []
    
    for pixel_sequence in pixels:
        face = [int(pixel) for pixel in pixel_sequence.split(' ')]
        face = np.asarray(face).reshape(w, h)
        face = cv2.resize(face.astype('uint8'), image_size)
        faces.append(face.astype('float32'))
        
    faces = np.asarray(faces)
    faces = np.expand_dims(faces, -1)
    emotions = pd.get_dummies(data['emotion']).as_matrix()
    return faces, emorions

def preprocess_input(x, v2 = True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x 

