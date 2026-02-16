#include <iostream>

using namespace std;

int main() {
  int k, n, w;
  cin >> k >> n >> w;

  int needed = (k * (w) * (w + 1)) / 2;
  cout << max(0, needed - n);
}
