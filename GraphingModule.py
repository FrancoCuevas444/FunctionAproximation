import AproximationModule as aprox
import numpy as np
import matplotlib.pyplot as plt
import warnings

def plotOriginalData(x_vector, y_vector):
	myDotGraph = plt.subplot(111)
	myDotGraph.plot(x_vector, y_vector, 'go')
	myDotGraph.set_xlim([x_vector.min() - 1,x_vector.max() + 1])
	myDotGraph.set_ylim([y_vector.min() - 10,y_vector.max() + 10])

def plotPolynomialFunction(x_vector, y_vector, grade):
	x_range = np.arange(x_vector.min() - 1,x_vector.max() + 1, 0.05)
	y_results = aprox.polynomialAproximation(x_range, x_vector, y_vector, grade)

	myFuncGraph = plt.subplot(111)
	myFuncGraph.plot(x_range, y_results)

def main():
	warnings.simplefilter("ignore")
	x_vector = np.array([-1, 1, 2, 3, 4, 5, 6])
	y_vector = np.array([4, 24 ,-1, 115, 40, 2, 9])
	
	plotOriginalData(x_vector, y_vector)
	plotPolynomialFunction(x_vector, y_vector, 3)
	plt.show()

main()
