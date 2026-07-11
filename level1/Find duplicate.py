# Find duplicate elements.
array=[2,2,4,5,6,7,4,0,7]
seen=set()
duplicate=set()
def findduplicate():
    for a in array:
        if a in seen:
            duplicate.add(a)
        else:
            seen.add(a)
    print(duplicate)
findduplicate()