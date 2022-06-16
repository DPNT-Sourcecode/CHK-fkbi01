
import collections
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    total = 0
    dic = collections.defaultdict(int)
    for char in skus:
        dic[char] += 1
        
    # print(char)
    # print(dic)
    for char in sorted(dic, key=dic.get, reverse=True):
        # print(char)
        # if dic.contain('A', 'B', 'C', 'D'):
        if char == 'A':
            if dic[char] == 3:
                total = total + 130
                # print(total)
            else:
                total = total + (50*dic[char])
                # print(total)
        if char == 'B':
            if dic[char] == 2:
                total = total + 45
                # print(total)
            else:
                total = total + (30*dic[char])
                # print(total)
        if char == 'C':
            total = total + (20*dic[char])

        if char == 'D':
            total = total + (15*dic[char])

        if char == '':
            total = total + 0

        if not char.isalpha() or (char not in "ABCD"):
            return -1


    return total
    
    
    
    

    
