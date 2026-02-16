// mod % 3 == 1 is always true
// nim % 3 == 2 is not true
// num % 3 == 0 is not true
#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}


void solve(){
    int n;
    cin >> n;
    if (n % 3 == 1){
        cout << "YES\n";
    }else{
        cout << "NO\n";
    }
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
