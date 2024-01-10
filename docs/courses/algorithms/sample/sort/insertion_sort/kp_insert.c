# include <stdio.h>

void insertion_sort (int list[], int n) {

  int i, j, key;
  
    // j 값은 key의 앞부터 시작하여 내려감
    // j 값은 양수
    // key 값보다 정렬된 배열에 있는 값이 크면 j번째를 j+1번째로 이동

  for ( i = 1; i < n; i++) {
  
    key = list[i]; // 현재 삽입될 숫자인 i번째 정수를 key 변수로 복사

    for ( j= i-1; j>=0 && list[j] > key; j--) {
    
      list[j+1] = list[j]; // 레코드의 오른쪽으로 이동
      
    }

    list[j+1] = key;
    
  }
}

void main(){

  int i;
  int list[5] = {8, 5, 6, 2, 4};

  // 삽입 정렬 수행
  insertion_sort(list, 5);

  // 정렬 결과 출력
  for (i=0; i<5; i++) {

    printf("%d ", list[i]);

  }
}