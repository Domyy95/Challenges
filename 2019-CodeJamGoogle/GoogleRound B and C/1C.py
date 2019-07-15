import sys 

def scrivi(result):
	for i in range(0, len(result)):
		print("Case #{}: {}".format(i+1, result[i]))

def risolvi(P,M):

	moves = []
	len_moves = len(M[0])
	maxlen = len_moves
	for i in range(0,len(M)):
		m = []
		len_moves = len(M[i])
		if (len_moves > maxlen):
			maxlen = len_moves
		for j in range(0,len_moves):
			m.append(M[i][j])

		moves.append(m)

	for i in range(0,len(M)):
		if(len(moves[i]) < maxlen):
			eccolo = True
			while eccolo:
				moves[i].extend(moves[i])
				if(len(moves[i]) > maxlen):
					eccolo = False

	sol = ''
	for conta in range(0,maxlen):
		r,p,s = 0,0,0
		for i in range(0,int(P)):
			if(moves[i][conta] == 'R'):
				r = 1
			if(moves[i][conta] == 'P'):
				p = 1
			if(moves[i][conta] == 'S'):
				s = 1
			if(p ==1 and s ==1 and r ==1):
				return 'IMPOSSIBLE'

		if( p == 0 and s == 0 and r ==1):
			return sol + 'P'
		if( p == 1 and s == 0 and r ==0):
			return sol + 'S'
		if( p == 0 and s == 1 and r ==0):
			return sol + 'R'
		if( p == 0 and s == 1 and r ==1):
			sol = sol + 'R'
		elif( p == 1 and s == 0 and r ==1):
			sol = sol + 'P'
		elif( p == 1 and s == 1 and r ==1):
			sol = sol + 'S'

		if(len(sol) > 500):
				return 'IMPOSSIBLE'

	return 'IMPOSSIBLE'
	
if __name__ == '__main__':
	result = []
	N = int(input())
	for i in range(0,N):
		players = input()
		moves = []
		for j in range(0,int ( players)):
			mossa = input()
			moves.append(mossa)
			
		result.append(risolvi(players,moves))

	scrivi(result)