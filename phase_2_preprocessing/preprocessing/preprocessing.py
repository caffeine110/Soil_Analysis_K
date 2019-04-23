#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:36:36 2018

    
Aim     : To preprocess the data in csv to removes NaN, and rounding of Float variables

        : input file  <<  .../to_csv/original_details.csv
        : output file <<  .../to_csv/complete_details.csv

"""



#import os
#import numpy as np

import pandas as pd


field_names = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent_AC', 'Crop_type', 'pH', 'EC',
       'OC', 'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S',
       'Avail_Zn', 'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn', 'Time']

field_names_soil_para = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC',
                         'OC','Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 
                         'Avail_Zn','Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']

new_column_names = ['Latitude', 'Longitude', 'Avail_Cu', 'Avail_Mn' ,'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe','Soil_type', 'Crop_type']



class PreProcessor(object):
    def __init__ (self,df):
        self.df = df


    def remove_Duplicates(self,df):
        df.drop_duplicates(inplace=True)


    def change_Column_Names(self,df):
        #df.columns = field_names
        pass

        
    def delete_Columns(self,df):
        pass

    def remove_NaN(self,df):

        df.dropna(subset = ['Crop_type'])

        ### user details
        df['Sl_no'].fillna('Unknown', inplace=True)
        df['Date'].fillna('Unknown', inplace=True)
        df['Farmer_No'].fillna('Unknown', inplace=True)
        df['Macro/Micro_nutrient'].fillna('Unknown', inplace=True)
        df['Farmer_Name'].fillna('Unknown', inplace=True)
        df['District'].fillna('Unknown', inplace=True)
        df['Mandal'].fillna('Unknown', inplace=True)
        df['Village'].fillna('Unknown', inplace=True)

        

        ### soil parameters
        
        mean = df['Latitude'].mean()
        df['Latitude'].fillna(mean, inplace=True)

        mean = df['Longitude'].mean()
        df['Longitude'].fillna(mean, inplace=True)

        #mean = df['Extent_AC'].mean()
        #df['Extent_AC'].fillna('0.5', inplace=True)

        mean = df['pH'].mean()
        df['pH'].fillna(mean, inplace=True)

        mean = df['EC'].mean()
        df['EC'].fillna(mean, inplace=True)

        mean = df['OC'].mean()
        df['OC'].fillna(mean, inplace=True)

        mean = df['Avail_P'].mean()
        df['Avail_P'].fillna(mean, inplace=True)

        mean = df['Exch_K'].mean()
        df['Exch_K'].fillna(mean, inplace=True)

        mean = df['Avail_Ca'].mean()
        df['Avail_Ca'].fillna(mean, inplace=True)

        mean = df['Avail_Mg'].mean()
        df['Avail_Mg'].fillna(mean, inplace=True)
        
        mean = df['Avail_S'].mean()
        df['Avail_S'].fillna(mean, inplace=True)

        mean = df['Avail_Zn'].mean()
        df['Avail_Zn'].fillna(mean, inplace=True)

        mean = df['Avail_B'].mean()
        df['Avail_B'].fillna(mean, inplace=True)

        mean = df['Avail_Fe'].mean()
        df['Avail_Fe'].fillna(mean, inplace=True)

        mean = df['Avail_Cu'].mean()
        df['Avail_Cu'].fillna(mean, inplace=True)

        mean = df['Avail_Mn'].mean()
        df['Avail_Mn'].fillna(mean, inplace=True)


        df['Soil_type'].fillna('red', inplace=True)


    def rounding(self,df):
        df.round({'ph':2, 'ec':2, 'oc':2, 'av_p':2, 'av_k':2, 'av_s':2, 'av_zn':2,'av_b':2, 'av_fe':2, 'av_cu':2, 'av_mn':2 })


    def label_Encoding(self,df):
        pass
        
        from sklearn import preprocessing
        labelEncoder_croptype = preprocessing.LabelEncoder()
        labelEncoder_croptype.fit(df)
        labelEncoder_croptype.classes_
        
        labelEncoder_croptype.transform(df['crop'])
        df = labelEncoder_croptype.fit_transform(df['crop'])
    

    def scaler(self,df):
        pass


    def get_Details(self,df):
        print(df.count)
        print(df.dtypes)
        print(df.columns)
        print(df.head())
        print(df.info)



    def new_CSV(self,df):
        newFilePath = '../preprocessing/preprocessed.csv'
        df.to_csv(newFilePath,index= False)
        print('file writtern successfully')


# main Function
def main():

    filepath = '../down_to_csv/original_details_ap.csv'
    df = pd.read_csv(filepath, delimiter=';')
    df.columns

    #initialising object
    api = PreProcessor(df)

    #calling functinos
    api.remove_Duplicates(df)
    #api.change_Column_Names(df)
    api.remove_NaN(df)
    #api.rounding(df)
    api.get_Details(df)
    api.new_CSV(df)


if __name__ == "__main__":
    #calling main function
    main()
