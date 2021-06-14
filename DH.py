from random import randint

def DH(a,b):
	P = 23
	G = 9
	x = int(pow(G,a,P))
	y = int(pow(G,b,P))
	ka = int(pow(y,a,P))
	kb = int(pow(x,b,P))
	return(str(ka),str(kb))

if __name__ == '__main__':
	keys = DH(3,4)
	print(keys)
