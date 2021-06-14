import random

r = random.randint(1, 100)
# print(r)
count = 0

while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)

	if(num == r):
		print('你第', count ,'次就猜中了!!\n')
		break
	elif num >r :
		print('比答案大\n')
	elif num<r:
		print('比答案小\n')

	print('你猜了 ', count ,' 次\n')

