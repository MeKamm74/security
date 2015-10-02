import re
import sys

def gcdAndLinearCombo(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy

if len(sys.argv) > 1:
	f = open(sys.argv[1], 'r')
else:	
	f = open("default.cfg", 'r')

if len(sys.argv) > 2:
	log = open(sys.argv[2], 'w')
else:
	log = open("default.log", 'w')

a = int(f.readline())
b = int(f.readline())

gcd, x, y = gcdAndLinearCombo(a, b)

log.write("The gcd is: " + str(gcd) +"\n\n")
s = "The linear combination for (" + str(a) + ", " + str(b) + ") is: " + str(gcd) + " = " + str(a) + "*" + str(x) + " + " + str(b) + "*" + str(y)

log.write(s)