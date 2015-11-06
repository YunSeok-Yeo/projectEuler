

b = 0;


for b in range(1, 500):
	a = 1000 * (float)(2 * b - 1000) / (2 * b - 2000)
	if(int(a) < a):
		continue
	else:
		a = int(a);
		break;


c = 1000 - a - b;

print a * b * c
