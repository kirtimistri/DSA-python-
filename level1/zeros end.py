# Move all zeros to the end.
array=[1,2,0,3,6,0,5,6,0,9]
def  endzero():
      i=0
      for a in array:
            if(a!=0):
             array[i]=a             
             i=i+1
            #  print(array)
             
      while(i<len(array)):
        array[i]=0
        i=i+1
        print(array)
              
            
endzero()               