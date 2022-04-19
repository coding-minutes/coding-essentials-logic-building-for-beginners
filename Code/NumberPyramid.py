
N = int(input())
i = 1
while i<=N:
	#spaces
	spaces = 1
	while spaces<=N-i:
		print(" ",end="")
		spaces = spaces + 1

	#inc nos
	val = i
	cnt = 1
	while cnt <= i:
		print(val,end="")
		val = val + 1
		cnt = cnt + 1

	#dec nos
	# reset the val 
	val = val - 2
	cnt = 1
	while cnt<=i-1:
		print(val,end="")
		val = val - 1
		cnt = cnt + 1

	print()
	i = i + 1









