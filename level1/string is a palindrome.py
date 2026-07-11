# Check if a string is a palindrome.
string="madam"
def palindroe():
    i =0
    j=len(string)-1
    while (i<j):
       if (string[i]==string[j]):
           i=i+1
           j=j-1
           print("pallindrome")
       elif(string[i]!=string[j]):
        print("not pallindrome")
        return
palindroe()