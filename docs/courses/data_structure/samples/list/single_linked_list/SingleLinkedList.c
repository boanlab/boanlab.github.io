#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
}node;

void insert_node(node* head, const int index, const int data) {
    int k = index;
    node* preNode = head;
    node* newNode = (node*)malloc(sizeof(node));
    newNode -> data = data;

    while (k-- && preNode != NULL)
        preNode = preNode->next;

    if (preNode == NULL) {
        free(newNode);
        return;
    }

    newNode -> next = preNode -> next;
    preNode -> next = newNode;
}

void delete_node(node* head, const int index) {
    int k = index;
    node* temp = head;
    node* garbage = NULL;

    while (k-- && temp != NULL) 
        temp = temp -> next;
    
    if (temp == NULL || temp -> next == NULL)
        return;
    
    garbage = temp -> next;
    temp -> next = garbage -> next;
    free(garbage);
}

int search(node* head, const int val) {
    if (head -> next == NULL) return -1;

    int index = 0;
    node* temp = head -> next;

    while (temp -> data != val) {
        ++index;
        temp = temp -> next;

        if (temp == NULL) return -1;
    }

    return index;
}

int get_data(node* head, const int index) {
    if (head -> next == NULL) return -1;

    int k = index;
    node*  temp = head -> next;

    while (k--) temp = temp -> next;
    return temp -> data;
}

int size(node* head) {
    node* temp = head -> next;
    int len = 0;

    while (temp != NULL) {
        ++len;
        temp = temp -> next;
    }

    return len;
}

void print_all(node* head) {
    if (head -> next == NULL) return;

    node* temp = head -> next;
    while (temp != NULL) {
        printf("%d ", temp -> data);
        temp = temp -> next;
    }
    printf("\n");
}

int main(void) {
    node* head = (node* )malloc(sizeof(node));
    head->data = 0;
    head->next = NULL;

    insert_node(head, 0, 123);
    print_all(head); // expect output: 123

    insert_node(head, 1, 10);
    print_all(head); // expect output: 123 10

    insert_node(head, 2, 20);
    print_all(head); // expect output: 123 10 20

    insert_node(head, 1, 11);
    print_all(head); // expect output: 123 11 10 20
    
    insert_node(head, 5, 19); // 길이를 넘어서는 인덱스를 전달해본다.
    print_all(head); // expect output: 123 11 10 20

    printf("%d\n", search(head, 20)); // expect output: 3
    printf("%d\n", search(head, 11)); // expect output: 1
    printf("%d\n", size(head)); // expect output: 4
    printf("%d\n", get_data(head, 3)); // expect output: 20

    delete_node(head, 0);
    print_all(head); // expect output: 11 10 20
    
    delete_node(head, 4); // 길이를 넘어서는 인덱스를 전달해본다.
    print_all(head); // expext output: 11 10 20
}