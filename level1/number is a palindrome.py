# Check if a number is a palindrome.
def numpalindrome():
    number=10014
    degit=str(number)
    i=0
    j=len(degit)-1
    while(i<j):
        if (degit[i]==degit[j]):
            i=i+1
            j=j-1
            print("number is palindrome")
        elif(degit[i]!=degit[j]):
            print("number is not palindrome")
            return
# numpalindrome()

def math():
    reverse=0
    number=12216
    original=number
    while(number>0):
        degit=number%10
        reverse=reverse*10+degit
        number=number//10
    if (original==reverse):
        print("number is palindrome")
    else:
        print("it is not a palindrome")
        return

math()
