


#include <stdio.h>
#include <stdlib.h>

typedef struct node{        // 자기 참조 구조체(다른 구조체(노드)를 연결해야 하기 때문)

    int data;
    struct Node *left;
    struct Node *right;

}Node;


Node* insert_node(Node *node, int data){

    if(node == NULL){   // 자식 노드가 없다면
        
        node = (Node *)malloc(sizeof(node)); // 1, 메모리를 할당
        node->left = NULL;                  // 2. 왼쪽 자식 노드 NULL 로 초기화
        node->right = NULL;                 // 3. 오른쪽 자식 노드 NULL 로 초기화
        node->data = data;                 // 4. 현재 노드에 값 삽입
    }

    else{   // 이진 탐색 트리 처럼 값 삽입
        
        if(node->data > data)
            node->left = insert_node(node->left,data);
        else
            node->right = insert_node(node->right,data);
    }

    return node;
}


void Inorder(Node* node){

    if(node == NULL)
        return;
    
    Inorder(node->left);        // 왼쪽 노드 부터 방문
    printf("%d ", node->data);   // 현재 노드 방문
    Inorder(node->right);       // 오른쪽 노드 방문
}



int main(){


    Node *root = NULL;

    root = insert_node(root,10);
    root = insert_node(root,3);
    root = insert_node(root,7);
    root = insert_node(root,12);
    root = insert_node(root,1);
    root = insert_node(root,17);
   
    Inorder(root);  // 중위 순회


    free(root); // 메모리 해제

    return 0;
}

