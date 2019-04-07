import sys 

def scrivi(result):
	for i in range(0, len(result)):
		print("Case #{}: {} ".format(i+1, result[i] ))

def risolvi(n,p):
	rev = p[::-1]
	n = int(n)
	tot = 2*n - 2
	meta = (tot / 2)
	meta = int (meta)

	if(p[0] == 'E'):
		if(p[len(p) - 1] == 'S'):
			sol = 'S'* meta + 'E' * meta
		else:
			t = True
			i = 0
			ponte = 0
			while t:
				if(p[i] == 'S'):
					ponte = ponte + 1
				if(p[i] == 'S' and p[i+1] == 'S'):
					t = False 
				i = i+1
			sol = 'S'* ponte + 'E'*meta + 'S'* (meta - ponte)

	else:
		if(p[len(p) - 1] == 'E'):
			sol = 'E'* meta + 'S' * meta
		else:
			t = True
			i = 0
			ponte = 0
			while t:
				if(p[i] == 'E'):
					ponte = ponte + 1
				if(p[i] == 'E' and p[i+1] == 'E'):
					t = False 
				i = i+1
			sol = 'E'* ponte + 'S'*meta + 'E'* (meta - ponte)

	return sol



if __name__ == '__main__':
	result = []
	N = int(input())
	for i in range(1, N + 1 ):
		n = input()
		p = input()
		sol = risolvi(n,p)
		result.append(sol)

	scrivi(result)