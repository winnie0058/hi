import random

start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
# print(r)

count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)

	if(num == r):
		print('你第' , count , '次就猜中了!!\n')
		break
	elif num >r :
		print('比答案大\n')
	elif num<r:
		print('比答案小\n')

	print('你猜了' , count , '次\n')

