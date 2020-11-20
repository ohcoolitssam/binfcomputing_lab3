#!/usr/bin/env python

file = open("dna.txt")
fh = file.read()
readtext = fh.rstrip("\n")
file.close()

x = open("output.txt", 'w')
x.write(readtext)	
x.close()

with open ("output.txt",'r') as f:
	q = f.read()
	z = q.rstrip("\n")
	a = readtext[:-1]

print("\n" + z.lower() + "\n")
print("pwd" + "\n")
print(len(z))
print("\n") 
print(float(4/3.25))
print("\n")

	




