import math

num = 600851475143
i = 2;
while num > 1:
	while num % i == 0:
		num /= i;
	i+=1

	if i*i > num and num > 1:
		print num
		break;
