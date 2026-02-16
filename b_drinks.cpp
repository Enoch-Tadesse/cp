#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}


void solve(){
    int n;
    cin >> n;
    int total = 0;
    vector<int> nums(n);
    for (int &x : nums){
        cin >> x;
        total += x;
    }
    cout << (float) total / n << endl;

}
int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    
    while(t--){
        solve();
    }
}
