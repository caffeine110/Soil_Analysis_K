#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
AIM     : Ecctraction of User data and Soil data from processed  data File
        : To Analyse the soil Data in Karnataka State and its compatibility, fertility,
          and predict the best fit crop for that soil
          


to      :
        : user details : user_details.csv
        : soil details : soil_parameters.csv

"""



import pandas as pd
import os


field_names = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro-nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent-AC', 'Crop_before', 'pH', 'EC',
       'OC', 'Avail-P', 'Exch-K', 'Avail-Ca', 'Avail-Mg', 'Avail-S',
       'Avail-Zn', 'Avail-B', 'Avail-Fe', 'Avail-Cu', 'Avail-Mn', 'Time']



class Exctraction(object):
    def __init__(self,df):
        self.df = df

    def removeDuplicate(self,df):
        df.drop_duplicates(inplace=True)
    
    
    
def main():

    # for complete details
    filepath = 'datasets/AndhraPradesh/complete_details_ap.csv'
    df_full = pd.read_csv(filepath)
    

    obj_full = Exctraction(df_full)
    obj_full.removeDuplicate(df_full)
    filepath_n = 'datasets/AndhraPradesh/complete_details_ap.csv'
    df_full.to_csv(filepath_n , index = False)



    ###################################################################
    ####  For User Details
    filepath_n = 'datasets/AndhraPradesh/complete_details_ap.csv'
    
    df_user = pd.read_csv(filepath_n, usecols = ['Sl_no', 'Date', 'Farmer_No',
                                                 'Macro/Micro-nutrient','Farmer_Name', 
                                                 'District','Mandal','Village','Latitude', 
                                                 'Longitude','Survey_No','Fathers_Name','Time','Crop_before'])


    filepath_to_save_user = 'datasets/AndhraPradesh/user_details.csv'
    df_user.to_csv(filepath_to_save_user, index = False)




    ###################################################################
    ####  For Soil Parametersig

    filepath_n = 'datasets/AndhraPradesh/complete_details_ap.csv'
    df_soil = pd.read_csv(filepath_n, usecols = ['Latitude','Longitude','pH', 'EC', 'pH', 'Avail-P',
                                                 'Exch-K', 'Avail-Ca', 'Avail-Mg', 
                                                 'Avail-Zn', 'Avail-Fe', 'Avail-Cu', 
                                                 'Avail-Mn'])

    df_soil['Crop_Label'] = df_user['Crop_before']
    
        
    filepath_to_save_soil_para = 'datasets/AndhraPradesh/soil_parameters.csv'
    df_soil.to_csv(filepath_to_save_soil_para, index = False)


    #################################################################################
    ############################# only crops

    filepath_crops = 'datasets/AndhraPradesh/complete_details_ap.csv'
    df_crop = pd.read_csv(filepath_crops, usecols = ['Crop_before'])
    
        
    filepath_to_save_only_crops = 'datasets/AndhraPradesh/only_crops.csv'
    df_crop.to_csv(filepath_to_save_only_crops, index = False)
    
    ################################################################################


if __name__ == "__main__":
    #calling Main function
    main()