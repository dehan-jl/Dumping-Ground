k = int(input())
print(" "*k + "#")
for i in range(1, k): print(" "*(k-i) + "#" + " "*((2*i-1)) + "#")
for i in range(2, k): print(" "*(i) + "#" + " "*((2*k-1)-(2*i)) + "#")
print(" "*k + "#")
input()