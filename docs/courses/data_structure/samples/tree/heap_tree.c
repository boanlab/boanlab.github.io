#include <stdio.h>
#include <math.h>
#include <stdlib.h>



/*--------구조체 선언--------*/

typedef struct NODE{
    int data;
} Node;

typedef struct HEAP{
    Node heap[100];
    int size;
} Heap;

/*------------------------*/



/*----------함수 선언--------*/

void Input_Data(Heap *hp, int data);
void Delete_Data(Heap *hp);
void Print_Heap(Heap *hp);

/*------------------------*/



int main(int argc, const char * argv[]) {
    Heap hp;
    
    Input_Data(&hp, 31);
    Input_Data(&hp, 8);
    Input_Data(&hp, 30);
    Input_Data(&hp, 14);
    Input_Data(&hp, 24);
    Input_Data(&hp, 2);
    Input_Data(&hp, 5);
    Input_Data(&hp, 3);

    Print_Heap(&hp);

    Delete_Data(&hp);

    Print_Heap(&hp);

    Delete_Data(&hp);

    Print_Heap(&hp);

    Delete_Data(&hp);

    Print_Heap(&hp);
    return 0;
}



void Input_Data(Heap *hp, int data){
    int i = 0;
    int tmp;

    hp->size++;
    i = hp->size;
    hp->heap[i].data = data;
    puts("\nInputing data starts.");

    while(i > 1){
        if(hp->heap[i/2].data < hp->heap[i].data){
            tmp = hp->heap[i].data;
            hp->heap[i].data = hp->heap[i/2].data;
            hp->heap[i/2].data = tmp;
            i = i/2;
        }
        else{
            break;
        }
    }
    printf("hp->heap[%d].data = %d.\n", i, hp->heap[i].data);
    puts("Inputing data is complete.");
}



void Delete_Data(Heap *hp){
    int tmp;
    int i = 1;
    int j = 0;
    
    hp->heap[i].data = hp->heap[hp->size--].data;

    while(i <= hp->size){
        j = 2*i;
        if(j > hp->size){
            break;
        }

        if(hp->heap[i].data >= hp->heap[j].data && hp->heap[i].data >= hp->heap[j+1].data){
            break;
        }

        if(hp->heap[j].data < hp->heap[j+1].data){
            j = j+1;
        }

        tmp = hp->heap[j].data;

        hp->heap[j].data = hp->heap[i].data;

        hp->heap[i].data = tmp;

        i = j;
    }
}

void Print_Heap(Heap *hp){
    int i = 1;
    int k = 1;
    puts("\nPrinting starts.");
    while (i <= hp->size){
        for(int j = 1; j <= pow(2, k-1); j++){
            if(i > hp->size){
                break;
            }
            printf("%2d  ", hp->heap[i].data);
            i++;
        }
        printf("\n");
        k++;
    }
    puts("Printing is complete.");
}