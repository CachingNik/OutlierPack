# A library capable of removing outliers from a pandas dataframe

```
PROJECT 2, UCS633 - Data Analysis and Visualization
Nikhil Gupta  
COE17
Roll number: 101703371
```
Output is the number of rows removed from the input dataset. The remaining rows of the dataset are streamed to a new csv file whose name is required as an input.

`The no of rows removed: 5`

## Installation
`pip install outlierpack_NG`

*Note the name has an underscore not a hyphen. If installation gives error or package is not found after installing, install as sudo.*

*Recommended - test it out in a virtual environment.* 

## To use via command line
`outcli myData.csv newData.csv`

First argument after outcli is the input csv filename from which the dataset is extracted. The second argument is for storing the final dataset after processing.

## To use in .py script
```
from outlib.models import r_outliers
r_outliers('myData.csv', 'newData.csv')
```

*Can email me for any issues or suggestions*
