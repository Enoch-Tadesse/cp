#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, m, k;
    cin >> n >> m >> k;
    int big = std::max(n, std::max(m, k));
    int small = std::min(n, std::min(m, k));
    for (int num : {n, m, k}) {
      if (num != big && num != small) {
        std::cout << num << endl;
        break;
      }
    }
  }
}
