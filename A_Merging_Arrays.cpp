#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> nums1(n);
    for (int &x : nums1) {
        cin >> x;
    }
    vector<int> nums2(m);
    for (int &x : nums2) {
        cin >> x;
    }
    vector<int> out;
    out.reserve(n + m);
    int i = 0;
    int j = 0;
    while (i < n && j < m) {
        if (nums1[i] < nums2[j]) {
            out.push_back(nums1[i]);
            i += 1;
        } else {
            out.push_back(nums2[j]);
            j++;
        }
    }
    while (i < n) {
        out.push_back(nums1[i]);
        i += 1;
    }
    while (j < m) {
        out.push_back(nums2[j]);
        j += 1;
    }
    for (int &x : out) {
        cout << x << " ";
    }
}
int main() {

    int t = 1;

    while (t--) {
        solve();
    }
}
