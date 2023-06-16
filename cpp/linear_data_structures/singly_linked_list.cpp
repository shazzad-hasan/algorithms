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

    // insert a node at the start of the list
    void add(int item){
      Node* temp = new Node(item);
      temp->setNext(head);
      head = temp;
    }

    // insert a node at the end of the list
    void append(int item){
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

    int size(){
      Node* current = head;
      int count = 0;
      while (current != nullptr){
        count++;
        current = current->getNext();
      }
      return count;
    }

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

    void remove(int item){
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
        previous->setNext(current->getNext());
      }
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
};

int main(){

  SinglyLinkedList L;
  L.add(31);
  L.add(77);
  L.add(17);
  L.add(93);
  L.add(26);
  L.add(54);
  
  L.display();

  cout<<"size: "<<L.size()<<endl;
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;
  L.remove(17);
  cout<<"Is 17 in the list? "<<L.search(17)<<endl;

  L.display();

  L.append(100);
  L.append(111);
  
  L.display();

  return 0;
}

