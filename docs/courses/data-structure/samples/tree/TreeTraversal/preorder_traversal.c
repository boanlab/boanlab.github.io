# include <stdio.h>
# include <stdlib.h>

typedef struct Node
{
    int item;
    struct Node* left;
    struct Node* right;
}Node;

Node* Insert(Node* root, int value) {
    if (root == NULL) {
        root = (Node*)malloc(sizeof(Node));
        root -> left = root -> right = NULL;
        root -> item = value;
        return root;
    } else {
        if (root -> item > value) root -> left = Insert(root -> left, value);
        else root -> right = Insert(root -> right, value);
    }
    
    return root;
}

Node* Search(Node* node, int value) {
    if (node == NULL) return NULL;

    if (node -> item == value) {
        return node;
    } else {
        if (node -> item > value) {
            return Search(node->left, value);
        } else {
            return Search(node->right, value);
        }
    }
}

Node* FindMinNode(Node* node) {
    Node* temp = node;
    
    while (temp->left != NULL) temp = temp -> left;

    return temp;
}

Node* Delete(Node* node, int value) {
    Node* newNode = NULL;

    if (node == NULL) return NULL;

    if (node->item > value) {
        node -> left = Delete(node->left, value);
    } else if (node->item < value) {
        node -> right = Delete(node->right, value);
    } else {
        if (node->right != NULL && node->left != NULL) {
            newNode = FindMinNode(node->right);
            node -> item = newNode->item;
            node -> right = Delete(node->right, newNode->item);
        } else {
            newNode = (node -> left == NULL) ? node->right : node->left;
            free(node);
            return newNode;
        }
    }

    return node;
}

void Preorder(Node* root) {
    if (root) {
        printf("%d", root->item);
        Preorder(root->left);
        Preorder(root->right);
    }
}

int main() {
    Node* root = NULL;

    root = Insert(root, 20);
    root = Insert(root, 10);
    root = Insert(root, 32);
    root = Insert(root, 4);
    root = Insert(root, 13);
    root = Insert(root, 25);
    root = Insert(root, 55);

    Preorder(root);
}