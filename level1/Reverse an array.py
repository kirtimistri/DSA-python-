# Reverse an array (without reverse()).
numbers=[1,2,3,4,5,6]
def reversearray():   
        rev=[]
        i=len(numbers)-1
        while(i >= 0):
            rev.append(numbers[i])
            i=i-1
        print(rev)

reversearray()
