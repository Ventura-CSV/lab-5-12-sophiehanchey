import random

def split(numbers):
	#################
	# Make your code 
	#################
	return numbers


numbers = [3,2,0,5,4]
# print (id(numbers))
numbers = split(numbers)
# print (id(numbers))
print (numbers)


numbers = [ random.randint(0,20) for i in range(10)]
print (numbers)
numbers = split(numbers)
print (numbers)
