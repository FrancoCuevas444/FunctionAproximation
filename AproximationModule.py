import numpy as np
import warnings

def polynomialMatrix(x_vector, grade) :
	a_matrix = []

	for x in x_vector:
		row = np.power(np.full((grade + 1), x), np.flipud(np.arange(grade + 1)))
		a_matrix.append(row)

	a_matrix = np.array(a_matrix)

	return a_matrix

def leastSquare(a_matrix, y_vector) :
	at_matrix = a_matrix.T

	at_a_inverse = np.linalg.inv((at_matrix.dot(a_matrix)))
	result = ((at_a_inverse).dot(at_matrix)).dot(y_vector)

	return result

def polynomialFuncEval(x_range, coef):
	grade = len(coef)
	y_results = np.empty(shape = (0,0))

	for x in x_range :
		x_values = np.power(np.full((grade), x), np.flipud(np.arange(grade)))
		result = x_values.dot(coef)
		y_results = np.append(y_results, result)

	return y_results

def polynomialAproximation(x_range, x_vector, y_vector, grade) :
	a_matrix = polynomialMatrix(x_vector, grade)
	coef = leastSquare(a_matrix, y_vector)
	y_graph = polynomialFuncEval(x_range, coef)
	return y_graph


		

