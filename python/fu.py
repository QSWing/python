#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randrange
from flask import Flask, render_template, request
import pandas as pd
import csv, os


d2 = pd.read_csv('C:/ST/python/again/data/suiciderate5.csv') #世界近年各国自杀率
d4 = pd.read_csv('C:/ST/python/again/data/sun.csv') #世界各国日照率
d5 = pd.read_csv('C:/ST/python/again/data/compare.csv',encoding="gbk")#全球近年分年龄段自杀率
d6 = pd.read_csv('C:/ST/python/again/data/suicidebysex.csv',encoding="gbk")#全球近年性别自杀率
d7 = pd.read_csv('C:/ST/python/again/data/work.csv',encoding="gbk")#全球近年男女参与劳动率


def jup():
    G="C:/ST/python/again/1.html"
    return G

def jns():
    G="C:/ST/python/again/2.html"
    return G
def co():
    G="C:/ST/python/again/4.html"
    return G

def oc():
    G="C:/ST/python/again/5.html"
    return G
def zh():
    G="C:/ST/python/again/3.html"
    return G


# In[ ]:




