#or row['Crop_before']==
import csv

fieldnames = ['Crop_before']
writeFile = open('CROPS.csv', 'w', newline='')

with open('stemed_crops.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    writer = csv.DictWriter(writeFile, fieldnames)
    writer.writeheader()
    for row in reader:
        other = row
        if ( row['Crop_before']=='GROUND NUT' or row['Crop_before']=='Ground Nut' or 
            row['Crop_before']=='GroundNut' or row['Crop_before']=='Ground nut' or
            row['Crop_before']=='Groundnut' or row['Crop_before']=='G.Nut' or
            row['Crop_before']=='Grounat' or row['Crop_before']=='groundnut' or
            row['Crop_before']=='ground nut' or row['Crop_before']=='Ground Nat' or
            row['Crop_before']=='ground nut/groundnut'):
            row['Crop_before'] = 'groundnut'
            writer.writerow(row)
            
            
        elif ( row['Crop_before']=='Cottan,Ground Nat' or row['Crop_before']=='Ground nut,Cottan' or
              row['Crop_before']=='Cottan ,Groundnat' or row['Crop_before']=='Groundnut,Cottan' or 
              row['Crop_before']=='Cotton/Ground Nut' or row['Crop_before']=='Cotton/Ground Nut'  or
              row['Crop_before']=='Cotton/Groundnut'  or row['Crop_before']=='cottan/groundnut' or
              row['Crop_before']=='Ground Nat/Cottan'  or row['Crop_before']=='Ground Nut /Cotton'  or
              row['Crop_before']=='Ground Nut/ Cotton' or row['Crop_before']=='GroundNut/Cotton' or
              row['Crop_before']=='cottan/groundnut'):
            row['Crop_before'] = 'cottan/groundnut'
            writer.writerow(row)

        elif ( row['Crop_before']=='SUNFLOWER' or row['Crop_before']=='Sunflower' or row['Crop_before']=='sunflower'):
            row['Crop_before'] = 'sunflower'
            writer.writerow(row)
        
            
        elif ( row['Crop_before']=='Black Gram' or row['Crop_before']=='Black gram' or row['Crop_before']=='Blackgram'):
            row['Crop_before'] = 'blackgram'
            writer.writerow(row)

        elif ( row['Crop_before']=='Horsegram' or row['Crop_before']=='Horse gram' or row['Crop_before']=='hoesegram'):
            row['Crop_before'] = 'horsegram'
            writer.writerow(row)

        elif ( row['Crop_before']=='SUGER CANE ' or row['Crop_before']=='Sugar Cane' or row['Crop_before']== 'Cane' or
              row['Crop_before']=='Sugarcane' or row['Crop_before']=='suger cane' or
              row['Crop_before']=='Sugarcane ' or row['Crop_before']=='Sugercane' or row['Crop_before']=='suger cane '):
              row['Crop_before'] = 'sugarcane'
              writer.writerow(row)

        elif ( row['Crop_before']=='paddy' or row['Crop_before']=='paddy  ' or row['Crop_before']== 'PADDY'):
            row['Crop_before'] = 'paddy'
            writer.writerow(row)

        elif ( row['Crop_before']=='Topioca' or row['Crop_before']=='Topioca  ' or row['Crop_before']== 'Topica'):
            row['Crop_before'] = 'Topica'
            writer.writerow(row)

        elif ( row['Crop_before']=='Mulbarry' or row['Crop_before']=='Mulberrry  ' or row['Crop_before']== 'Mulberry'):
            row['Crop_before'] = 'mulberry'
            writer.writerow(row)


        elif ( row['Crop_before']=='maize' or row['Crop_before']=='Maize' or row['Crop_before']== 'Mazi' or row['Crop_before']=='Mc'):
            row['Crop_before'] = 'maize'
            writer.writerow(row)

        elif ( row['Crop_before']=='Cottan' or row['Crop_before']=='Cotton' or row['Crop_before']== 'cotton' or row['Crop_before']=='Cotton '):
            row['Crop_before'] = 'cotton'
            writer.writerow(row)

        elif ( row['Crop_before']=='Green Gram' or row['Crop_before']=='Green gram'):
            row['Crop_before'] = 'greengram'
            writer.writerow(row)

        elif ( row['Crop_before']=='paddy' or row['Crop_before']=='paddy  '  or row['Crop_before']=='Paady' or row['Crop_before']=='Paddy' or 
            row['Crop_before']=='Paddy ' ):
            row['Crop_before'] = 'paddy'
            writer.writerow(row)

        elif ( row['Crop_before']=='Potatao' or row['Crop_before']=='Potato'):
            row['Crop_before'] = 'potato'
            writer.writerow(row)

        elif ( row['Crop_before']=='Red' or row['Crop_before']=='Red Gram'):
            row['Crop_before'] = 'redgram'
            writer.writerow(row)

        elif ( row['Crop_before']=='Jonna/Senaga' or row['Crop_before']=='Jonna+ sunflower' or row['Crop_before']=='Mahendra Jonna' or
              row['Crop_before']=='Pacha Jonna' or row['Crop_before']=='Pacha Jonna' or 'Peasara + Pacha Gaddi'):
            row['Crop_before'] = 'jonna'
            writer.writerow(row)

        elif ( row['Crop_before']=='Vegetable' or row['Crop_before']=='Vegetables' or row['Crop_before']=='Vegitable'):
            row['Crop_before'] = 'vegetable'
            writer.writerow(row)

        elif ( row['Crop_before']=='JOWAR' or row['Crop_before']=='jowar' or row['Crop_before']=='Jowar'):
            row['Crop_before'] = 'jowar'
            writer.writerow(row)

        elif ( row['Crop_before']=='Paddy/G.nut' or row['Crop_before']=='Paddy/G.gram' or row['Crop_before']=='Paddy/Maize/G.N'):
            row['Crop_before'] = 'paddy/groundnut'
            writer.writerow(row)


        elif ( row['Crop_before']=='Eucaliptus' or row['Crop_before']=='Eucalyptus'):
            row['Crop_before'] = 'eucalyptus'
            writer.writerow(row)


        elif ( row['Crop_before']=='yam' or row['Crop_before']=='Yam'):
            row['Crop_before'] = 'yam'
            writer.writerow(row)

        elif ( row['Crop_before']=='Onian' or row['Crop_before']=='Oniyan'):
            row['Crop_before'] = 'onion'
            writer.writerow(row)


        elif ( row['Crop_before']=='chill' or row['Crop_before']=='Cowpea'):
            row['Crop_before'] = 'cowpea'
            writer.writerow(row)

        elif ( row['Crop_before']=='Cow pea' or row['Crop_before']=='Cowpea'):
            row['Crop_before'] = 'cowpea'
            writer.writerow(row)


        elif ( row['Crop_before']=='Oil Palm ' or row['Crop_before']=='Oil Palm'):
            row['Crop_before'] = 'oilpalm'
            writer.writerow(row)

        elif ( row['Crop_before']=='Turmaric' or row['Crop_before']=='Turmeric'):
            row['Crop_before'] = 'turmaric'
            writer.writerow(row)

        elif ( row['Crop_before']=='Sesamum' or row['Crop_before']=='Sesumum'):
            row['Crop_before'] = 'turmaric'
            writer.writerow(row)

        elif ( row['Crop_before']=='-' or row['Crop_before']=='Unknown' or row['Crop_before']=='Unknown ' ):
            row['Crop_before'] = 'unknown'
            writer.writerow(row)


        elif ( row['Crop_before']=='Cashew Nut' or row['Crop_before']=='Cashew Raina' or row['Crop_before']=='Cashew+Maize Cashewnut Cashewnut Cashewnut, Mango (Intercrop Maize And Seasamum)' or row['Crop_before']=='Cashewnut, Mango (Intercrop Maize And Seasamum)' or row['Crop_before']=='Cashewnut' or row['Crop_before']=='Cashew+Maize'):
            row['Crop_before'] = 'cashew'
            writer.writerow(row)
            

        else:
            writer.writerow(other)
