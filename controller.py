import numpy as np 
import pandas as pd  
import pprint as pp

def install_to_numeric(nparray):
    new_data = []
    for ele in nparray:
        value = "".join(ele[0][:-1].split(','))
        if value != None:
            new_data.append(int(value))
        else:
            new_data.append(np.nan)
    # return pd.DataFrame(nparray)
    return np.asarray(new_data)
