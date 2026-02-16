#include <bits/stdc++.h>
#include <cmath>
#include <functional>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}


void solve(vector<int> &primes){
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums){
        cin >> x;
    }
    sort(nums.begin(), nums.end(), greater<int>());
    long long p = 0;
    long long curr = 0;
    int ans = 0;
    for (int i = 0 ; i < n; i ++){
        p += primes[i];
        curr += nums[i];
        if (curr >= p){
            ans = i + 1;
        }
    }
    cout << n - ans << endl;
}
int main(){

    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    long long N = 6e6;
    vector<int> val , primes(N, 1);
    primes[0] = primes[1] = false;
    for (long long i = 2; i < N ; i ++){
        if (!(primes[i])) continue;
        val.push_back(i);
        for (long long j = i + i; j < N; j += i){
            primes[j] = 0;
        }
    }
    int t = 1;
    cin >> t;
    while(t--){
        solve(val);
    }
}
