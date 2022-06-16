
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
            mod3 = dic[char] // 3
            if dic[char] % 3 == 0:
                total = total + ((mod3)*130)
                # print(total)
            elif dic[char] > 3:
                total = total + (130*mod3) + (50*(dic[char]-mod3*3))
                # print(total)
            else:
                total = total + (50*dic[char])
                print(total)
        if char == 'B':
            mod = dic[char] // 2
            if dic[char] % 2 == 0:
                total = total + (mod*45)
            elif dic[char] > 2:
                total = total + (45*mod) + (30*(dic[char]-(mod*2)))
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

    
