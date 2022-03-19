def peak_element(L):
    """ Find Peak Element """
    first = 0
    last = len(L)-1
    while first < last:
        mid = (first + last) // 2
        if L[mid-1] < L[mid] and L[mid] > L[mid+1]:
            return L[mid]
        elif L[mid] < L[mid+1]:
            first = mid + 1
        else:
            last = mid - 1
    return L[first]
    
    # # recursive version
    # first = 0
    # last = len(L)-1
    # while first <= last:
    #     mid = first + (last - first) // 2
    #     if L[mid-1] > L[mid]:
    #         return peak_element(L[:mid])
    #     elif L[mid] < L[mid+1]:
    #         return peak_element(L[mid+1:])
    #     else:
    #         return L[mid]
        
test1 = [1,2,1,3,5,6,4]
print(peak_element(test1))  
nums2 = [1,2,3,1]
print(peak_element(nums2))