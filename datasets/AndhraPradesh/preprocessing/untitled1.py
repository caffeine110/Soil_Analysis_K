field_names = ['Sl_no', 'Date', 'Farmer_No', 'Macro/Micro_nutrient', 'Farmer_Name',
       'District', 'Mandal', 'Village', 'Latitude', 'Longitude', 'Survey_No',
       'Soil_type', 'Fathers_Name', 'Extent_AC', 'Crop_type', 'pH', 'EC',
       'OC', 'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S',
       'Avail_Zn', 'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn', 'Time']

field_names_soil_para = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC',
                         'OC','Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 
                         'Avail_Zn','Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']



import csv

writeFile = open('datasets/AndhraPradesh/preprocessing/2.csv', 'w', newline='')

with open('datasets/AndhraPradesh/preprocessing/processed_soil_para.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    writer = csv.DictWriter(writeFile, field_names_soil_para)
    writer.writeheader()
    for row in reader:
        original = row        

        if ( row['Crop_type']=='GROUND NUT' or row['Crop_type']=='Ground Nut' or 
            row['Crop_type']=='GroundNut' or row['Crop_type']=='Ground nut' or
            row['Crop_type']=='Groundnut' or row['Crop_type']=='G.Nut' or
            row['Crop_type']=='Grounat' or row['Crop_type']=='groundnut' or
            row['Crop_type']=='ground nut' or row['Crop_type']=='Ground Nat' or
            row['Crop_type']=='ground nut/groundnut'):
            row['Crop_type'] = 'groundnut'
            
            
        elif ( row['Crop_type']=='Cottan,Ground Nat' or row['Crop_type']=='Ground nut,Cottan' or
              row['Crop_type']=='Cottan ,Groundnat' or row['Crop_type']=='Groundnut,Cottan' or 
              row['Crop_type']=='Cotton/Ground Nut' or row['Crop_type']=='Cotton/Ground Nut'  or
              row['Crop_type']=='Cotton/Groundnut'  or row['Crop_type']=='cottan/groundnut' or
              row['Crop_type']=='Ground Nat/Cottan'  or row['Crop_type']=='Ground Nut /Cotton'  or
              row['Crop_type']=='Ground Nut/ Cotton' or row['Crop_type']=='GroundNut/Cotton' or
              row['Crop_type']=='cottan/groundnut'):
            row['Crop_type'] = 'cottan/groundnut'

        elif ( row['Crop_type']=='SUNFLOWER' or row['Crop_type']=='Sunflower' or row['Crop_type']=='sunflower'):
            row['Crop_type'] = 'sunflower'
        
            
        elif ( row['Crop_type']=='Black Gram' or row['Crop_type']=='Black gram' or row['Crop_type']=='Blackgram'):
            row['Crop_type'] = 'blackgram'

        elif ( row['Crop_type']=='Horsegram' or row['Crop_type']=='Horse gram' or row['Crop_type']=='hoesegram'):
            row['Crop_type'] = 'horsegram'

        elif ( row['Crop_type']=='SUGER CANE ' or row['Crop_type']=='Sugar Cane' or row['Crop_type']== 'Cane' or
              row['Crop_type']=='Sugarcane' or row['Crop_type']=='suger cane' or
              row['Crop_type']=='Sugarcane ' or row['Crop_type']=='Sugercane' or row['Crop_type']=='suger cane '):
              row['Crop_type'] = 'sugarcane'

        elif ( row['Crop_type']=='paddy' or row['Crop_type']=='paddy  ' or row['Crop_type']== 'PADDY'):
            row['Crop_type'] = 'paddy'

        elif ( row['Crop_type']=='Topioca' or row['Crop_type']=='Topioca  ' or row['Crop_type']== 'Topica'):
            row['Crop_type'] = 'Topica'

        elif ( row['Crop_type']=='Mulbarry' or row['Crop_type']=='Mulberrry  ' or row['Crop_type']== 'Mulberry'):
            row['Crop_type'] = 'mulberry'


        elif ( row['Crop_type']=='maize' or row['Crop_type']=='Maize' or row['Crop_type']== 'Mazi' or row['Crop_type']=='Mc'):
            row['Crop_type'] = 'maize'

        elif ( row['Crop_type']=='Cottan' or row['Crop_type']=='Cotton' or row['Crop_type']== 'cotton' or row['Crop_type']=='Cotton '):
            row['Crop_type'] = 'cotton'

        elif ( row['Crop_type']=='Green Gram' or row['Crop_type']=='Green gram'):
            row['Crop_type'] = 'greengram'

        elif ( row['Crop_type']=='paddy' or row['Crop_type']=='paddy  '  or row['Crop_type']=='Paady' or row['Crop_type']=='Paddy' or 
            row['Crop_type']=='Paddy ' ):
            row['Crop_type'] = 'paddy'

        elif ( row['Crop_type']=='Potatao' or row['Crop_type']=='Potato'):
            row['Crop_type'] = 'potato'

        elif ( row['Crop_type']=='Red' or row['Crop_type']=='Red Gram'):
            row['Crop_type'] = 'redgram'

        elif ( row['Crop_type']=='Jonna/Senaga' or row['Crop_type']=='Jonna+ sunflower' or row['Crop_type']=='Mahendra Jonna' or
              row['Crop_type']=='Pacha Jonna' or row['Crop_type']=='Pacha Jonna' or 'Peasara + Pacha Gaddi'):
            row['Crop_type'] = 'jonna'

        elif ( row['Crop_type']=='Vegetable' or row['Crop_type']=='Vegetables' or row['Crop_type']=='Vegitable'):
            row['Crop_type'] = 'vegetable'

        elif ( row['Crop_type']=='JOWAR' or row['Crop_type']=='jowar' or row['Crop_type']=='Jowar'):
            row['Crop_type'] = 'jowar'

        elif ( row['Crop_type']=='Paddy/G.nut' or row['Crop_type']=='Paddy/G.gram' or row['Crop_type']=='Paddy/Maize/G.N'):
            row['Crop_type'] = 'paddy/groundnut'


        elif ( row['Crop_type']=='Eucaliptus' or row['Crop_type']=='Eucalyptus'):
            row['Crop_type'] = 'eucalyptus'


        elif ( row['Crop_type']=='yam' or row['Crop_type']=='Yam'):
            row['Crop_type'] = 'yam'

        elif ( row['Crop_type']=='Onian' or row['Crop_type']=='Oniyan'):
            row['Crop_type'] = 'onion'


        elif ( row['Crop_type']=='chill' or row['Crop_type']=='Cowpea'):
            row['Crop_type'] = 'cowpea'


        elif ( row['Crop_type']=='Oil Palm ' or row['Crop_type']=='Oil Palm'):
            row['Crop_type'] = 'oilpalm'

        elif ( row['Crop_type']=='Turmaric' or row['Crop_type']=='Turmeric'):
            row['Crop_type'] = 'turmaric'

        elif ( row['Crop_type']=='Sesamum' or row['Crop_type']=='Sesumum'):
            row['Crop_type'] = 'sesamum'

        elif ( row['Crop_type']=='-' or row['Crop_type']=='Unknown' or row['Crop_type']=='Unknown ' ):
            row['Crop_type'] = 'unknown'


        elif ( row['Crop_type']=='Cashew Nut' or row['Crop_type']=='Cashew Raina' or
              row['Crop_type']=='Cashew+Maize Cashewnut Cashewnut Cashewnut, Mango (Intercrop Maize And Seasamum)' or
              row['Crop_type']=='Cashewnut, Mango (Intercrop Maize And Seasamum)' or row['Crop_type']=='Cashewnut' or
              row['Crop_type']=='Cashew+Maize'):
            row['Crop_type'] = 'cashew'
            
        else:
            row['Crop_type'] = 'groundnut'
            print("no change")
    
        writer.writerow(row)

    