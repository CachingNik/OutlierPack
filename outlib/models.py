import numpy as np
import pandas as pd

def r_outliers(incsv_file, outcsv_file):

    dataset = pd.read_csv(incsv_file)

    d = dataset.iloc[:,1:]  

    for i, row in d.iterrows():
        threshold = 3
        mean = np.mean(row)
        std = np.std(row)
        for value in row:
            z_score = (value-mean)/std
            if np.abs(z_score)>threshold:
                dataset = dataset.drop(d.index[i])
                break
            
    dataset.to_csv(outcsv_file, index=False)
    print 'The no of rows removed:',len(d) - len(dataset)