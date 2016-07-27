k = int(input())
for i in range(k+1):
	for n in range(k-i): print(" ", end='')
	for j in range((2*i)-1): print("#", end='')
	print()
input()