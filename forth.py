max = 0;
for i in range(100, 999):
	for j in range(i, 999):
		num = str(i*j);
		check = True;
		for l in range(0, len(num) / 2):
			if num[l] != num[len(num) - l - 1]:
				check = False
				break;
		if check:
			if i*j > max:
				max = i*j;

print max
