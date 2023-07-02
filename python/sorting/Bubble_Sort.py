def bubble_sort(L):
    # # while loop implementation
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]

    # for loop implementation
    # for pass_num in range(len(L), 0, -1):
    #     for i in range(1, pass_num):
    #         if L[i-1] > L[i]:
    #             L[i-1], L[i] = L[i], L[i-1]
    
if __name__=="__main__":

    testlist = [75,16,83,17,17,77,31,0,44,55,20]
    bubble_sort(testlist)
    print(testlist)
