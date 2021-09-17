from itertools import permutations
print('How many symbols do you want to enter?')
num = int(input())
print('Enter the', num, 'symbols')
l = []
inpnum = 0
for i in range(num): 
    j = input()
    l.append(j)

perm = permutations(l)
for i in list(perm):
    print (i)