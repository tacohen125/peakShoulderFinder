 import numpy as np
 import pandas as pd
 from scipy import signal

 def peak_shoulder_index(y, frame=5, order=3, returnInflection=False, returnPeak=True, returnY=False, threshold=0.005):
     '''Determines the locations of peaks and inflection points of a signal.

     Iteratively performs a polynomial fitting in the data to detect its
     baseline. At every iteration, the fitting weights on the regions with
     peaks are reduced to identify the baseline only.
     Parameters
     ----------
     y : ndarray
         Data to detect the baseline.
     deg : int
         Degree of the polynomial that will estimate the data baseline. A low
         degree may fail to detect all the baseline present, while a high
         degree may make the data too oscillatory, especially at the edges.
     max_it : int
         Maximum number of iterations to perform.
     tol : float
         Tolerance to use when comparing the difference between the current
         fit coefficient and the ones from the last iteration. The iteration
         procedure will stop when the difference between them is lower than
         *tol*.
     Returns
     -------
     ndarray
         Array with the baseline amplitude for every original point in *y*'''

     yfilter = signal.savgol_filter(y, frame, order)

     inflection_points_index, peaks_index = index_return(yfilter, threshold=threshold)

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


def index_return(y_list, threshold=0.0025):
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
    differences_first_list = []
    #differences_second_list = []

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
            difference_first = all_lists.iloc[i:i+2]['dydy'].mean()
            differences_first_list.append(difference_first)
            #difference_second = all_lists.iloc[i]['dydy'] - all_lists.iloc[i-1]['dydy']
            #differences_second_list.append(difference_second)

        if not first_derivative_positive and second_derivative_negative:
            inflection_points_index.append(i)
            difference_first = all_lists.iloc[i:i+2]['dydy'].mean()
            differences_first_list.append(difference_first)
            #difference_second = all_lists.iloc[i]['dydy'] - all_lists.iloc[i-1]['dydy']
            #differences_second_list.append(difference_second)

    inflection_points = pd.DataFrame(
        {'indexes': inflection_points_index,
         'differences first': differences_first_list,
         #'differences second': differences_second_list
        })

    #inflection_points_index = [int(i) for i in np.abs(inflection_points).sort_values('differences', ascending = True).reset_index(drop = True).loc[:number_of_inflections-1]['indexes'].tolist()]

    inflection_points_index = inflection_points[np.abs(inflection_points['differences first'])<threshold]['indexes'].values

    return inflection_points_index, peaks_index
