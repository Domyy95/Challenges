import sys 
import numpy as np

# command line: 
# python ex1.py < input.txt to read input.txt as input 

def scrivi(result):
	for i in range(0, len(result)):
		print("Case #{}: {} {} {}".format(i+1, result[i][0] , result[i][1],result[i][2]))

def solution(M,T):
	results = list()
	for i in range(0,T):
		matrix = M[i]
		matrix = matrix.astype(np.int)
		trace = np.sum(matrix.diagonal())
		col = 0
		rows = 0
		l = len(matrix[0])
		for r in range(0,l):
			unique = np.unique(matrix[r])
			if len(unique) < l:
				rows+=1
			unique = np.unique(matrix[:,r])
			if len(unique) < l:
				col+=1

		results.append((trace,rows,col))

	return results

if __name__ == '__main__':
	
	Matrix = []


	T = int(input())
	for i in range(0, T):
		n = int(input())
		m = np.array([])
		for j in range(i,i+n):
			row = input()
			row = list(row.split())
			m = np.append(m,row)

		m.shape=(n,n)
		Matrix.append(m)

	result = solution(Matrix,T)
	scrivi(result)