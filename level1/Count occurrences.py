# Count occurrences of each character.
word="apple"
phrese=list(word)
count=0
def countoccurrence():
    i=0 
    j=len(phrese)-1
    for ch in word :
        count=0
        for c in word:
            if (ch==c):
                count=count+1
                # print(ch,count)
        print(ch,count)
countoccurrence()