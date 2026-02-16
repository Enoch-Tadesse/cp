#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
    ll n;
    cin >> n;
    vector<ll> nums(n);
    for (ll &x : nums){
        cin >> x;
    }
    ll ans = 1;
    ll l = 0;
    ll r = 0;
    while (r < nums.size()){
        while (r < nums.size() - 1 && nums[r] <= nums[r + 1]){
            r += 1;
        }
        ans = max(ans, r - l + 1);
        l = r + 1;
        r += 1;
    }
    cout << ans << "\n";
}
int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll t = 1;
    
    while(t--){
        solve();
    }
}
