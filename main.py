from flask import Flask, render_template,request,jsonify

from phase_3_model_DNN import crop_prediction
from phase_4_fertilizers_required import fertilizers_required



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


#get_fertilizers_required
@app.route("/get_fertilizers_required", methods=["POST"])
def get_fertilizers():
    
    if request.method == "POST":		

        """
        test_soil_para = ['Latitude', 'Longitude', 'Soil_type', 'Crop_type', 'pH', 'EC', 'OC',
               'Avail_P', 'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn',
               'Avail_B', 'Avail_Fe', 'Avail_Cu', 'Avail_Mn']
        """


        Latitude = request.form['Latitude']
        Longitude = request.form['Longitude']
        #Soil_type = request.form['Soil_type']
        #Crop_type = request.form['Crop_type']
        pH = request.form['pH']
        EC = request.form['EC']
        OC = request.form['OC']
        Avail_P = request.form['Avail_P']
        Exch_K = request.form['Exch_K']
        Avail_Ca = request.form['Avail_Ca']
        Avail_Mg = request.form['Avail_Mg']
        Avail_S = request.form['Avail_S']
        Avail_Zn = request.form['Avail_Zn']
        Avail_B = request.form['Avail_B']
        Avail_Fe = request.form['Avail_Fe']
        Avail_Cu = request.form['Avail_Cu']
        Avail_Mn = request.form['Avail_Mn']
        #= request.form['']

         
        test_soil_para = list()
        test_soil_para = [ Latitude, Longitude, pH, EC, OC, Avail_P,
                          Exch_K, Avail_Ca, Avail_Mg, Avail_S, Avail_Zn, Avail_B,
                          Avail_Fe, Avail_Cu, Avail_Mn]
    

        test_soil_para_get_crop_type = [ Latitude, Longitude, pH, EC, OC, Avail_P,
                          Exch_K, Avail_Ca, Avail_Mg, Avail_S, Avail_Zn, Avail_B,
                          Avail_Fe, Avail_Cu, Avail_Mn]

        
        test_soil_para_get_crop_type = [ float(i) for i in test_soil_para_get_crop_type ]
        
        #default
        #test_soil_para_get_crop_type = [13,14,1.073756,13.111439205,7.3076,0.20419851113,0.386997517,16.994856,06.0894044665,1461.48171638,275.1377171215881,13.750777171,0.93561339956,0.551166257362,11.470392332515 ]

        #test_soil_para_get_crop_type = [ 16.72,80.36,2.57,10.42,8.48,0.31,0.54,24.1,212.0,6050.0,1066.0,36.49,0.58,1.94,24.91 ]
        
        #test_soil_para_get_crop_type = [ 16.19,80.86,3.68,20.5,8.31,0.76,0.71,26.23,527.0,4669.0,592.0,84.5,4.84,1.23,13.0 ]
        
        #blackgram = 
        #test_soil_para_get_crop_type = [ 13.01,78.55,1.92,17.69,7.3,0.43,0.7,6.0,64.0,1453.0,387.0,41.15,2.58,0.71,16.97 ]
        
        #jonna = 
        #test_soil_para_get_crop_type = [ 17.68,82.89,0.68,17.24,8.38,2.52,0.43,14.57,2037.0,869.0,223.0,184.3,0.86,1.84,6.26 ]
        
        #test_soil_para_get_crop_type = [ 14.49,80.06,2.72,7.7,8.4,0.77,0.5,4.25,89.0,2763.0,533.0,126.93,1.8,1.72,44.02 ]
        
        #jonna = 
        #test_soil_para_get_crop_type = [ 15.49,79.48,2.28,14.46,8.95,0.37,0.58,10.52,346.0,2529.0,820.0,24.48,0.54,2.68,29.64 ]


        Crop_type = crop_prediction.get_best_fitting_Crop(test_soil_para_get_crop_type)

        #attempted_ = request.form['']



        test_soil_para_get_fertilizers_req = [ pH, EC, OC, Avail_P,
                          Exch_K, Avail_Ca, Avail_Mg, Avail_S, Avail_Zn, Avail_B,
                          Avail_Fe, Avail_Cu, Avail_Mn ]

        test_soil_para_get_fertilizers_req = [ float(i) for i in test_soil_para_get_fertilizers_req ]

        #default
        #test_soil_para_get_fertilizers_req = [1.073756,13.111439205,7.3076,0.20419851113,0.386997517,16.994856,06.0894044665,1461.48171638,275.1377171215881,13.750777171,0.93561339956,0.551166257362,11.470392332515 ]

        result_string = [ 'pH', 'EC', 'OC', 'Avail_P',
                          'Exch_K', 'Avail_Ca', 'Avail_Mg', 'Avail_S', 'Avail_Zn', 'Avail_B',
                          'Avail_Fe', 'Avail_Cu', 'Avail_Mn', 'Crop_type']

        result = fertilizers_required.get_fertilizers_required(test_soil_para_get_fertilizers_req)
        result.append(Crop_type)
        
        print(result)
        # labels = [ pH, EC, OC, Avail_P,Exch_K, Avail_Ca, Avail_Mg, Avail_S, Avail_Zn, Avail_B,Avail_Fe, Avail_Cu, Avail_Mn ]
        return render_template('result.html',result=result,result_string=result_string,n=len(result))
        # return jsonify(result)

        #return render_template('index.html')



#@app.route("/about")
#def about():
#    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)
