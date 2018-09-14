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
    def __init__ (self,df):
        self.df = df


    def rounding(self,df):
        df.round({'ph':2, 'ec':2, 'oc':2, 'av_p':2, 'av_k':2, 'av_s':2, 'av_zn':2,'av_b':2, 'av_fe':2,'av_cu':2, 'av_mn':2 })

        
    def removeNaN(self,df):
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
        
        
    def labelEncode(self,df):
        
        place = "Red Soil"
        df['soil_type'].fillna(place, inplace=True)
        
        
        from sklearn import preprocessing
        labelEncoder_soiltype = preprocessing.LabelEncoder()
        labelEncoder_soiltype.fit(df['soil_type'])
        labelEncoder_soiltype.classes_

        labelEncoder_soiltype.transform(df['soil_type'])
        df['soil_type'] = labelEncoder_soiltype.fit_transform(df['soil_type'])


    def scaler(self,df):
        pass

    def tobinary(self,df):
        pass

    def new_csv(self,df):
        newFilePath = 'preprocessing/processed.csv'
        df.to_csv(newFilePath,index= False)
        
        
        
def main():

    filepath = 'exctraction/soil_parameters.csv'
    df = pd.read_csv(filepath)

    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.removeNaN(df)
    api.rounding(df)
    api.labelEncode(df)
    api.new_csv(df)


if __name__ == "__main__":
    #calling main function
    main()