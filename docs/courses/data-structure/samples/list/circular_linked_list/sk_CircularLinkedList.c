#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
	element data;
	struct ListNode* link;
}ListNode;

ListNode * insert_first(ListNode* head, element data) {
	ListNode* node = (ListNode*)malloc(sizeof(ListNode));
	node->data = data;
	
	if (head == NULL) {
		head = node;
		node->link = head; // 기존에 노드가 없었다면 삽입된 첫 번째 노드의 링크는 자기 자신을 가리키게 한다. 
	}
	
	else {
		node->link = head->link;
		head->link = node;
	}
	
	return head; // 변경된 head 포인터 반환 
}

ListNode * insert_last(ListNode* head, element data) {
	ListNode* node = (ListNode*)malloc(sizeof(ListNode));
	node->data = data;
	
	if (head == NULL) {
		head = node;
		node->link = head; // 기존에 노드가 없었다면 삽입된 첫 번째 노드의 링크는 자기 자신을 가리키게 한다. 
	}
	
	else {
		node->link = head->link;
		head->link = node;
		head = node; // head의 위치를 새로운 노드로 바꾸어 새로운 노드가 마지막 노드가 되게 한다. 
	}
	
	return head; // 변경된 head 포인터 반환 
}

void print(ListNode* head) {
	ListNode* n = head->link;
	
	if (head == NULL) return;
	
	do {
		printf("%d -> ", n->data);
		n = n->link;
	}while(n != head);
	
	printf("%d\n", n->data);
	printf("\n");
}

int main() {
	ListNode* head = NULL;
	
	head = insert_last(head, 13);
	head = insert_last(head, 15);
	head = insert_first(head, 12);
	print(head);
	
}