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
#import os

field_names = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent_AC', 'Crop_type', 'pH', 'EC',
       'OC', 'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S',
       'Avail_Zn', 'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn', 'Time']


class Exctraction(object):
    def __init__(self,df):
        self.df = df

    def removeDuplicate(self,df):
        df.drop_duplicates(inplace=True)
    
    
    
def main():

    # for complete details
    filepath = 'datasets/AndhraPradesh/down_to_csv/original_details_ap.csv'
    df_full = pd.read_csv(filepath, delimiter=";")

    df_full.columns    

    obj_full = Exctraction(df_full)
    obj_full.removeDuplicate(df_full)
    filepath_n = 'datasets/AndhraPradesh/new_complete_details_ap.csv'
    df_full.to_csv(filepath_n , index = False)



    ###################################################################
    ####  For User Details
    filepath = 'datasets/AndhraPradesh/new_complete_details_ap.csv'
    
    df_user = pd.read_csv(filepath, usecols = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient',
                                               'Farmer_Name','District', 'Mandal', 'Village',
                                               'Survey_No','Soil_type','Fathers_Name','Crop_type','Time'])


    filepath_to_save_user = 'datasets/AndhraPradesh/saperation/user_details.csv'
    df_user.to_csv(filepath_to_save_user, index = False)




    ###################################################################
    ####  For Soil Parameters
    filepath = 'datasets/AndhraPradesh/new_complete_details_ap.csv'
    df_soil = pd.read_csv(filepath, usecols = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type',
                                               'pH', 'EC','OC', 'Avail_P', 'Exch_K','Avail_Ca',
                                               'Avail_Mg', 'Avail_S','Avail_Zn', 'Avail_B',
                                               'Avail_Fe', 'Avail_Cu', 'Avail_Mn' ])


    filepath_to_save_soil_para = 'datasets/AndhraPradesh/saperation/soil_parameters.csv'
    df_soil.to_csv(filepath_to_save_soil_para, index = False)


    


if __name__ == "__main__":
    #calling Main function
    main()