def bubble_sort(L):
    '''
    Bubble Sort Algorithm 
    Complexity: O(n**2)
    '''
    # while loop implementation
    swap = False
    while not swap: # O(n)
        swap = True
        print(L)
        for i in range(1, len(L)): # O(n)
            if L[i-1] > L[i]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]

    # # for loop implementation 2
    # n = len(L)
    # for i in range(n):
    #     swap = False
    #     for j in range(0, n-i-1):
    #         if L[j] > L[j+1]:
    #             L[j], L[j+1] = L[j+1], L[j]
    #             swap = True
    #     if not swap:
    #         break

    # for loop implementation 3
    # for pass_num in range(len(L), 0, -1):
    #     for i in range(1, pass_num):
    #         if L[i-1] > L[i]:
    #             L[i-1], L[i] = L[i], L[i-1]
    
if __name__=="__main__":
    testlist = [75,16,83,17,17,77,31,0,44,55,20]
    bubble_sort(testlist)
    print(testlist)
