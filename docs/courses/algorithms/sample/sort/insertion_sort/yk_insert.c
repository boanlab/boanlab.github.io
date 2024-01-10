#include<stdio.h>


void InsertionSort(int *arr, int arrSize){
    int i,j;
    int key;

    for(i=1; i<arrSize;i++){
        key = arr[i];
        j = i-1;
        while(j>=0 & arr[j] > key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int main(void){

    int arr[5] = {9,5,3,7,1};
    int i;

    InsertionSort(arr,5);

    for(i=0; i<5; i++){
        printf("arr[%d] : %d\n", i,arr[i]);
    }
}
