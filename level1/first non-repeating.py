# Find the first non-repeating character.
def first_non_repeating_char():
    arr1=[2,2,3,3,8,4,4,5]
    arr2=[]
    
    for i in arr1:
        if arr1.count(i)==1:
            arr2.append(i)
    print(arr2[0])
first_non_repeating_char()