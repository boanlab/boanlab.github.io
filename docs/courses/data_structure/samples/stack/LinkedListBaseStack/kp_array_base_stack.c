# include <stdio.h>
# define MAX 100

typedef struct Stack {

    int stack[MAX]; //스택의 value
    int top; //스택의 index

}Stack;

//스택 초기화
void Init (Stack* p) {

    p -> top = 0;
}

//스택이 비었는지 확인
int IsEmpty (Stack* p) {

    if (p -> top == 0) return 1;
    else return 0;

}

//스택 꽉 차있는지 확인
int IsFull (Stack* p) {

    if (p -> top == MAX-1) return 1;
    else return 0;

}

//value를 스택에 추가
void Push (Stack* p, int value) {

    if (IsFull(p)) printf("스택에 더 이상 공간이 없어요..");

    else {

        p -> top += 1;
        p -> stack[p -> top] = value;

    }
}

//제일 위에 있는 value 제거
void Pop (Stack* p) {

    int e;
    if (IsEmpty(p)) printf("현재 스택이 비어있습니다.");
        
    else {

        e = p -> stack[p -> top];
        p -> top -= 1;
        printf("방금 |%d|가 Pop 되었습니다.\n",e);
    }

}

//스택 제일 위에 있는 value 반환
int Peek (Stack* p) {

    if (IsEmpty(p)) printf("현재 스택이 비어있습니다.");
    else return p -> stack[p -> top];

}

void Print (Stack* p) {

    printf("현재 Stack 상황");

    for (int i=1; i <= p -> top; i++) {

        printf("|%d| ", p -> stack[i]);

    }

    printf("\n");
}

int main() {

    Stack stack;
    Init(&stack);

    //스택에 1~10까지 넣기
    for(int i=1; i <= 10; i++) {

        Push(&stack, i);

    }
    Print(&stack);

    printf("%d가 top에 있어요.\n",Peek(&stack));
    Pop(&stack);
    Pop(&stack);

    Print(&stack);

    
}