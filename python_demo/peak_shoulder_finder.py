import numpy as np
import pandas as pd
from scipy import signal

def peak_shoulder_index(y, frame=5, order=3, returnInflection=False,
        returnPeak=True, returnY=False, min_dist = 1):
    '''Determines the locations of peaks and inflection points of a signal.

    Iteratively performs a polynomial fitting on the data to detect its
    baseline. At every iteration, the fitting weights on the regions with
    peaks are reduced to identify the baseline only.

    Parameters
    ---------
    y : ndarray
        Data to detect the baseline.
    frame: int (default = 5)
        The length of the filter window; the frame must be a positive odd
        integer.
    order : int (default = 3)
        Degree of the polynomial that will estimate the data baseline. A low
        degree may fail to detect all the baseline present, while a high
        degree may make the data too oscillatory, especially at the edges.
        order must be less than frame
    min_dist : int (default = 1)
        Minimium distance between shoulder index points.
    returnInflection : bool (default = False)
        Adds an additional output that contains the indices of the curve
        shoulders.
    returnPeak bool (default = True)
        Adds an output that contains the indices of the peaks.
    returnY : bool (default = False)
        Adds an additional output that contains the filtered y data.

    Returns
    -------
    peaks_index : lst
        Indexes for the peak locations.
    inflection_points_index : lst (optional)
        Indexes for the shoulder locations.
    yfilter : lst (optional):
        Filtered y data.'''

    yfilter = signal.savgol_filter(y, frame, order)

    inflection_points_index, peaks_index = index_return(yfilter,
            min_dist = min_dist)

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


def index_return(y_list, min_dist = 1):
    '''
    Input a y list, and index_return will return a list of indexes for
    all shoulder locations and peak locations

    Parameters
    ---------
    y_list : ndarray
        Data to detect the baseline.
    min_dist : int (default = 1)
        Minimium distance between shoulder index points.

    Returns
    -------
    peaks_index : lst
        Indexes for the peak locations.
    inflection_points_index : lst
        Indexes for the shoulder locations.'''

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
    differences_first_list = []
    differences_second_list = []

    for i in range(0, len(all_lists)-1):

        #calculate the directions of the first and second derivatives
        #if the first and second derivate pass through zero from positive to
        #negative or vice versa
        first_derivative = (all_lists.iloc[i]['dy']>=0
                                >= all_lists.iloc[i+1]['dy'])
        first_derivative_positive = all_lists.iloc[i]['dy']>=0
        first_derivative_negative = all_lists.iloc[i]['dy']<0
        second_derivative_positive = (all_lists.iloc[i]['dydy']<=0
                                        <=all_lists.iloc[i+1]['dydy'])
        second_derivative_negative = (all_lists.iloc[i]['dydy']>=0
                                        >=all_lists.iloc[i+1]['dydy'])

        #add the desired first and second derivatives to a list and return
        if first_derivative:
            peaks_index.append(i)

        if first_derivative_positive and second_derivative_positive:
            inflection_points_index.append(i)
            difference_first = all_lists.iloc[i]['dy']
            differences_first_list.append(difference_first)
            difference_second = all_lists.iloc[i]['dydy']
            differences_second_list.append(difference_second)

        if first_derivative_negative and second_derivative_negative:
            inflection_points_index.append(i)
            difference_first = all_lists.iloc[i]['dy']
            differences_first_list.append(difference_first)
            difference_second = all_lists.iloc[i]['dydy']
            differences_second_list.append(difference_second)

    inflection_points = pd.DataFrame(
        {'indexes': inflection_points_index,
         'differences first': differences_first_list,
         'differences second': differences_second_list
        })

    inflection_points['Bool'] = 0

    for i in range(0,(len(inflection_points)-1)):
        if difference_first > 0:
            if ((inflection_points['indexes'].iloc[i+1]
                    - inflection_points['indexes'].iloc[i]) < min_dist):
                if (inflection_points['differences first'].iloc[i+1]
                        > inflection_points['differences first'].iloc[i]):
                    inflection_points['Bool'].iloc[i]= 1
            else:
                inflection_points['Bool'].iloc[i] = 1
        else:
            if ((inflection_points['indexes'].iloc[i+1]
                    - inflection_points['indexes'].iloc[i]) < min_dist):
                if (inflection_points['differences first'].iloc[i+1]
                        < inflection_points['differences first'].iloc[i]):
                    inflection_points['Bool'].iloc[i]= 1
            else:
                inflection_points['Bool'].iloc[i] = 1

    inflection_points_index = (inflection_points[inflection_points['Bool']==1]
                                    ['indexes'].values)

    return inflection_points_index, peaks_index
