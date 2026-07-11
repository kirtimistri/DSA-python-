# Find the missing number in an array.
array=[1,3,4,5,6,8]
def missnum():
    for num in range (1,9) :   
        if num not in array :    
            print (num)
missnum()           