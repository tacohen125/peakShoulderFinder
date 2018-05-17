import numpy as np
import pandas as pd
import peak_shoulder_finder as pks

def test_index_return():

	#generates a test case
	pts=25 

	x=np.linspace(-5,5,num=pts)

	yactual_1 = np.sin(x * 0.5*np.pi)
	yactual_2 = -(0.5 * (x-2))**2
	yactual_3 = -(0.5* (x+2))**2
	yactual = yactual_1 + yactual_2 + yactual_3

	#runs the function
	inflection_points_index, peak_index = pks.index_return(yactual)

	assert isinstance(inflection_points_index, list), 'the inflection point output is not a list'
	assert isinstance(peak_index, list), 'the peak point output is not a list'

	assert all(isinstance(item, int) for item in inflection_points_index), 'the inflection indices are not integers'
	
	return