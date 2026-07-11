# Find the smallest number.
numbers=[1,2,3,4,5,6]
small=float("inf")
secondsmall=numbers[0]
for num in numbers:
    if (num<secondsmall):
        
        secondsmall=num 
    elif num<small and num != small:
        small=num 
print(small)   