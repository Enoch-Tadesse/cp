#include <iostream>
#include <string>

using namespace std;

int main() {
  int size;
  cin >> size;
  string word;
  cin >> word;
  int counter = 0;
  for (int i = 0; i < size - 1; i++) {
    if (word[i] == word[i + 1])
      counter += 1;
  }
  cout << counter << endl;
}
