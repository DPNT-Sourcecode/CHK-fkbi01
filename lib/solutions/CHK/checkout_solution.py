

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    import collections
    total = 0
    dic = collections.defaultdict(int)
    for char in skus:
        dic[char] += 1
        
    for char in sorted(dic, key=dic.get, reverse=True):
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
            
        if not char.isalpha():
            return -1

    return total
    
    
    
    

    
