# Check whether two strings are anagrams.
def anagram():
    str1="apple"
    str2="leppa"
    if(len(str1)!=len(str2)):
        print("strings cannot be anagrams because the lengths are not equal !")
    elif(sorted(str1)==sorted(str2)):
        print("strings are anagrams")
    else:
        print(" yhem legth of strings is equal but they are not anagrams ")
        return
anagram()