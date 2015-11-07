'''
Created on Oct 16, 2015

@author: ahanagrawal
'''

if __name__ == '__main__':
    def reverse(s):
        toReturn = ""
        for i in range(len(s)-1,-1,-1):
            toReturn += s[i]
        return toReturn
    
list = ["hello", "new", "was"]
print(map(reverse,list));