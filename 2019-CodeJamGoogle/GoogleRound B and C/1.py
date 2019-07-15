import sys 
import statistics
import math

def scrivi(result):
	for i in range(0, len(result)):
		print("Case #{}: {} {}".format(i+1, result[i][0],result[i][1] ))


def dist_min(punto,retta):

	minx = 999999999999999999999999999999
	miny = 999999999999999999999999999999
	for p in retta:
		x = punto[0] - p[0]
		if(x<0):
			x = x*(-1)

		if(x<minx):
			minx = x

		y = punto[1] - p[1]
		if(y<0):
			y = y*(-1)

		if(y<miny):
			miny = y

	return minx + miny

def risolvi(P,Q,people):

	passi = []

	for t in range(0,len(people)):
		l = []
		n = 0
		conta = [0,0,0,0]

		if(people[t][2] == 'W'):
			conta[0] += 1
			for h in range(0,int(people[t][0])):
				l.append((h,int(people[t][1])))

		elif(people[t][2] == 'S'):
			conta[1] += 1
			for h in range(int(people[t][1]) , Q):
				l.append((int(people[t][0]),int(people[t][1])+n))
				n += 1

		elif(people[t][2] == 'E'):
			conta[2] += 1
			for h in range(int(people[t][0]) , Q):
				l.append((int(people[t][0])+n,int(people[t][1])))
				n += 1

		else:
			conta[3] += 1
			for h in range(0,int ( int(people[t][1]) )):
				l.append((int(people[t][0]),h))
				n += 1

		passi.append(l)



	if(P == 1):
		if(people[t][2] == 'W'):
			return (0,int (people[t][1])-1)

		elif(people[t][2] == 'S'):
			return (int (people[t][0])+1 , Q-1)

		elif(people[t][2] == 'E'):
			return (Q-1,int (people[t][1])-1)

		else:
			return (int (people[t][0])+1, 0)

	
	mindist = 99999999999999999999999999999999999999999
	puntopreciso = (0,0)
	for q1 in range(0,Q):
		for q2 in range(0,Q):
			punto = (q1,q2)
			dist = 0
			for d in passi:
				dist += dist_min(punto,d)

			if(mindist > dist):
				mindist = dist
				puntopreciso = punto

	if (conta[2] == 1 and conta[0] ==0):
		return (Q-1,puntopreciso[1]) 
	elif (conta[1] == 1 and conta[3] ==0):
		return (puntopreciso[0], Q-1) 
	elif (conta[0] == 1 and conta[2] ==0):
		return (0,puntopreciso[1])
	elif (conta[3] == 1 and conta[1] ==0):
		return (puntopreciso[0],0)

	return puntopreciso
	

if __name__ == '__main__':
	result = []
	N = int(input())
	for i in range(0,N):
		s = input()
		P,Q = s.split(" ")
		P = int(P)
		Q = int(Q)
		people = []

		for j in range(0,P):
			s = input()
			tupla = s.split(" ")
			people.append(tupla)

		result.append(risolvi(P,Q,people))

	scrivi(result)