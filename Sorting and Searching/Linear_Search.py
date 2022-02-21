def linear_search(L, e):
    """ Linear Search on unsorted List """
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

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linear_search(testlist, 17))
print(linear_search(testlist, 1000))