#include <cmath>
#include <iostream>

#include <unordered_set>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        unsigned long long int n;
        cin >> n;
        unordered_set<unsigned long long int> seen;
        for (unsigned long long i = 1; i < ceil(cbrt(n)); i++)
            seen.insert(pow(i, 3));
        bool flag = false;
        for (auto num : seen) {
            if (seen.find(n - num) != seen.end()) {
                cout << "YES\n";
                flag = true;
                break;
            }
        }
        if (not flag)
            cout << "NO\n";
    }
}
