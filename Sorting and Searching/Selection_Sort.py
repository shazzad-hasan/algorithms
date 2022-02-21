def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
                
        suffixSt += 1
        
testlist = [54,26,93,17,77,31,44,55,20]
selection_sort(testlist)
print(testlist)