'''
Created on Nov 22, 2015

@author: ahanagrawal
'''


def toh(reserves, left, right, total, abs_total):
    if total == 0:
        return
    print("Move from ", reserves, " to ", left)
    
    
    toh(right, reserves, left, abs_total - total, abs_total - total)
    toh(reserves, right, left, total - 1, abs_total)
    


if __name__ == "__main__":
    toh(1,2,3,3,3)