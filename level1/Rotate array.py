# Rotate an array by k positions
def rotate_array(arr, k):
     n=len(arr)
     rotate=[]
     k=k%n
     if k==0:
          for i in range(n):
               rotate.append(arr[i])
     else:
          for i in range(k, n):
               rotate.append(arr[i])
          for i in range(k):
               rotate.append(arr[i])
     print(rotate)          
     return rotate

rotate_array([1, 2, 3, 4, 5], 2)