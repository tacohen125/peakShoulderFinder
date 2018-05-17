'''
Input a y list, and peak_shoulder_finder will return a list of indexes for all
inflection points and all peaks

inflection_points_index, peaks_index = peak_shoulder_finder(y_list)

'''

def peak_shoulder_finder(y_list):

    dy = np.diff(y_list)
    dydy = np.diff(dy)

    y_list = yactual_4[2:].tolist()
    dy_list = dy[1:].tolist()
    dydy_list = dydy.tolist()

    all_lists = pd.DataFrame(
        {'y': y_list,
         'dy': dy_list,
         'dydy': dydy_list}
    )

    inflection_points_index = []
    peaks_index = []

    for i in range(0, len(all_lists)-1):

        first_derivative = all_lists.iloc[i-1]['dy'] >= 0 >= all_lists.iloc[i]['dy']
        first_derivative_positive = all_lists.iloc[i-1]['dy'] > 0
        first_derivative_negative = all_lists.iloc[i-1]['dy'] < 0
        second_derivative_positive = all_lists.iloc[i-1]['dydy'] <= 0 <= all_lists.iloc[i]['dydy']
        second_derivative_negative = all_lists.iloc[i-1]['dydy'] >= 0 >= all_lists.iloc[i]['dydy']

        if first_derivative:
            peaks_index.append(i)

        if first_derivative_positive and second_derivative_positive:
            inflection_points_index.append(i)

        if not first_derivative_positive and second_derivative_negative:
            inflection_points_index.append(i)

    return inflection_points_index, peaks_index