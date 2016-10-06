import numpy as np
import warnings

def polynomialMatrix(x_vector, grade) :
	a_matrix = []

	for x in x_vector:
		row = np.power(np.full((grade + 1), x), np.flipud(np.arange(grade + 1)))
		a_matrix.append(row)

	a_matrix = np.array(a_matrix)

	return a_matrix

def polynomialAproximation(x_vector, y_vector, grade) :
	a_matrix= polynomialMatrix(x_vector, grade)
	at_matrix = a_matrix.T

	at_a_inverse = np.linalg.inv((at_matrix.dot(a_matrix)))

	result = (at_a_inverse).dot(at_matrix).dot(y_vector)

	return result

def main():
	warnings.simplefilter("ignore")

if __name__ == "__main__" :
	main()
		

