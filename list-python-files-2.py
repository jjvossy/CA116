import os
files = os.listdir(".")
i = 0
while i < len(files):
	with open(files[i]) as n:
		n = n.read()
	if files[i].split('.')[-1] == 'py' and 0 < len(n):
			print files[i]
	i += 1
