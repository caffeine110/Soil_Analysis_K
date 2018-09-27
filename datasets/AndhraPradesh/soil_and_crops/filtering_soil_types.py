#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:29:34 2018

@author: gaurav
"""


import pandas as pd

filepath = 'only_soil_types.csv'
df = pd.read_csv(filepath)

df.info
