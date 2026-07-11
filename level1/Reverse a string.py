# Reverse a string (without reverse()).
string="keep"
def reversestring():
    rev=""
    i= len(string)-1
    while(i>=0):
        rev=rev + string[i]
        i=i-1
    print(rev)
# reversestring() 
 
def twopinters():
    chars=list(string)
    rev=""
    i=0 
    j=len(string)-1
    print(len(string))
    while (i <= j ):
        chars[i],chars[j]=chars[j],chars[i]
        i=i+1
        j=j-1
        print(chars)
twopinters()