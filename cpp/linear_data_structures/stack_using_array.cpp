/* C++ implementation of stack using array. */

#include <iostream>
using namespace std;

int const MAX_SIZE = 100;

class Stack{
  private:
    int top;
    int data[MAX_SIZE];

  public:
    Stack(){
      top = -1;
    }

    void push(int item){
      if (top >= MAX_SIZE-1){
        cout<<"Stack is full"<<endl;
        return;
      }
      data[++top] = item;
    }

    void pop(){
      if (top < 0){
        cout<<"Stack is empty"<<endl;
        return;
      }
      data[top--];
    }

    void peak(){
      if (top < 0){
        cout<<"Stack is empty"<<endl;
        return;
      }
      else {
        cout<<data[top]<<endl;
      }
    }

    bool isEmpty(){
      return (top < 0);
    }

    bool isFull(){
      return (top >= MAX_SIZE-1);
    }

    int size(){
      return top+1;
    }

    void display(){
      if (top < 0){
        cout<<"Stack is empty"<<endl;
        return;
      }
      cout<<"Stack elements are: ";
      for (int i=top; i>=0; i--){
        cout<<data[i]<<" ";
      }
      cout<<endl;
    }
};

int main(){
  Stack s;

  cout<<"Is the stack empty? "<<s.isEmpty()<<endl;

  s.push(50);
  s.push(8);
  s.push(15);
  s.push(10);

  s.display();
  cout<<"Number of elements in the stack: "<<s.size()<<endl;

  s.pop();
  s.display();
  cout<<"Number of elements in the stack: "<<s.size()<<endl;

  s.peak();
  cout<<"Is the stack full? "<<s.isFull()<<endl;

  return 0;
}