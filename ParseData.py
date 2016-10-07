import numpy as np
import csv

data = './data.csv'

def parseCSV(file, delimiter):
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=delimiter)
		read_list = np.array(list(reader)).astype(np.float)

	return read_list.T

def getData(filedir):
	return parseCSV(filedir, ',')

