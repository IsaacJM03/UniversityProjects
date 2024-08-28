#include <stdio.h>
#include <stdlib.h>

struct node
{
  int value;
  struct node *next; //pointer to next node
};


void printList(struct node* node){
  while(node != NULL)
  {
    printf("%d ", node->value);
    node = node->next;
  }
  printf("\n");
};

struct node* reverseList(struct node* head) {
  // initialize 3 pointers
  struct node *current = head, *previous = NULL, *next;

  while (current!=NULL)
  {
    next = current->next; //store the next node

    current->next = previous; //reverse the current node's next pointer to point to the previous node

    // move pointers one position ahead
    previous = current;
    current = next;
  }
  return previous; //return head of reversed linked list
}

int main()
{
  struct node *head = NULL;
  struct node *one = NULL;
  struct node *two = NULL;
  struct node *three = NULL;

  // allocate memory
  one = malloc(sizeof(struct node));
  two = malloc(sizeof(struct node));
  three = malloc(sizeof(struct node));
  
  // assign values
  one->value = 1;
  two->value = 2;
  three->value = 3;

  // link the nodes
  one->next = two;
  two->next = three;
  three->next = NULL;

  head = one; //set the head

  // print the linked list
  printList(head);

}