# Find the second largest number.
numbers=[1,2,3,4,5]
def secondlarge():
    large=numbers[1]
    secondlarge=float("-inf")
    for num in numbers:               
        if(num>large):    
         secondlarge=large
         large=num     
        elif num>secondlarge and large != num:
          secondlarge=num  
    print(secondlarge)   
secondlarge()              
    