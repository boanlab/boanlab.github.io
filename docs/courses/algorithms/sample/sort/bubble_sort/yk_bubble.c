#include <stdio.h>
#include <string.h>


int bubble_sort(int* arr, int arrSize){

    int i,j;
    int  count = 0;
    int tmp;
    int sorted[arrSize];
    memmove(sorted,arr,sizeof(int)*arrSize);

    for(i=0; i<arrSize-1; i++){
        for(j=0; j<arrSize-1; j++){
            if(sorted[j]>sorted[j+1]){
                tmp = sorted[j];
                sorted[j] = sorted[j+1];
                sorted[j+1] = tmp;
            }
        }
    }
}

int main(void){

    int arr[20] = {7,3,5,5,1,2,2,3,9,2,2,7,1,7,3,2,3,6,6,7};

    bubble_sort(arr,20);
}
