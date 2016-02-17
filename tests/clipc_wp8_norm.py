# python
# KNMI clipc
# author: andrej
# clipc@knmi.nl
import numpy as np

# normalisation functions
#
# normalisation functions 
# requested by johannes
#

# min max normalisation
# also feature scaling...
def normA(X):
	minX = np.min(X)
	maxX = np.max(X)

	return ((X -  minX ) / ( maxX - minX ))

# normalisation by standardisation
# standard score
def normB(X):
	meanX = np.mean(X)
	stdX  = np.std(X)

	return (X - meanX) / stdX

# norm by percentiles...
def normC(X):
	return 0