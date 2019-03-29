#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018


        
AIM     : Ecctraction of User data and Soil data from processed  data File
        : To Analyse the soil Data in AndhraPradesh State and its compatibility, fertility,
          and predict the best fit crop for that soil
          


to      : Input file : datasets/AndhraPradesh/down_to_csv/original_details_ap.csv

        : 2nd INput file:  datasets/AndhraPradesh/new_complete_details_ap.csv
            
        : user details : user_details.csv
        : soil details : soil_parameters.csv

        : 
"""



import csv

field_names_soil_para = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC',
                         'OC','Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 
                         'Avail_Zn','Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']


writeFile = open('filtered_SOIL_types.csv', 'w', newline='')


with open('../saperation/only_soil_types.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    writer = csv.DictWriter(writeFile, field_names_soil_para)
    writer.writeheader()
    
    for row in reader:
        original = row
        soil_type = row['Soil_type']

        black = [ '   Black' ' Black' '-','BLACK' 'Black' 'Black ','Black  '  'black soil' 'black',
                 'black soil' 'Black Soil' 'Black soil' ] 

            
        red = [ ' Red'  'Red' 'RED' ,'Red '  'Red Soils' 'Red soil','Red Soil'  'Redsoil' 'red soil',
         'res soil'  'red' ]
        if soil_type in red:
            soil_type = ''

    
        sand =[ 'SAND'  'Sand' 'Sand +Chowdu' ,
              'Sand +Ondu'  'Sand+Ondu+White'  'Sandi soil',
              'Sandy'  'Sandy ' 'sand' 'Sandy soil' ] 
        if soil_type in sand:
            soil_type = 'sand'


        redsandy = [ 'Red Sandy'  'Red Sandy '  'Red Sandy Loam' ,
              'Red sandy'  'Red sandy loam'  'Sandy Red',
              'red sandy'  'red sandy\\'  'sand',
              'Red  Sandy' ]
        if soil_type in redsandy:
            soil_type = 'redsandy'


        chowdu = [ 'Chowdu +Nalla regadi'  'Black, chowdu' ,
             'Cashewnut'  'Chowdu'  'Chowdu + Black',
             'Chowdu +Black' ,  'Chowdu +Nalla regadi', 
             'Chowdu Sudda'  'Chowdu+ Nalla regadi',
             'Chowdu+ Red'  'Garuku'  'Gurugu ' 'Chowdu + Nalla regadi']
        if soil_type in chowdu:
            soil_type = 'chowdu'


        sandyloam = [ 'Sandy Loam' ,  'Sandy Loam ' ,
            'Sandy loam' 'Sandyloam' 'sandy loam']
        if soil_type in sandyloam:
            soil_type = 'sandyloam'

        nallaregadi = [ 'Nalla regadi' ,  'Red + Nalla regadi' ,
            'Nalla savudu' 'Nalla regadi + chowdu' ]
        if soil_type in nallaregadi:
            soil_type = 'nallaregadi'

        blacksandy = [ 'black sandy' 'black sandy '  'blacksandy',
             'Black Sandy' ]
        if soil_type in blacksandy:
            soil_type = 'blacksandy'
            
        clay =[ 'Claim', 'Clay'  'Clay Sandy','Black Clay' 'Black Clay ' 'clayey loam']
        if soil_type in clay:
            soil_type = 'clay'

        brown = [ 'Brown ' 'Brown Clay'  'Brown Dark',
             'Brown Light' 'Light Broiwn' 'Light Brown',
             'Broan Clay']
        if soil_type in brown:
            soil_type = 'brown'

        mixed = [ 'Mixed soil' 'Black & Mooru'  'Black & Red',
             'Black + Chowdu' 'Black Clay ' 'Tella masaka',
             'Thella kattu' 'Erra maska']
        if soil_type in mixed:
            soil_type = 'mixed'

        rock = [ 'Rox Soil' , 'Rock soil'  ,'Sowdu']
        if soil_type in rock:
            soil_type = 'rock'

        sudha = [ 'Sudda'  'Rock soil' ]
        if soil_type in sudha:
            soil_type = 'sudha'

        saline = ['Saline Soil',  'Saline soil']
        if soil_type in saline:
            soil_type = 'saline'


        sudda = [ '' , 'Sudda Neela'  'Sowdu']
        if soil_type in sudda:
            soil_type = 'sudda'
            
        
        new_row = {'Soil_type':soil_type}
        writer.writerow(new_row)
        print(new_row)