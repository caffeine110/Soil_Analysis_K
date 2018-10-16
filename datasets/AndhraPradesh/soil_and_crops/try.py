##########################################################

import pandas as pd

filepath = 'only_crops.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_type'])
labelEncoder_croptype.classes_

##########################################################


### soil types
##########################################################

import pandas as pd

filepath = 'only_soil_types.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Soil_type'])
labelEncoder_croptype.classes_

df.info
df.count()
df.columns

##########################################################





### soil types
##########################################################
import pandas as pd

filepath = 'CROPS.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_type'])
labelEncoder_croptype.classes_

### soil types
##########################################################
import pandas as pd

filepath = 'stemed_crops.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_type'])
labelEncoder_croptype.classes_


##########################################################

################### TEMP EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

import pandas as pd

filepath = 'datasets/AndhraPradesh/preprocessing/Temp.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_type'])
labelEncoder_croptype.classes_


################### TEMP EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

import pandas as pd

filepath = 'datasets/AndhraPradesh/preprocessing/1.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_type'])
labelEncoder_croptype.classes_


### soil types
##########################################################

import pandas as pd

filepath = 'datasets/AndhraPradesh/preprocessing/SOIL.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Soil_type'])
labelEncoder_croptype.classes_

df.info
df.count()
df.columns

##########################################################


import pandas as pd

filepath = 'original_details_ap.csv'
df = pd.read_csv(filepath, delimiter=";")

print(df['OC'])

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Soil_type'])
labelEncoder_croptype.classes_

df.info
df.count()
df.columns



