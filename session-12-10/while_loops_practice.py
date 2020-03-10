
# 1. Use a while loop to print numbers 1-10:
b = 0
while b<11:
	print(b)
	b+=1
# 2. Use a while loop to print the first 10 multiples of 24:
a = 0
while a<241:
	print(a)
	a+=24
# 3. Use a while loop to find the average of these numbers:
numbers = [10,42,-2, 900,5,8,39]
<<<<<<< HEAD
print(len(numbers))
c = 0
for i in numbers:
	c+=i
	print(c)
print(c/7)

i= 0
total = 0
while i < len(numbers):
	total+= numbers[i]
	i+= 1
print(total)
print(total/len(numbers))

=======
print(numbers[1])
i = 0
total = 0

while i < len(numbers):
	total += numbers[i]
	i+=1

print(total)
average = total/len(numbers)

print(average)
>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
