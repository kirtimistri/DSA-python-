# Remove duplicates from an array (without Set).
numbers=[1,2,1,3,3,4,5,5]
def removeduplicates():
    # for num in numbers :
    #     print(num)
    unique=[]
    for num in numbers:
        if num not in unique:
            unique.append(num)
    print(unique)

removeduplicates()       