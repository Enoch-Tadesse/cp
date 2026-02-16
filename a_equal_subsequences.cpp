#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        int counter = 0;
        while (k--) {
            cout << 1;
            counter++;
        }
        while (counter < n) {
            cout << 0;
			counter ++;
        }
        cout << "\n";
    }
}
