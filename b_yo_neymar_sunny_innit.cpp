#include <bits/stdc++.h>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
#define pb push_back
#define pob pop_back
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
    int n;
    cin >> n;

    vector<int> arr(n + 1);
    vector<int> pos(n + 1);
    loop_from(i, 1, n + 1) {
        cin >> arr[i];
        pos[arr[i]] = i;
    }

    set<int> seen = {-1, 0, n + 1, n + 2};
    vector<ll> ans(n + 15, 0);

    loop_from(i, 1, n + 1) {
        int p = pos[i];

        auto it = seen.upper_bound(p);
        int nxt = *it;
        int nnxt = *next(it);
        int prv = *prev(it);
        int pprv = *prev(prev(it));

        ll L = p - prv;
        ll Lp = p - pprv;
        ll R = nxt - p;
        ll Rp = nnxt - p;

        auto add = [&](vector<ll>& ans, int l, int r, ll val) {
            ans[l] += val;
            ans[r] -= val;
        };

        add(ans, 0, prv, L * R * i);
        add(ans, prv, prv + 1, (Lp - 1) * R * i);
        add(ans, prv + 1, p, (L - 1) * R * i);
        add(ans, p + 1, nxt, L * (R - 1) * i);
        add(ans, nxt, nxt + 1, L * (Rp - 1) * i);
        add(ans, nxt + 1, n + 3, L * R * i);

        seen.insert(p);
    }

    loop_from(i, 1, n + 1) {
        ans[i] += ans[i - 1];
        cout << ans[i] << " ";
    }
    cout << nl;
}

int left(int p, ll vl, Seg& seg) {
    if (p <= 0) return -1;
    if (seg.query(0, p - 1) > vl) return -1;
    ll l = 0, r = p;
    while (r - l > 1) {
        ll mid = (l + r) / 2;
        if (seg.query(mid, p - 1) > vl)
            r = mid;
        else
            l = mid;
    }
    return l;
}

int right(ll p, ll vl, ll n, Seg& seg) {
    if (p >= n - 1) return n;
    if (seg.query(p + 1, n - 1) > vl) return n;
    int l = p, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r + 1) / 2;
        if (seg.query(p + 1, mid) > vl)
            l = mid;
        else
            r = mid;
    }
    return r;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    loop(_, t) { solve(); }
}
