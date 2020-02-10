import numpy as np
import pandas as pd

def r_outliers(incsv_file, outcsv_file):

    dataset = pd.read_csv(incsv_file)
    
    Q1 = dataset.quantile(0.25)
    Q3 = dataset.quantile(0.75)
    
    IQR = Q3 - Q1
    
    new_dataset = dataset[((dataset >= (Q1 - 1.5 * IQR)) &(dataset <= (Q3 + 1.5 * IQR))).all(axis=1)]
            
    new_dataset.to_csv(outcsv_file, index=False)
    print 'The no of rows removed:',len(dataset) - len(new_dataset)