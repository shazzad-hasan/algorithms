def binary_search(L, e):
    """ Binary search on a sorted list """
    # first = 0
    # last = len(L) - 1
    # found = False

    # while first <= last and not found:
    #     mid = (first + last) // 2
    #     if L[mid] == e:
    #         found = True
    #     else:
    #         if L[mid] > e:
    #             last = mid -1
    #         else:
    #             first = mid + 1
    # return found

    # Recursive implementation
    if L == []:
        return False 
    elif len(L) == 1:
        return L[0] == e
    else:
        mid = len(L) // 2
        if L[mid] > e:
            return binary_search(L[:mid], e)
        else:
            return binary_search(L[mid:], e)



testlist = [0, 2, 6, 8, 15, 17, 23, 30, 32, 42]
print(binary_search(testlist, 15))
print(binary_search(testlist, 25))