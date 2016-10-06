import numpy as np
import warnings

def polynomialMatrix(x_vector, grade):
	A_matrix = []

	for x in x_vector:
		row = np.power(np.full((grade + 1), x), np.flipud(np.arange(grade + 1)))
		A_matrix.append(row)

	A_matrix = np.array(A_matrix)

	return A_matrix

def main():
	warnings.simplefilter("ignore")
	my_matrix = polynomialMatrix([2, 1, 1, 1, 1 ,1, 2], 10)
	print my_matrix

if __name__ == "__main__" :
	main()
		

