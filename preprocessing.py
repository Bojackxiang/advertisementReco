import numpy as np 
import pandas as pd  
import pprint as pp
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import modules
from controller import *


picking_up_category = "Art & Design"
dataset = pd.read_csv('./dataset.csv')
category_data = dataset.loc[dataset['Genres'] == picking_up_category]

# ! obtain the rating (success)
rate = category_data.iloc[:, 2:3]

# ! change the review to int (success)
reviews = category_data.iloc[:, 3:4]
reviews = reviews.astype(int)

# ! cahnge the string to float number (success)
size = category_data.iloc[:, 4:5]
size['Size'] = size['Size'].astype(str).str[:-1]
size['Size'] = size['Size'].replace({'Varies with devic': np.nan})
size['Size'] = size['Size'].map(lambda x: float(x))

# ! processing the install (success)
install = category_data.iloc[:, 5:6]
install['Installs'] = install['Installs'].astype(str).str[:-1]
install['Installs'] = install['Installs'].map(lambda x: int("".join(x.split(','))))

# ! 构建 X, y
X = pd.concat([rate, reviews, size], axis=1).values
imputer_rate = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer_rate = imputer_rate.fit(X[:, 0:3])
new_rate = imputer_rate.transform(X[:, 0:4])
X[:, 0:4] = new_rate
y = install

# ! 开始训练模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
pp.pprint(X_train)
regression = LinearRegression()
regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)







