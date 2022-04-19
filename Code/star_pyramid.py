
N = int(input())
i = 1
while i<=N:

	spaces = 1
	while spaces<=N-i:
		print(" ",end="")
		spaces=spaces + 1

	stars = 1
	while stars<=2*i - 1:
		print("*",end="")
		stars = stars + 1
	print()
	i = i+1


