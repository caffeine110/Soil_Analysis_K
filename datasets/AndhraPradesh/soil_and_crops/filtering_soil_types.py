#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018

@author : gaurav gaurav
        : caffeine110
        
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

writeFile = open('datasets/AndhraPradesh/preprocessing/SOIL.csv', 'w', newline='')



with open('datasets/AndhraPradesh/preprocessing/processed_soil_para.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    writer = csv.DictWriter(writeFile, field_names_soil_para)
    writer.writeheader()
    
    for row in reader:
        other = row
        if ( row['Soil_type']=='   Black' or row['Soil_type']==' Black' or row['Soil_type']=='-' or
            row['Soil_type']=='BLACK' or row['Soil_type']=='Black' or row['Soil_type']=='Black ' or
            row['Soil_type']=='Black  '  or row['Soil_type']=='black soil' or row['Soil_type']=='black' or
            row['Soil_type']=='black soil' or row['Soil_type']=='Black Soil' or row['Soil_type']=='Black soil'):
            row['Soil_type'] = 'black'
            writer.writerow(row)

            
        elif ( row['Soil_type']==' Red'  or row['Soil_type']=='Red' or row['Soil_type']=='RED'  or
              row['Soil_type']=='Red '  or row['Soil_type']=='Red Soils' or row['Soil_type']=='Red soil' or
              row['Soil_type']=='Red Soil'  or row['Soil_type']=='Redsoil' or row['Soil_type']=='red soil' or
              row['Soil_type']=='res soil'  or row['Soil_type']=='red'):
            row['Soil_type'] = 'redsoil'
            writer.writerow(row)

        elif ( row['Soil_type']=='SAND'  or row['Soil_type']=='Sand' or row['Soil_type']=='Sand +Chowdu'  or
              row['Soil_type']=='Sand +Ondu'  or row['Soil_type']=='Sand+Ondu+White'  or row['Soil_type']=='Sandi soil' or
              row['Soil_type']=='Sandy'  or row['Soil_type']=='Sandy ' or row['Soil_type']=='sand' or row['Soil_type']=='Sandy soil'):
            row['Soil_type'] = 'sandy'
            writer.writerow(row)

        elif ( row['Soil_type']=='Red Sandy'  or row['Soil_type']=='Red Sandy '  or row['Soil_type']=='Red Sandy Loam'  or
              row['Soil_type']=='Red sandy'  or row['Soil_type']=='Red sandy loam'  or row['Soil_type']=='Sandy Red' or
              row['Soil_type']=='red sandy'  or row['Soil_type']=='red sandy\\'  or row['Soil_type']=='sand' or
              row['Soil_type']=='Red  Sandy'):
            row['Soil_type'] = 'redsandy'
            writer.writerow(row)


        elif( row['Soil_type']=='Chowdu +Nalla regadi'  or row['Soil_type']=='Black, chowdu'  or
             row['Soil_type']=='Cashewnut'  or row['Soil_type']=='Chowdu'  or row['Soil_type']=='Chowdu + Black' or
             row['Soil_type']=='Chowdu +Black'  or  row['Soil_type']=='Chowdu +Nalla regadi' or 
             row['Soil_type']=='Chowdu Sudda'  or row['Soil_type']=='Chowdu+ Nalla regadi' or
             row['Soil_type']=='Chowdu+ Red'  or row['Soil_type']=='Garuku'  or row['Soil_type']=='Gurugu ' or row['Soil_type']=='Chowdu + Nalla regadi'):
            row['Soil_type'] = 'chowdu'
            writer.writerow(row)


        elif( row['Soil_type']=='Sandy Loam'  or  row['Soil_type']=='Sandy Loam '  or
            row['Soil_type']=='Sandy loam' or row['Soil_type']=='Sandyloam' or row['Soil_type']=='sandy loam'):
            row['Soil_type'] = 'sandyloam'
            writer.writerow(row)

        elif( row['Soil_type']=='Nalla regadi'  or  row['Soil_type']=='Red + Nalla regadi'  or
            row['Soil_type']=='Nalla savudu' or row['Soil_type']=='Nalla regadi + chowdu' ):
            row['Soil_type'] = 'nalla'
            writer.writerow(row)

        elif( row['Soil_type']=='black sandy' or row['Soil_type']=='black sandy '  or row['Soil_type']=='blacksandy' or
             row['Soil_type']=='Black Sandy' ):
            row['Soil_type'] = 'blacksandy'
            writer.writerow(row)
            
        elif( row['Soil_type']=='Claim' or row['Soil_type']=='Clay'  or row['Soil_type']=='Clay Sandy' or
             row['Soil_type']=='Black Clay' or row['Soil_type']=='Black Clay ' or row['Soil_type']=='clayey loam'):
            row['Soil_type'] = 'clay'
            writer.writerow(row)

        elif( row['Soil_type']=='Brown ' or row['Soil_type']=='Brown Clay'  or row['Soil_type']=='Brown Dark' or
             row['Soil_type']=='Brown Light' or row['Soil_type']=='Light Broiwn' or row['Soil_type']=='Light Brown' or
             row['Soil_type']=='Broan Clay'):
            row['Soil_type'] = 'brown'
            writer.writerow(row)

        elif( row['Soil_type']=='Mixed soil' or row['Soil_type']=='Black & Mooru'  or row['Soil_type']=='Black & Red' or
             row['Soil_type']=='Black + Chowdu' or row['Soil_type']=='Black Clay ' or row['Soil_type']=='Tella masaka' or
             row['Soil_type']=='Thella kattu' or row['Soil_type']=='Erra maska'):
            row['Soil_type'] = 'mix'
            writer.writerow(row)

        elif( row['Soil_type']=='Rox Soil'  or row['Soil_type']=='Rock soil'  or row['Soil_type']=='Sowdu'):
            row['Soil_type'] = 'soudu'
            writer.writerow(row)

        elif( row['Soil_type']=='Sudda'  or row['Soil_type']=='Rock soil' ):
            row['Soil_type'] = 'rock'
            writer.writerow(row)

        elif(['Soil_type']=='Saline Soil' or  row['Soil_type']=='Saline soil'):
            row['Soil_type'] = 'saline'
            writer.writerow(row)


        elif( row['Soil_type']==''  or row['Soil_type']=='Sudda Neela'  or row['Soil_type']=='Sowdu'):
            row['Soil_type'] = 'soudu'
            writer.writerow(row)

        else:
            writer.writerow(other)
