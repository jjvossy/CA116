n = raw_input()
a = []
while n != 'end':
	a.append(int(n))
	n = raw_input()  

i = 0
n = input()
a.append(n)
while i < len(a):
	v = a[i]
	p = i
	while 0 < p and v < a[p - 1]:
		a[p] = a[p - 1]
		p = p - 1
	a[p] = v
	i = i + 1
print p
