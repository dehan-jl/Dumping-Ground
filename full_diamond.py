k = int(input())
for i in range(k+1):
	print(" "*(k-i) + "#"*(2*i-1))
for i in range(1, k+1):
	print(" "*(i) + "#"*((2*k-1)-(2*i)))
input()