import numpy as np
import pandas as pd
from scipy import signal

def overall(y, frame=5, order=3, returnInflection=False, returnPeak=True, returnY=False):
    '''
Input a y list, and peak_shoulder_finder will filter the function first,
then return a list of indexes for all
inflection points and all peaks
inflection_points_index, peaks_index = peak_shoulder_finder(y_list)

'''

    yfilter = signal.savgol_filter(y, frame, order)

    inflection_points_index, peaks_index = index_return(yfilter)
	
    if returnY == False:
        if returnInflection == True and returnPeak == True:
            return peaks_index, inflection_points_index
        elif returnInflection == False and returnPeak == True:
            return peaks_index
        else:
            return inflection_points_index

    else:
        if returnInflection == True and returnPeak == True:
            return peaks_index, inflection_points_index, yfilter
        elif returnInflection == False and returnPeak == True:
            return peaks_index, yfilter
        else:
            return inflection_points_index, yfilter

def index_return(y_list):
    '''
Input a y list, and peak_shoulder_finder will return a list of indexes
for all inflection points and all peaks

inflection_points_index, peaks_index = peak_shoulder_finder(y_list)

'''

    # calculate the first and second derivatives of the y list
    dy = np.diff(y_list)
    dydy = np.diff(dy)

    # convert values to list and dataframe
    y_list = y_list[2:].tolist()
    dy_list = dy[1:].tolist()
    dydy_list = dydy.tolist()
    all_lists = pd.DataFrame(
        {'y': y_list,
         'dy': dy_list,
         'dydy': dydy_list})

    inflection_points_index = []
    peaks_index = []

    for i in range(0, len(all_lists)-1):

        #calculate the directions of the first and second derivatives
        #if the first and second derivate pass through zero from positive to
        #negative or vice versa
        first_derivative = (all_lists.iloc[i-1]['dy']>=0
                                >= all_lists.iloc[i]['dy'])
        first_derivative_positive = all_lists.iloc[i-1]['dy']>0
        first_derivative_negative = all_lists.iloc[i-1]['dy']<0
        second_derivative_positive = (all_lists.iloc[i-1]['dydy']<=0
                                        <=all_lists.iloc[i]['dydy'])
        second_derivative_negative = (all_lists.iloc[i-1]['dydy']>=0
                                        >=all_lists.iloc[i]['dydy'])

        #add the desired first and second derivatives to a list and return
        if first_derivative:
            peaks_index.append(i)

        if first_derivative_positive and second_derivative_positive:
            inflection_points_index.append(i)

        if not first_derivative_positive and second_derivative_negative:
            inflection_points_index.append(i)


    return inflection_points_index, peaks_index
