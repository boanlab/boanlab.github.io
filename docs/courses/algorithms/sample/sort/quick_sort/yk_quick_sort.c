#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y){

    int tmp = *x;
    *x = *y;
    *y = tmp;
    
}

void quick (int a[], int left, int right){  // 오름차순 정렬

    int pl = left;
    int pr = right;
    int x = a[(pl+pr)/2]; // 피봇은 가운데 요소로 선택

    do {
        while(a[pl] < x)
            pl++;       // pl이 피봇보다 작으면 pl+1을 pl로 설정
        
        while(a[pr] > x)
            pr--;       // pr이 피봇보다 크면 pr-1을 pr로 설정

        if(pl <= pr){
            swap(&a[pl],&a[pr]);
            pl++;
            pr--;
        }

    } while(pl <= pr);
    

    // 재귀 호출 부분 (피봇을 기준으로 앞 리스트와 뒷 리스트를 다시 퀵정렬을 수행해야 함)
    if(left < pr)       // pr과 left가 같아질 때 까지 계속 퀵정렬 반복
        quick(a,left,pr);

    if(pl < right)      // pl과 right가 같아질 때 까지 계속 퀵정렬 반복
        quick(a, pl, right);   
}

int main(void){

    int i,nx;
    int *arr; // 동적 리스트 할당을 위한 포인터 선언

    puts("퀵 정렬");
    printf(" 요소 개수 : ");
    scanf("%d", &nx);

    arr = calloc(nx, sizeof(int)); // calloc 은 모든 할당 값들을 0으로 초기화 해준다.

    for(i=0; i<nx; i++){
        printf("arr[%d] : ",i);
        scanf("%d",&arr[i]);
    }

    quick(arr,0,nx-1);
    puts("오름차순으로 정렬");

    for(i=0; i<nx; i++)
        printf("arr[%d] = %d\n", i, arr[i]);
    free(arr);

    return 0;

}
