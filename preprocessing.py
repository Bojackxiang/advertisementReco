import numpy as np 
import pandas as pd  
import pprint as pp
from sklearn.preprocessing import Imputer
from controller import *

picking_up_category = "Art & Design"
dataset = pd.read_csv('./dataset.csv')
category_data = dataset.loc[dataset['Genres'] == picking_up_category]
rate = category_data.iloc[:, 2:3]

# ! change the review to int
reviews = category_data.iloc[:, 3:4]
reviews = reviews.astype(int) 

# ! cahnge the string to float number
size = category_data.iloc[:, 4:5].values
for ele in size:
    if len(ele[0]) > 10:
        ele[0] = float('nan')
    else:
        ele[0] = float(ele[0][:-1])
size = pd.DataFrame(size)

# ! processing the install 
install = category_data.iloc[:, 5:6].values
preprocess_install = install_to_numeric(install)

# ! 构建 X, y
X = pd.concat([rate, reviews, size], axis=1).values
imputer_rate = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer_rate = imputer_rate.fit(X[:, 0:4])
new_rate = imputer_rate.transform(X[:, 0:4])
X[:, 0:4] = new_rate
X_dataframe = pd.DataFrame(X)
print(type(X_dataframe))
X_dataframe.to_csv('X.csv')
y = preprocess_install

# * 到目前为止，数据预处理里已经完成，x，y，









# X = pd.concat([dataset.iloc[:, 2:3], dataset.iloc[:, 3:4], dataset.iloc[:, 4:5], )
# imputer = Imputer(missing_values="nan", strategy="mean", axis=0)


# imputer = imputer.fit(dataset[:, 2:3])
# new_rating = imputer.tranform(dataset[:, 2:3])
# print(new_rating)
# preprocessed_data = pd.concat([dataset.iloc[:, 2:3], dataset.iloc[:, 3:4], dataset.iloc[:, 4:5], dataset.iloc[:, 8:9]], axis=1)


# ! <class 'pandas.core.frame.DataFrame'>
# pp.pprint(type(dataset.iloc[:, 2:3]))
# ! <class 'numpy.ndarray'>
# pp.pprint(type(useful_data.values))



# print(type(number_list))
# number_list.astype('int64')
# print(type(number_list))



