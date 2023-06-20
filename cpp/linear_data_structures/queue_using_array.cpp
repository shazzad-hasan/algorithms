/* C++ implementation of queue using array. */

#include <iostream>
using namespace std;

const int MAX_SIZE = 1000;

class Queue{
  private:
    int front;
    int rear;
    int data[MAX_SIZE];
  public:
    Queue(){
      front = -1;
      rear = -1;
    }

    bool isEmpty(){
      return (front == -1 && rear == -1);
    }

    bool isFull(){
      return (rear == MAX_SIZE-1);
    }

    int size(){
      return rear-front+1;
    }

    void enqueue(int item){
      if (isFull()){
        cout<<"Queue is full"<<endl;
        return;
      }
      if (isEmpty()){
        front = 0;
        rear = 0;
      }
      else{
        rear++;
      }
      data[rear] = item;
    }

    void dequeue(){
      if (isEmpty()){
        cout<<"Queue is empty"<<endl;
        return;
      }
      if (front == rear){
        front = -1;
        rear = -1;
      }
      else {
        front++;
      } 
    }

    int peek(){
      if (isEmpty()){
        cout<<"Queue is empty"<<endl;
        return -1;
      }
      return data[front];
    }

    void display(){
      if (isEmpty()){
        cout<<"Queue is empty"<<endl;
        return;
      }
      cout<<"Queue elements are: ";
      for (int i=front; i<= rear; i++){
        cout<<data[i]<<" ";
      }
      cout<<endl;
    }

};

int main(){
  Queue q;

  cout<<"Is the queue empty? "<<q.isEmpty()<<endl;

  q.enqueue(10);
  q.enqueue(36);
  q.enqueue(76);
  q.enqueue(50);
  q.enqueue(85);

  cout<<"Is the queue empty? "<<q.isEmpty()<<endl;
  cout<<"Number of elements in the queue: "<<q.size()<<endl;
  
  q.display();

  q.dequeue();
  cout<<"Front element is: "<<q.peek()<<endl;
  q.dequeue();
  cout<<"Front element is: "<<q.peek()<<endl;

  q.display();
  cout<<"Is the queue empty? "<<q.isEmpty()<<endl;
  cout<<"Number of elements in the queue: "<<q.size()<<endl;

  return 0;
}

