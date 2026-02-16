#include <bits/stdc++.h>

#include <utility>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

vector<ll> genPrimes(ll left, ll right) {
    vector<ll> primes(right + 1, 1);
    vector<ll> output;
    primes[0] = 0;
    primes[1] = 0;
    for (ll i = 2; i < primes.size(); i++) {
        if (primes[i] == 1) {
            if (i >= left && i <= right) {
                output.push_back(i);
            }
            for (ll j = i + i; j < primes.size(); j += i) {
                primes[j] = 0;
            }
        }
    }
    return output;
}

void solve(vector<pair<ll, ll>>input, vector<ll> primes) { 
	for (int i = 0; i < input.size(); i++){
	}
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    vector<pair<ll, ll>> input;
    ll back = 0;
    ll front = 0;
    while (t--) {
        ll left, right;
        cin >> left >> right;
        back = min(back, left);
        front = max(front, right);
        pair<ll, ll> pair;
        pair.first = left;
        pair.second = right;
        input.push_back(pair);
    }
    vector<ll> primes = genPrimes(back, front);
    solve(input, primes);
}
