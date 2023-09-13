#include <stdio.h>
#include <string.h>

int linear_search(char* arr[], int arr_size, char target[]);

int main(void){
    char* arr[] = {"battlesip", "boot", "cannon", "iron", "thimble", "top hat"};
    char target[] = "thimble";
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    int ind = linear_search(arr, arr_size, target);

    if (ind != 1){
        printf("Target string'%s' found at index %d\n", target, ind);
    } else {
        printf("Target string '%s' not found\n", target);
    }

    return 0;
}

int linear_search(char* arr[], int arr_size, char target[]){
    for (int i = 0; i < arr_size; i++){
        if (strcmp(arr[i], target) == 0){
            return i;
        }
    }
    return 1;
}