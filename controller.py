import numpy as np 
import pandas as pd  
import pprint as pp

def install_to_numeric(nparray):
    for ele in nparray:
        value = "".join(ele[0][:-1].split(','))
        if value != None:
            ele[0] = int(value)
        else:
            ele[0] = np.nan
    return pd.DataFrame(nparray)
