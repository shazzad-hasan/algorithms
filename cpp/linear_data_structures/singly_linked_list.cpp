#include <iostream>
using namespace std;

class Node{
  private:
    int value;
    Node* next;
  
  public:
    Node(int initValue){
      value = initValue;
      next = nullptr;
    }

    int getValue(){
      return value;
    }

    void setValue(int newValue){
      value = newValue;
    }

    Node* getNext(){
      return next;
    }

    void setNext(Node* newNext){
      next = newNext;
    }
};

class SinglyLinkedList{
  public:
    Node* head;
    SinglyLinkedList(){
      head = nullptr;
    }

    bool isEmpty(){
      return head == nullptr;
    }

    int size(){
      Node* current = head;
      int count = 0;
      while (current != nullptr){
        count++;
        current = current->getNext();
      }
      return count;
    }

    // insert a node at the start of the list
    void insert_first(int item){
      Node* temp = new Node(item);
      temp->setNext(head);
      head = temp;
    }

    // insert a node at the end of the list
    void insert_last(int item){
      Node* temp = new Node(item);

      if (head == nullptr){
        temp->setNext(head);
        head = temp;
      }

      Node* current = head;
      while (current->getNext() != nullptr){
        current = current->getNext();
      }
      current->setNext(temp);
    }

    // insert a node at a given position
    void insert_at(int pos, int item){
      Node* current = head;
      Node* temp = new Node(item);

      int len = 0;
      while (current != nullptr){
        len++;
        current = current->getNext();
      }
      current = head;

      if (pos < 0 || pos > len-1){
        cout<<"Invalid position"<<endl;
        return;
      }

      for (int i=0; i<pos-1; i++){
        current = current->getNext();
      }

      temp->setNext(current->getNext());
      current->setNext(temp);

    }

    // search whether a given node exists
    bool search(int item){
      Node* current = head;
      while (current != nullptr){
        if (current->getValue() == item){
          return true;
        }
        else {
          current = current->getNext();
        }
      }
      return false;
    }

    // delete a given node 
    void delete_item(int item){
      Node* current = head;
      Node* previous = nullptr;
      bool found = false;
      while (!found){
        if (current->getValue() == item){
          found = true;
        }
        else {
          previous = current;
          current = current->getNext();
        }
      }
      if (previous == nullptr){
        head = current->getNext();
      }
      else {
        // change the next pointer of the previous node
        previous->setNext(current->getNext());
      }
    }

    // delete  the first node
    void delete_first(){
      head = head->getNext();
    }

    // delete the last node
    void delete_last(){
      Node* current = head;

      while (current->getNext()->getNext() != nullptr){
        current = current->getNext();
      }
      delete (current->getNext());
      current->setNext(nullptr);
    }

    // delete a node at a given position
    void delete_at(int pos){
      Node* current = head;
      Node* previous = nullptr;

      if (head == nullptr){
        cout<<"Empty List"<<endl;
        return;
      }

      int len = 0;
      while (current != nullptr){
        len++;
        current = current->getNext();
      }
      current = head;

      if (pos < 0 || pos > len-1){
        cout<<"Invalid position"<<endl;
        return;
      }

      if (pos == 0){
        delete_first();
        return;
      }

      for (int i=0; i<pos; i++){
        previous = current;
        current = current->getNext();
      }
      // change the next pointer of the previous node
      previous->setNext(current->getNext());
    }

    // print the linked list
    void display(){
      cout<<"Current Linked List: ";
      Node* current = head;
      while (current != nullptr){
        cout<<current->getValue()<<" ";
        current = current->getNext();
      }
      cout<<endl;
    }
};

int main(){

  SinglyLinkedList L;

  cout<<"Is L an empty linked list? "<<L.isEmpty()<<endl;

  L.insert_first(3);
  L.insert_first(7);
  L.display();
  L.insert_last(43);
  L.insert_last(26);
  L.display();
  L.insert_at(2, 17);
  L.insert_at(4, 55);
  L.display();

  cout<<"Does L is an empty linked list? "<<L.isEmpty()<<endl;
  cout<<"size: "<<L.size()<<endl;
  
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;

  L.delete_item(17);
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;
  L.display();

  L.delete_first();
  L.delete_last();
  L.display();

  L.delete_at(-1);
  L.delete_at(100);
  L.display();

  L.delete_at(1);
  L.display();

  return 0;
}

