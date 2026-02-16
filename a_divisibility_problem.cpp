#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
    int n , m;
    cin >> n >> m;
    if (n % m == 0) {
        cout << 0 << endl;
        return;
    }
    int r = n / m;
    // cout << "cand1 " << m * (r + 1) << m << " " << r << endl;
    // cout << "cand2 " << m * r << endl;
    cout << (m * (r + 1) - n) << "\n";
}
int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    while(t--){
        solve();
    }
}
