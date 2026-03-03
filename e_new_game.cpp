#include <bits/stdc++.h>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
#define pb push_back()
#define pob pop_back()
#define int long long
#define nl '\n'
#define print(x) cout << (x) << endl
#define show(v)                         \
    for (auto& x : v) cout << x << " "; \
    cout << endl
#define debug(i) cout << #i << ": " << i << endl

#define infi numeric_limits<ll>::max()
#define ninfi numeric_limits<ll>::min()
#define infd numeric_limits<ld>::infinity()
#define ninfd -numeric_limits<ld>::infinity()
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;

template <typename K, typename V>
using umap = unordered_map<K, V>;

static mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define RAND(a, b) uniform_int_distribution<long long>(a, b)(rng)
ll big = RAND(1, 1e9);
long long modPow(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2 == 1) {
            res = (res * base) % mod;
        }

        base = (base * base) % mod;
        exp /= 2;
    }

    return res;
}

void solve() {
    ll n, k;
    cin >> n >> k;
    vector<ll> nums(n);
    umap<ll, ll> cnt;
    for (ll& x : nums) {
        cin >> x;
        cnt[x]++;
    }
    vll keys;
    for (auto [k, v] : cnt) keys.push_back(k);
    sort(all(keys));

    ll ans = 0, num_card = 0, l = 0;

    for (int r = 0; r < keys.size(); r++) {
        num_card += cnt[keys[r]];
        while (r >= l && (keys[r] - keys[l] > r - l || r - l + 1 > k)) {
            num_card -= cnt[keys[l]];
            l += 1;
        }
        ans = max(ans, num_card);
    }
    cout << ans << nl;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    loop_from(_, 0, t) { solve(); }
}
