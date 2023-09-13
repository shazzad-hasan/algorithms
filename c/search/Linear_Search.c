#include <stdio.h>

int linear_search(int arr[], int arr_size, int target);

int main(void){
    int arr[] = {1, 2, 32, 8, 17, 19, 42, 13, 0};

    int arr_size = sizeof(arr) / sizeof(arr[0]);
    int target = 42;
    int ind = linear_search(arr, arr_size, target);

    if (ind != 1){
        printf("Target element %d found at index %d\n", target, ind);
    } else {
        printf("Target element %d not found\n", target);
    }

    return 0;
}

int linear_search(int arr[], int arr_size, int target){
    for (int i = 0; i < arr_size; i++){
        if (arr[i] == target){
            return i;
        }
    }
    return 1;
}