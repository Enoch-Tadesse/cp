#include <iostream>
#include <vector>

using namespace std;

int main() {
  int k, l, m, n, d;
  cin >> k >> l >> m >> n >> d;
  vector<bool> nums(d + 1, false);
  for (int num : {k, l, m, n}) {
    for (int i = num; i < d + 1; i += num) {
      nums[i] = true;
    }
  }
  int counter = 0;
  for (bool ver : nums)
    counter += int(ver);
  cout << counter << std::endl;
}
