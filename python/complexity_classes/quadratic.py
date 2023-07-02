def square(n):
    """
    Takes in a positive integer integer, n and return  n^2
    
    Complexity: O(n^2)

    """
    result = 0
    for i in range(n):
        for j in range(n):
            result += 1
    return result


def isSubset(L1, L2):
    """
    Inputs: Two lists, L1 & L2
    Output: return True if L1 is a subset of L2, else return False
    
    Complexity: O(n^2), where n = len(L1) = Len(L2) 
        

    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
    