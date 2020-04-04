import sys 
import numpy as np

# command line: 
# python ex1.py < input.txt to read input.txt as input 

def scrivi(result):
	for i in range(0, len(result)):
		print("Case #{}: {}".format(i+1, result[i]))

def solution(s,T):
	result = list()
	for i in range(0,T):
		sol = s[i]

		n = 0
		index = 0
		for c in range(0,len(s[i])):
			num = int(s[c])
			print(sol[index])
			if(num > n):
				to_add = num - n
				sol = sol[:index] + (to_add *'(') + sol[index:]
				index+=to_add +1

			elif(n>num):
				to_close = n-num
				sol =  sol[:index] + to_close * ')' + sol[index:]
				index+=to_close	+1			

		result.append(sol)

	return result

if __name__ == '__main__':
	
	strings = list()
	T = int(input())

	for i in range(0, T):
		strings.append(input().replace(' ',''))

	result = solution(strings,T)
	scrivi(result)