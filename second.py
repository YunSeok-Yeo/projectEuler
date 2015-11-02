list = [1, 2];
i = 2;
while True:
	if list[i-1] + list[i-2] > 4000000:
		break;
	list.append(list[i-1] + list[i-2]);
	i=i+1;
total = 0;
for i in range(1, i):
	if(list[i] % 2 == 0):
		total = total + list[i];
print total
