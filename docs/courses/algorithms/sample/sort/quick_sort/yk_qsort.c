
// quick sort를 c언어 qsort를 이용한 코드 입니다.


#include <stdio.h>
#include <stdlib.h>         //  qsort를 사용하기 위한

// 오름차순으로 정렬하는 비교 함수
int static int_cmp (const int *a, const int *b){ 

    if(*a < *b)
        return -1;
    else if(*a > *b)
        return 1;
    else
        return 0;
}


int main(void){
    
    int i, nx;
    int *arr;
    puts("qsort를 이용한 quick sort ");
    printf("요소 개수 : ");
    scanf("%d", &nx);

    arr = calloc(nx, sizeof(int));
    for(i=0; i<nx; i++){
        printf("arr[%d] : ", i);
        scanf("%d", &arr[i]);
    }

    qsort(arr,nx,sizeof(int), (int(*)(const void *, const void *))int_cmp); //qsort 사용

    puts("오름차순으로 정렬 완료");
    for(i=0; i<nx; i++)
        printf("arr[%d] = %d\n", i, arr[i]);
    free(arr);

    return 0;
}
