#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

@author : gaurav gahukar
        : caffeine110
    
Aim     : To preprocess the data in csv to removes NaN, and rounding of Float variables

        : input file  <<  .../to_csv/original_details.csv
        : output file <<  .../to_csv/complete_details.csv

"""



#import os
#import numpy as np

import pandas as pd


field_names = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro-nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent-AC', 'Crop_before', 'pH', 'EC',
       'OC', 'Avail-P', 'Exch-K', 'Avail-Ca', 'Avail-Mg', 'Avail-S',
       'Avail-Zn', 'Avail-B', 'Avail-Fe', 'Avail-Cu', 'Avail-Mn', 'Time']



class PreProcessor(object):
    def __init__ (self,df):
        self.df = df


    def remove_Duplicates(self,df):
        df.drop_duplicates(inplace=True)


    def change_Column_Names(self,df):
        df.columns = field_names
        
        
    def delete_Columns(self,df):
        pass

    def remove_NaN(self,df):

        df['Farmer_Name'].fillna('Unknown', inplace=True)
        df['Survey_No'].fillna('Unknown', inplace=True)
        df['Soil_type'].fillna('Unknown', inplace=True)
        df['Fathers_Name'].fillna('Unknown', inplace=True)
 
        #df['Extent-AC'] = df['Extent-AC'].convert_objects(convert_numeric=True)
        #df['Extent-AC'].fillna(0.00, inplace=True)

        #mean = df['Extent-AC'].mean()
        #df['Extent-AC'].fillna(mean, inplace=True)

        df['Extent-AC'].fillna(0, inplace= True)

        df['Crop_before'].fillna('Unknown', inplace=True)

        mean = df['pH'].mean()
        df['pH'].fillna(mean, inplace=True)
        
        mean = df['EC'].mean()
        df['EC'].fillna(mean, inplace=True)
        
        mean = df['Avail-P'].mean()
        df['Avail-P'].fillna(mean, inplace=True)
        
                


    def rounding(self,df):
        df.round({'ph':2, 'ec':2, 'oc':2, 'av_p':2, 'av_k':2, 'av_s':2, 'av_zn':2,'av_b':2, 'av_fe':2, 'av_cu':2, 'av_mn':2 })


    def label_Encoding(self,df):
        pass
        #place = "Maize"
        #df['crop'].fillna(place, inplace=True)
        
        #from sklearn import preprocessing
        #labelEncoder_croptype = preprocessing.LabelEncoder()
        #labelEncoder_croptype.fit(df['crop'])
        #abelEncoder_croptype.classes_

        #labelEncoder_croptype.transform(df['crop'])
        #df['crop'] = labelEncoder_croptype.fit_transform(df['crop'])


    def scaler(self,df):
        pass


    def get_Details(self,df):
        print(df.count)
        print(df.dtypes)
        print(df.columns)
        print(df.head())
        print(df.info)


    def new_CSV(self,df):
        newFilePath = 'to_csv/AndhraPradesh/complete_details_ap.csv'
        df.to_csv(newFilePath,index= False)
        
        
# main Function        
def main():

    filepath = 'to_csv/AndhraPradesh/original_details_ap.csv'
    df = pd.read_csv(filepath, delimiter=';')
    print(df.count)


    #initialising object    
    api = PreProcessor(df)

    #calling functinos
    api.remove_Duplicates(df)
    api.change_Column_Names(df)
    api.remove_NaN(df)
    api.rounding(df)
    api.get_Details(df)
    api.new_CSV(df)


if __name__ == "__main__":
    #calling main function
    main()
