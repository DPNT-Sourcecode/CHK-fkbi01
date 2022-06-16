

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    offer = False
    # data_upper = [name.upper() for name in user_list]
    if skus.isalpha() and skus == 'A':
        if offer == True:
            return 130
        # print(50)
        return 50
    elif skus.isalpha() and skus == 'B':
        if offer == True:
            return 45
        # print(30)
        return 30
    
    elif skus.isalpha() and skus == 'C':
        # print(20)
        return 20
    
    elif skus == "":
        return 0
    
    elif skus.isalpha() and skus== 'D':
        return 15
    
    else:
        return -1
    
    
    
    

    



