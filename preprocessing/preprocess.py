#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author: gaurav
"""


"""
field_names = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn' ]

"""

import pandas as pd
import numpy as np
import os


class PreProcessor(object):
    def __init__ (self):
        try:
            filepath = 'original_details.csv'
            df = pd.read_csv(filepath, index = False)
            return df
            
        except:
            print("File not found...")



    def rounding(self):
        df.round({'ph':2, 'ec':2, 'oc':2, 'av_p':2, 'av_k':2, 'av_s':2, 'av_zn':2,'av_b':2, 'av_fe':2,'av_cu':2, 'av_mn':2 })

    def removeDuplicate(df):
        df.drop_duplicates(inplace=True)
    
    def removeNaN(self):
        mean = df['ph'].mean()
        df['ph'].fillna(mean, inplace=True)
        
        mean = df['ec'].mean()
        df['ec'].fillna(mean, inplace=True)
        
        mean = df['oc'].mean()
        df['oc'].fillna(mean, inplace=True)
        
        mean = df['av_p'].mean()
        df['av_p'].fillna(mean, inplace=True)
        
        mean = df['av_k'].mean()
        df['av_k'].fillna(mean, inplace=True)
        
        mean = df['av_s'].mean()
        df['av_s'].fillna(mean, inplace=True)
        
        mean = df['av_zn'].mean()
        df['av_zn'].fillna(mean, inplace=True)
        
        mean = df['av_b'].mean()
        df['av_b'].fillna(mean, inplace=True)
        
        mean = df['av_fe'].mean()
        df['av_fe'].fillna(mean, inplace=True)
        
        mean = df['av_cu'].mean()
        df['av_cu'].fillna(mean, inplace=True)
        
        mean = df['av_mn'].mean()
        df['av_mn'].fillna(mean, inplace=True)
        
        
    def labelEncode(self):
        from sklearn import preprocessing
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        labelEncoder_soiltype = LabelEncoder()
        df['soil_type'] = labelEncoder_soiltype.fit_transform(df['soil_type'])


    def scaler(self):
        pass

    def tobinary(self):
        pass

    def new_csv(df):
        newFileName = 'processed.csv'
        pd.to_csv(newFileName,index= False)
    
def main():
    #initialising object
    api = PreProcessor()

    #calling functinos
    api.rounding()
    api.removeDuplicate()
    api.removeNaN()
    api.labelEncode()


if __name__ == "__main__":
    #calling main function
    main()