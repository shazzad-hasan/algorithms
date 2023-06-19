#include <iostream>
#include <stack>
using namespace std;

int main(){
  stack<int> s;

  cout<<"Is the stack empty? "<<s.empty()<<endl; 
  cout<<"Total number of elements in the stack: "<<s.size()<<endl;

  s.push(11);
  s.push(50);
  s.push(45);
  s.push(36);

  cout<<"Is the stack empty? "<<s.empty()<<endl;
  cout<<"Number of elements in the stack: "<<s.size()<<endl;

  cout<<"Stack elements are: ";
  while (!s.empty()){
    cout<<s.top()<<" ";
    s.pop();
  }
  cout<<endl;

  return 0;
}