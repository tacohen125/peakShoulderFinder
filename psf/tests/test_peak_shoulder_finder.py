import numpy as np
import pandas as pd
import psf

def test_index_return():

	#generates a test case
	pts=25

	x=np.linspace(-5,5,num=pts)

	yactual_1 = np.sin(x * 0.5*np.pi)
	yactual_2 = -(0.5 * (x-2))**2
	yactual_3 = -(0.5* (x+2))**2
	yactual = yactual_1 + yactual_2 + yactual_3

	#runs the function
	inflection_points_index, peak_index = psf.index_return(yactual)

	assert isinstance(inflection_points_index, list), 'the inflection point output is not a list'
	assert isinstance(peak_index, list), 'the peak point output is not a list'

	assert all(isinstance(item, int) for item in inflection_points_index), 'the inflection indices are not integers'
	assert all(isinstance(item, int) for item in peak_index), 'the peak indices are not integers'

	assert all(item >= 0 for item in inflection_points_index), 'the inflection indices are not positive'
	assert all(item >= 0 for item in peak_index), 'the peak indices are not positive'

	assert (max(inflection_points_index) <= len(yactual)-1), 'the inflection point output contains an index that is too large'
	assert (max(peak_index) <= len(yactual)-1), 'the peak point output contains an index that is too large'

	assert (len(inflection_points_index) == 2), 'the inflection points list is not the right size'
	assert (len(peak_index) == 1), 'the peak points list is not the right size'

	return
