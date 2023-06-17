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

    void display(){
      cout<<"Current Linked List: ";
      Node* current = head;
      while (current != nullptr){
        cout<<current->getValue()<<" ";
        current = current->getNext();
      }
      cout<<endl;
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

      if (len < pos){
        cout<<"Index out of range"<<endl;
        return;
      }

      if (pos == 0){
        head = head->getNext();
        return;
      }

      for (int i=0; i<pos-1; i++){
        previous = current;
        current = current->getNext();
      }
      // change the next pointer of the previous node
      previous->setNext(current->getNext());
    }
};

int main(){

  SinglyLinkedList L;
  L.insert_first(3);
  L.insert_first(7);
  L.insert_first(17);
  L.insert_first(43);
  L.insert_first(26);
  L.insert_first(54);
  
  L.display();

  cout<<"size: "<<L.size()<<endl;
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;
  L.delete_item(17);
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;

  L.display();

  L.insert_last(60);
  L.insert_last(75);

  L.display();

  L.delete_at(2);
  L.display();

  L.insert_at(3, 93);
  L.display();

  return 0;
}

