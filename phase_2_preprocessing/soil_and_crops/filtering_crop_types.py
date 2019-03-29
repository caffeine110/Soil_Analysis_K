#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:37:47 2018

"""




# all parameters form downloaded data
# all paremeters...
field_names_crop_type = ['Crop_type']

import csv

# to save Crops in CROPS.csv file
# write data in writeFIle
writeFile = open('filtered_CROP_types.csv', 'w', newline='')


# open file processed_soil_para.ccsv
with open('../saperation/only_crop_types.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    #create an object writer 
    # DictWriter is dictionary wirteer
    # which write row as dict
    
    writer = csv.DictWriter(writeFile, field_names_crop_type)
    writer.writeheader()
    
    # for loop to iterate in file text (reader)
    for row in reader:
        
        # for convinience and backup
        # if any error occurs print,iginal
        original = row        
        crop_type = row['Crop_type']

        groundnut = [ 'GROUND NUT','Ground Nut','GroundNut','Ground nut','Groundnut','G.Nut',
            'Grounat','groundnut','ground nut','Ground Nat','ground nut/groundnut' ]
       
        if crop_type in groundnut:
            crop_type='groundnut'
        
        
        cotton = [ 'Cottan,Ground Nat','Ground nut,Cottan','Cottan ,Groundnat','Groundnut,Cottan',
              'Cotton/Ground Nut','Cotton/Ground Nut' ,'Cotton/Groundnut' ,'cottan/groundnut',
              'Ground Nat/Cottan' ,'Ground Nut /Cotton' ,'Ground Nut/ Cotton','GroundNut/Cotton',
              'cottan/groundnut' ]
        if crop_type in cotton:
            crop_type = 'cotton'
            
        sunflower = ['SUNFLOWER','Sunflower','sunflower']
        if crop_type in sunflower:
            crop_type = 'sunflower'

            
        blackgram  = [ 'Black Gram','Black gram','Blackgram' ]
        if crop_type in blackgram:
            crop_type = 'blackgram'


        horsegram = [ 'Horsegram','Horse gram','hoesegram' ]
        if crop_type in horsegram:
            crop_type = 'hoesegram'


        sugarcane = [ 'SUGER CANE ','Sugar Cane', 'Cane','Sugarcane','suger cane',
              'Sugarcane ','Sugercane','suger cane ' ]
        if crop_type in sugarcane:
            crop_type = 'sugercane'


        paddy = [ 'paddy','paddy  ', 'PADDY' ]
        if crop_type in paddy:
            crop_type = 'paddy'


        topica = [ 'Topioca','Topioca  ', 'Topica' ]
        if crop_type in topica:
            crop_type = 'topica'


        mulbarry = [ 'Mulbarry','Mulberrry  ', 'Mulberry' ]
        if crop_type in mulbarry:
            crop_type = 'mulbarry'



        maize = [ 'maize','Maize', 'Mazi','Mc' ]
        if crop_type in maize:
            crop_type = 'maize'


        cotton = [ 'Cottan','Cotton', 'cotton','Cotton ' ]
        if crop_type in cotton:
            crop_type = 'cotton'


        greengram = [ 'Green Gram','Green gram' ]
        if crop_type in greengram:
            crop_type = 'greengram'


        paddy = [ 'paddy','paddy  ' ,'Paady','Paddy','Paddy ' ]
        if crop_type in paddy:
            crop_type = 'paddy'


        potato = [ 'Potatao','Potato' ]
        if crop_type in potato:
            crop_type = 'potato'

        redgram = [ 'Red','Red Gram' ]
        if crop_type in redgram:
            crop_type = 'redgram'

        jonna = [ 'Jonna/Senaga','Jonna+ sunflower','Mahendra Jonna','Pacha Jonna',
                 'Pacha Jonna','Peasara + Pacha Gaddi' ]
        if crop_type in jonna:
            crop_type = 'jonna'

        vegetables = [ 'Vegetable','Vegetables','Vegitable' ]
        if crop_type in vegetables:
            crop_type = 'vegetables'

        jowar = [ 'JOWAR','jowar','Jowar' ]
        if crop_type in jowar:
            crop_type = 'jowar'

        paddy = [ 'Paddy/G.nut','Paddy/G.gram','Paddy/Maize/G.N' ]
        if crop_type in paddy:
            crop_type = 'paddy'


        ecalyptus = [ 'Eucaliptus','Eucalyptus' ]
        if crop_type in ecalyptus:
            crop_type = 'ecalyptus'


        yam = [ 'yam','Yam' ]
        if crop_type in yam:
            crop_type = 'yam'

        onion = [ 'Onian','Oniyan' ]
        if crop_type in onion:
            crop_type = 'onion'


        cowpea = [ 'chill','Cowpea' ]
        if crop_type in cowpea:
            crop_type = 'cowpea'


        oilpalm = [ 'Oil Palm ','Oil Palm' ]
        if crop_type in oilpalm:
            crop_type = 'oilpalm'

        turmaric = [ 'Turmaric','Turmeric' ]
        if crop_type in turmaric:
            crop_type = 'turmaric'
                
        seasum = [ 'Sesamum','Sesumum' ]
        if crop_type in seasum:
            crop_type = 'seasum'

        unknown = [ '-','Unknown','Unknown '  ]
        if crop_type in unknown:
            crop_type = 'unknown'


        cashew = [ 'Cashew Nut','Cashew Raina',
                  'Cashew+Maize Cashewnut Cashewnut Cashewnut, Mango (Intercrop Maize And Seasamum)',
                  'Cashewnut, Mango (Intercrop Maize And Seasamum)','Cashewnut','Cashew+Maize' ]
        if crop_type in cashew:
            crop_type = 'cashew'
        
        
        new_row = {'Crop_type':crop_type}
        writer.writerow(new_row)
        print(crop_type)