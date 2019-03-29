#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018
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
    # take preprocessed.csv as input
    

    ###################################################################
    ####  For User Details
    
    # input file :  preprocessed.csv
    
    filepath = '../preprocessing/preprocessed.csv'
    
    # usecols to open only selected columns
    df_user = pd.read_csv(filepath, usecols = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient',
                                               'Farmer_Name','District', 'Mandal', 'Village',
                                               'Survey_No','Soil_type','Fathers_Name','Crop_type','Time'])

    # save user_details in User_details.csv file
    filepath_to_save_user = '../saperation/user_details.csv'
    df_user.to_csv(filepath_to_save_user, index = False)




    ###################################################################
    ####  For Soil Parametersdatasets/AndhraPradesh/preprocessing/processed_soil_para
    
    #input file: new_complete_details_ap.csv
    
    filepath = '../preprocessing/preprocessed.csv'
    
    # usecols to select only soil para
    df_soil = pd.read_csv(filepath, usecols = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type',
                                               'pH', 'EC','OC', 'Avail_P', 'Exch_K','Avail_Ca',
                                               'Avail_Mg', 'Avail_S','Avail_Zn', 'Avail_B',
                                               'Avail_Fe', 'Avail_Cu', 'Avail_Mn' ])


    # store soil parameters in Soil_parameters.csv file
    filepath_to_save_soil_para = '../saperation/soil_parameters.csv'
    df_soil.to_csv(filepath_to_save_soil_para, index = False)


    


if __name__ == "__main__":
    #calling Main function
    main()
    
    
    
    
    