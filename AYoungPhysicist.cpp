#include <iostream>

using namespace std;

int main() {
  int x = 0;
  int y = 0;
  int z = 0;
  int t;
  cin >> t;
  while (t--) {
    int x1, y1, z1;
    cin >> x1 >> y1 >> z1;
    x += x1;
    y += y1;
    z += z1;
  }
  if (x == 0 && y == 0 && z == 0) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}
