#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
AIM     : Ecctraction of User data and Soil data from processed  data File
        : To Analyse the soil Data in Karnataka State and its compatibility, fertility,
          and predict the best fit crop for that soil
          
        : Final year Project of Compoter Engineering


to      :
user details : user_details.csv
soil details : soil_parameters.csv

"""



import pandas as pd
import os


field_names = ['card_no', 'farmer_number', 'sau', 'state', 'district', 'taluk',
       'village', 'farmer_name', 'survey_number', 'soil_type', 'authority',
       'ph', 'ec', 'oc', 'av_p', 'av_k', 'av_s', 'av_zn', 'av_b', 'av_fe',
       'av_cu', 'av_mn' ]



class Exctraction(object):
    def __init__(self,df):
        self.df = df

    def removeDuplicate(self,df):
        df.drop_duplicates(inplace=True)
    
    
    
def main():


    ##########################################################################
    # for complete details
    filepath = 'datasets/Karnataka/complete_details.csv'
    df_full = pd.read_csv(filepath)
    
    #print("File << original_details.csv >> not found")
    
    obj_full = Exctraction(df_full)
    obj_full.removeDuplicate(df_full)
    filepath_n = 'datasets/Karnataka/complete.csv'
    df_full.to_csv(filepath_n , index = False)



    ##########################################################################
    ####  For User Details
    filepath_n = 'datasets/Karnataka/complete_details.csv'
    df_user = pd.read_csv(filepath_n, usecols = ['card_no', 'farmer_number', 'sau',
                                               'state','district', 'taluk','village',
                                               'farmer_name','survey_number', 'soil_type','authority'])
    
    #print("File << all_details.csv >> not found")
    filepath_u = 'datasets/Karnataka/user_details.csv'
    df_user.to_csv(filepath_u, index = False)



    ##########################################################################
    ####  For Soil Parametersig
    filepath_n = 'datasets/Karnataka/complete_details.csv'
    df_soil = pd.read_csv(filepath_n, usecols = ['ph', 'ec', 'oc', 'av_p', 'av_k',
                                          'av_s','av_zn', 'av_b', 'av_fe','av_cu', 'av_mn','crop'])


    #print("File < all_details not found >  not found")    
    filepath_s = 'datasets/Karnataka/soil_parameters.csv'
    df_soil.to_csv(filepath_s, index = False)




    ##########################################################################
    ####  For soil types
    filepath_n = 'datasets/Karnataka/complete_details.csv'
    df_soil = pd.read_csv(filepath_n, usecols = ['soil_type'])


    #print("File < all_details not found >  not found")    
    filepath_s = 'datasets/Karnataka/soil_and_crops/only_soil_types.csv'
    df_soil.to_csv(filepath_s, index = False)


    """
    ##########################################################################
    ####  For crop types
    filepath_n = 'datasets/Karnataka/complete.csv'
    df_soil = pd.read_csv(filepath_n, usecols = [])


    #print("File < all_details not found >  not found")    
    filepath_s = 'datasets/Karnataka/soil_and_crops/only_crop_types.csv'
    df_soil.to_csv(filepath_s, index = False)
    """


if __name__ == "__main__":
    #calling Main function
    main()
    
    
    