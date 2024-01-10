# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# define n 10

void FindMinMax (int arr[]) {

    int small, large, min, max;
    min = arr[0];
    max = arr[0];

    for( int i = 0; i < n; i++ ) {

        if ( max < arr[i])
        max = arr[i];

        if ( min > arr[i])
        min = arr[i];
        
    }

    printf("MIN : %d, MAX : %d", min, max);

}

int main() {

    srand(time(NULL));

    int arr[n];
    for( int i = 0; i < n; i++ ) {

        arr[i] = (rand() % 100); // 0~99
        printf("%d", arr[i]);

    }

    FindMinMax(arr);

}