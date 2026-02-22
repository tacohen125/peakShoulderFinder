# Peak Shoulder Finder

[![Build Status](https://travis-ci.org/tacohen125/peakShoulderFinder.svg?branch=master)](https://travis-ci.org/tacohen125/peakShoulderFinder)
[![Coverage Status](https://coveralls.io/repos/github/tacohen125/peakShoulderFinder/badge.svg?branch=master)](https://coveralls.io/github/tacohen125/peakShoulderFinder?branch=master)

## Package for Peak Shoulder Finding and Analysis
This package applies a Savitzky-Golay filter to data to reduce the noise in the raw data. The Savitzky-Golay filter is used to smooth the data and hopefully increase the signal-to-noise ratio without greatly distorting the original data. This is done by fitting subsets of data with a low degree polynomial to minimize the RMSE. 

The filtered data is then fed into the peak_shoulder_finder.py function that uses first and second differentials to find the peaks and shoulders of the dataset.

In the organization of this project, find examples of the function under docs, where several python notebooks walk through the function. 

In the Data function, find the data that is used in the examples

In the peakShoulderFinder file, find the python functions that are used in this function.  

### How to Install 
```
pip install peakshoulderfinder  
```
### Software Dependencies 
- Python3 
- For python packages see requirements.txt

## Organization of the project
```
Data/
    Dataset1/
    Dataset2/
    Dataset3
docs/
    Makefile/
    conf.py
examples/
    second_derivative_calculator.ipynb/
python_demo/ 
    __init__.py/
    peak_shoulder_finder.py/
    version.py
README.md
requirements.txt
```

## Preview of function

chage to test pushing