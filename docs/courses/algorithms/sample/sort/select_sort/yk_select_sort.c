#include <stdio.h>

void select_sort(int* nums, int numsSize){

    int i,j;
    int min;
    int temp;
    
    for(i=0; i<numsSize-1; i++){
        min = i;
        for(j=i+1; j<numsSize; j++){
            if(nums[j]<nums[min])
                min = j;
        }
        temp = nums[i];
        nums[i] = nums[min];
        nums[min] = temp;
    }

}

int main(void){

    int nums[5] = {2,1,0,3,1};

    select_sort(nums,5);

    for (int i=0; i<5; i++){
        printf("nums[%d] : %d\n", i,nums[i]);
    }

}
