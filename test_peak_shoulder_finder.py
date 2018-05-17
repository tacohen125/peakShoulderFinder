import numpy as np
import pandas as pd
import peak_shoulder_finder as pks

def test_index_return():

	pts=25 

	x=np.linspace(-5,5,num=pts)

	yactual_1 = np.sin(x * 0.5*np.pi)
	yactual_2 = -(0.5 * (x-2))**2
	yactual_3 = -(0.5* (x+2))**2
	yactual = yactual_1 + yactual_2 + yactual_3

	inflection_points_index, peak_index = pks.index_return(yactual)


	return