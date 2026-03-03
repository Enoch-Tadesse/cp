#include <bits/stdc++.h>

#include <algorithm>
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

class TrieNode {
    public:
        TrieNode* child[2];

        TrieNode() {
            child[0] = nullptr;
            child[1] = nullptr;
        }
};

class Trie {
        TrieNode root;

    public:
        Trie() { root = TrieNode(); }

        void insert(ll num) {
            TrieNode* curr = &root;
            for (int i = 46; i >= 0; i--) {
                ll b = (num >> i) & 1;
                if (!curr->child[b]) {
                    curr->child[b] = new TrieNode();
                }
                curr = curr->child[b];
            }
        }

        ll query(ll num) {
            ll ans = 0;
            TrieNode* curr = &root;

            for (int i = 46; i >= 0; i--) {
                ll b = (num >> i) & 1;
                ll tog = 1 ^ b;
                if (curr->child[tog]) {
                    ans |= ((1LL) << i);
                    curr = curr->child[tog];
                } else {
                    curr = curr->child[b];
                }
            }

            return ans;
        }
};

void solve() {
    ll n;
    cin >> n;
    vector<ll> nums(n);
    vll pre;
    ll p = 0;
    for (ll& x : nums) cin >> x, p ^= x, pre.push_back(p);
    ll s = 0;
    vll suf;
    for (int i = n - 1; i >= 0; i--) s ^= nums[i], suf.push_back(s);
    reverse(all(suf));

    Trie trie;
    ll ans = pre[n - 1];
    trie.insert(0);


    for (int i = 1; i < n; i++) {
		ans = max(ans, trie.query(suf[i]));
		ans = max(ans, pre[i]);
		trie.insert(pre[i]);
    }
    print(ans);
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
