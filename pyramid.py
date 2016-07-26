height = int(input("height: "))
for i in range(height):
	for n in range(height-i):
		print(" ", end='')
	for j in range((2*i)-1):
		print("#", end='')
	print()
input()