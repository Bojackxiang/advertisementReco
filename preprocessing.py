import numpy as np 
import pandas as pd  
import pprint as pp
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import modules
from controller import *

def dispose(Genres):
    
    picking_up_category = Genres
    dataset = pd.read_csv('./dataset.csv')
    category_data = dataset.loc[dataset['Category'] == picking_up_category]


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
    #print(X)
    imputer_rate = Imputer(missing_values="NaN", strategy="mean", axis=0)

    imputer_rate = imputer_rate.fit(X[:, 0:3])
    new_rate = imputer_rate.transform(X[:, 0:4])
    #print(new_rate)
    X[:, 0:4] = new_rate
    y = install
    
    # ! 开始训练模型
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    #pp.pprint(X_train)
    
    regression = LinearRegression()
    regression.fit(X_train, y_train)
    # pp.pprint(type(X_test))
    my_test = np.array([[4, 7, 8]])
    y_pred = regression.predict(my_test)
    
    

def top10(Genres):
    picking_up_category = Genres
    dataset = pd.read_csv('./dataset.csv')
    category_data = dataset.loc[dataset['Category'] == picking_up_category]
    category_data['Installs'] = category_data['Installs'].astype(str).str[:-1]
    category_data['Installs'] = category_data['Installs'].map(lambda x: int("".join(x.split(','))))
    category_data = category_data.sort_values(by=['Installs'],ascending = False).head(10)
    key = []
    value = []
    dict1 = {}
    for e in category_data['App']:
        key.append(e)
    for e in category_data['Installs']:
        value.append(e)
    for i in range(len(key)):
        dict1[key[i]] = value[i]
    name = category_data.iloc[:, 0:1]
    install = category_data.iloc[:, 5:6]    
    X = pd.concat([name, install], axis=1).values
    print(dict1)
    return dict1

def findUniqueCate():
    dataset = pd.read_csv('./dataset.csv')
    generList = dataset.loc[:, 'Category'].unique()[:-1]
    return generList
    
def main():
    dispose('MEDICAL')

if __name__=='__main__':
    main()

    





