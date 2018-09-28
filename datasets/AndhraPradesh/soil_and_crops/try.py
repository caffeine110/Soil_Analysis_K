##########################################################
import pandas as pd

filepath = 'only_crops.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Crop_before'])
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
labelEncoder_croptype.fit(df['Crop_before'])
labelEncoder_croptype.classes_

##########################################################


### soil types
##########################################################

import pandas as pd

filepath = 'SOIL.csv'
df = pd.read_csv(filepath)

from sklearn import preprocessing
labelEncoder_croptype = preprocessing.LabelEncoder()
labelEncoder_croptype.fit(df['Soil_type'])
labelEncoder_croptype.classes_

df.info
df.count()
df.columns

##########################################################
