# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:34:53 2018

@author: Horizon
"""
#importing the libararies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importying the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values