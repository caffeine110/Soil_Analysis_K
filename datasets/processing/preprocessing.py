#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
    
Aim     : To preprocess the data in csv to removes NaN, and rounding of Float variables

"""



import pandas as pd
import numpy as np
import os

field_names = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn' ]



class PreProcessor(object):
    def __init__ (self,df):
        self.df = df

        
    def removeNaN(self,df):
        
        df['card_no'].fillna('Unknown', inplace=True)
        df['farmer_number'].fillna('Unknown', inplace=True)
        df['sau'].fillna('DAU', inplace=True)
        df['state'].fillna('Karnataka', inplace=True)
        df['district'].fillna('Unknown', inplace=True)
        df['taluk'].fillna('Unknown', inplace=True)
        df['village'].fillna('Unknown', inplace=True)
        df['farmer_name'].fillna('Unknown', inplace=True)
        df['survey_number'].fillna('Unknown', inplace=True)
        df['soil_type'].fillna('Unknown', inplace=True)
        df['authority'].fillna('DOA', inplace=True)
        
        
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
                


    def rounding(self,df):
        df.round({'ph':2, 'ec':2, 'oc':2, 'av_p':2, 'av_k':2, 'av_s':2, 'av_zn':2,'av_b':2, 'av_fe':2, 'av_cu':2, 'av_mn':2 })


    def label_Encoding(self,df):
        
        place = "Maize"
        df['crop'].fillna(place, inplace=True)
        
        
        from sklearn import preprocessing
        labelEncoder_croptype = preprocessing.LabelEncoder()
        labelEncoder_croptype.fit(df['crop'])
        labelEncoder_croptype.classes_

        labelEncoder_croptype.transform(df['crop'])
        df['crop'] = labelEncoder_croptype.fit_transform(df['crop'])



    def scaler(self,df):
        pass


    def get_Details(self,df):
        print(df.dtypes)
        print(df.columns)
        print(df.head())
        print(df.info)
        pass


    def new_csv(self,df):
        newFilePath = 'to_csv/complete_details.csv'
        df.to_csv(newFilePath,index= False)
        
        
        
def main():

    filepath = 'to_csv/original_details.csv'
    df = pd.read_csv(filepath)



    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.removeNaN(df)
    api.rounding(df)
    api.label_Encoding(df)
    api.new_csv(df)
    #api.tobinary(df)


if __name__ == "__main__":
    #calling main function
    main()
