import numpy as np
import pandas as pd
from scipy import signal
import peak_shoulder_finder as psf

def overall(y, frame=5):
    '''
Input a y list, and peak_shoulder_finder will filter the function first,
then return a list of indexes for all
inflection points and all peaks
inflection_points_index, peaks_index = peak_shoulder_finder(y_list)

'''

    yfilter = signal.savgol_filter(yrand, frame, 3)

	psf.index_return(yfilter)
	
	return inflection_points_index, peaks_index