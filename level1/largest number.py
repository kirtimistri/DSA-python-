# Find the largest number.
numbers=[1,2,7,3,4,5,6]
def largest():
    largest=numbers[0]
    for num in numbers:
        if num > largest:
            largest=num 
    print(largest)
largest()