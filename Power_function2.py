#python code to demonstrate the above approach
def power(x, y):
	if y==0:
		return 1

	temp = power(x, y // 2)
	# if y is even
	if y % 2 == 0:
		return temp * temp
	else:
		return x * temp * temp

x = 3
y = 5
print("Power is : ", power(x,y))