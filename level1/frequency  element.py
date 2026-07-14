# frequency of every element
# array=[1,2,2,3,7,7,4,4,4]
# visited = []
# def freq():  
#     i=0
#     j=len(array)-1
#     for i in array:
#         if i in visited :
#             continue
#         count=0
            
#         for j in array:
#             if (i==j):
#                 count=count+1
#                 print(i,"->",j)
# freq()

array=[1,2,2,3,7,7,4,4,4]

freq = {}

for arr in array:
    if arr in freq:
        freq[arr] += 1
    else:
        freq[arr] = 1

print(freq)