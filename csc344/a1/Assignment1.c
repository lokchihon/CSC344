// Name: Lok Chi Hon
// Programming Languages
// Assignment 1


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// declaring structs
// for Doubly Linked List
struct Node {
    char data;
    struct Node* next;
    struct Node* prev;
};

// for 2D Array
struct Instruction {
    char writeVal;
    char moveDir;
    int newState;
};

// Function declaration
void insertAtHead(struct Node** head, char newData);
void insertAtTail(struct Node** head, char newData);
void printAll(struct Node* node);

int main() {
    // variables
    int currentState;
    int numOfStates;
    int startState;
    int endState;

    char buffer;
    char buff[255];
    char *eachChar = malloc(sizeof(char));

    FILE *fp = fopen("input_test_1.txt", "r");
    
    printf("Writing tape...\n");

    if (fp == NULL){
        exit(EXIT_FAILURE);
    }

    struct Node* head = NULL;

    // taking first line of the input file and inserting it into the doubly linked list
    while(*eachChar !='\n' && *eachChar !='\r'){
       fscanf(fp, "%c", eachChar);
       if(*eachChar !='\n' && *eachChar !='\r'){
           insertAtTail(&head, *eachChar);
       }
    }
    
    // getting numOfStates from input file
    fscanf(fp, "%s",buff);
    buffer = buff[0];
    numOfStates = buffer-'0';

    // getting startState from input file
    fscanf(fp, "%s",buff);
    buffer = buff[0];
    startState = buffer-'0';

    // getting endState from input file
    fscanf(fp, "%s",buff);
    buffer = buff[0];
    endState = buffer-'0';  

    // making 2D array (numOfStates)x(255)
    struct Instruction** table = malloc(numOfStates*sizeof(struct Instruction*));
    for(int i = 0; i<numOfStates; i++){
        table[i] = malloc(255*sizeof(struct Instruction));
    }

    while(fgets(buff, 255, fp)){
       int currState = 0;
       char readValue[1] = "";
       char writeValue[1] = "";
       char moveDirection[1] = "";
       int moveToState = 0;

       fscanf(fp,"%d %c %c %c %d",&currState, readValue, writeValue, moveDirection, &moveToState);

       table[currState][(int)(*readValue)].writeVal = writeValue[0];
       table[currState][(int)(*readValue)].moveDir = moveDirection[0];
       table[currState][(int)(*readValue)].newState = moveToState;

    }
   
    printf("Initial tape contents: ");
    printAll(head);

    currentState = startState;
    struct Node* temp = head;

    // Turing Machine Implementation
    while(currentState != endState){
        char tempData = (temp->data);
        temp->data = table[currentState][tempData].writeVal;
        if(table[currentState][tempData].moveDir == 'R'){
            if(temp->next == NULL){
                insertAtTail(&head, 'B');
                temp = temp->next;
            }else{
                temp = temp->next;
            }
        }else{
            if(temp->prev == NULL){
                insertAtHead(&head, 'B');
                temp = temp->prev;
            }else{
                temp = temp->prev;
            }
        }
        currentState = table[currentState][tempData].newState;
    }

    printf("Final tape contents: ");
    printAll(head);

    fclose(fp);

    exit(EXIT_SUCCESS);

}

// inserting Node at head of doubly linked list
void insertAtHead(struct Node** head, char newData){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = (*head);
    newNode->prev = NULL;

    if ((*head) != NULL){
        (*head)->prev = newNode;
    }
    (*head) = newNode;
}

// inserting Node at tail of doubly linked list
void insertAtTail(struct Node** head, char newData){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* lastNode = (*head);
    newNode->data = newData;
    newNode->next = NULL;

    if((*head) == NULL){
        newNode->prev = NULL;
        (*head) = newNode;
        return;
    }
    while (lastNode->next != NULL){
        lastNode = lastNode->next;
    }

    lastNode->next = newNode;
    newNode->prev = lastNode;
}

// prints Doubly Linked List
void printAll(struct Node* node){
    struct Node* temp;
    while(node != NULL) {
        printf("%c", node->data);
        temp = node;
        node = node->next;
    }
    printf("\n");
}