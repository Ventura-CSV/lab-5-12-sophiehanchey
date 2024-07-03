import random


def split(numbers):
    #initializing variables and pivot point
    lessThan = []
    greaterThan = []
    pivot = numbers[0]
    del numbers[0]
    
    #loop through remainder of list
    while numbers:
        #sort values into respective lists
        if numbers[0] <= pivot:
            lessThan.append(numbers[0])
        else:
            greaterThan.append(numbers[0])
        del numbers[0]
    
    #update numbers
    numbers.extend(lessThan)
    numbers.append(pivot)
    numbers.extend(greaterThan)

    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
