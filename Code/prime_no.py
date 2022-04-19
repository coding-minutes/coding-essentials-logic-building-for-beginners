# Prime Number

def checkPrime():
	N = int(input())
	i = 2
	while i<N:
		if N%i==0:
			print("Not Prime")
			return
		i = i+1

	print("Prime")
	return

checkPrime()	
