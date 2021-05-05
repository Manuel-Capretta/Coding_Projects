#include <stdio.h> 
#include <stdlib.h> 
  
struct Node { 
    int data; 
    struct Node* next; 
}; 
  
void printList();
void reverseList();

int main(){ 
    struct Node* head = NULL; 
    struct Node* second = NULL; 
    struct Node* last = NULL; 
  
    // allocate the position in the list to the nodes 
    head = (struct Node*)malloc(sizeof(struct Node)); 
    second = (struct Node*)malloc(sizeof(struct Node)); 
    last = (struct Node*)malloc(sizeof(struct Node)); 
  
    head->data = 1; // assign data in first node 
    head->next = second; // Link first with second 
  
    second->data = 2; // assign data to second node 
    second->next = last; // Link secind to last
  
    last->data = 3; // assign data to last node 
    last->next = NULL; // Link last to nothing
  
    printList(head); //Print the list, starting with the Head
  
    return 0; 
}

//Creating the Structure of the node
void printList(struct Node* n){ 
    while (n != NULL) { //List cannot start Empty and ends when Empty
		if(n != NULL){
        	printf(" %d ->", n->data); //Print the data value of the node
        	n = n->next; //n moves to the next linked node
				if(n == NULL){ //print NULL if list ends
				printf(" NULL");
			}
		}
    } 
} 

void reverseList(){
	
}