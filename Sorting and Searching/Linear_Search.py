def linear_search(L, e):
    """ Linear search on unsorted list """
    # # using for loop
    # found = False
    # for i in range(len(L)):
    #     if L[i] == e:
    #         found = True 
    # return found

    # using while loop
    ind = 0
    found = False 
    while ind < len(L) and not found:
        if L[ind] == e:
            found = True
        else:
            ind += 1 
    return found 

# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(linear_search(testlist, 17))
# print(linear_search(testlist, 1000))



def Ordered_Linear_Search(L, e):
    """ Linear search on sorted list """
    # # using for loop
    # for i in range(len(L)):
    #     if L[i] == e:
    #         return True 
    #     if L[i] > e:
    #         return False 
    # return False 

    # using while loop
    ind = 0
    found = False 
    stop = False 
    while ind < len(L) and not found and not stop:
        if L[ind] == e:
            found = True 
        else:
            if L[ind] > e:
                stop = True 
            else:
                ind += 1 
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(Ordered_Linear_Search(testlist, 17))
print(Ordered_Linear_Search(testlist, 20))