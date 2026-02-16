#include <bits/stdc++.h>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
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

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;

template <typename T>
using vec = vector<T>;

template <typename Container>
auto csum(const Container& v) -> decltype(*v.begin() + 0) {
    return accumulate(v.begin(), v.end(), decltype (*v.begin() + 0)(0));
}

template <typename Container>
auto cmax(const Container& c) -> decltype(*c.begin()) {
    return *max_element(c.begin(), c.end());
}

template <typename Container>
auto cmin(const Container& c) -> decltype(*c.begin()) {
    return *min_element(c.begin(), c.end());
}

template <typename Container, typename Key>
bool exist(const Container& c, const Key& k) {
    return c.find(k) != c.end();
}

template <typename Map>
auto keys(const Map& m) {
    using KeyType = typename Map::key_type;
    vector<KeyType> res;
    res.reserve(m.size());
    for (const auto& [k, _] : m) res.push_back(k);
    return res;
}

template <typename Map>
auto values(const Map& m) {
    using ValueType = typename Map::mapped_type;
    vector<ValueType> res;
    res.reserve(m.size());
    for (const auto& [_, v] : m) res.push_back(v);
    return res;
}

template <typename Map>
auto items(const Map& m) {
    using PairType = typename Map::value_type;
    vector<PairType> res;
    res.reserve(m.size());
    for (const auto& p : m) res.push_back(p);
    return res;
}

template <typename K, typename V>
using umap = unordered_map<K, V>;

struct Node {
        ll val;
        Node* left;
        Node* right;
        bool alive;
        Node(ll val)
            : val(val),
              alive(true),
              left(nullptr),
              right(nullptr) {}
};

struct HeapNode {
        ll cost;
        Node* left;
        Node* right;
        bool operator<(const HeapNode& other) const {
            if (cost != other.cost) return cost > other.cost;
            return true;
        }
};

void solve() {
    ll n;
    cin >> n;
    vector<ll> nums(n);
    for (ll& x : nums) {
        cin >> x;
    }

    if (n == 2) {
        print(max(nums[0], nums[1]));
        return;
    }

    vector<Node*> nodes(n);
    for (ll i = 0; i < n; i++) nodes[i] = new Node(nums[i]);
    for (ll i = 0; i < n; i++) {
        nodes[i]->left = nodes[(i - 1 + n) % n];
        nodes[i]->right = nodes[(i + 1) % n];
    }

    priority_queue<HeapNode> heap;
    for (int i = 0; i < n; i++) {
        Node* left = nodes[i];
        Node* right = nodes[(i + 1) % n];
        heap.push({max(left->val, right->val), left, right});
    }

    ll alive = n;
    ll ans = 0;
    while (alive > 1) {
        auto top = heap.top();
        heap.pop();
        ll cost = top.cost;
        auto left = top.left;
        auto right = top.right;

        if (!left->alive || !right->alive || left->right != right) continue;
        ans += cost;
        --alive;

        Node* newNode = new Node(cost);
        Node* a = left->left;
        Node* b = right->right;

        a->right = newNode;
        newNode->left = a;

        b->left = newNode;
        newNode->right = b;

        left->alive = false;
        right->alive = false;

        heap.push({max(a->val, newNode->val),  a, newNode});
        heap.push({max(b->val, newNode->val),  newNode, b});
    }
    print(ans);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;

    loop_from(_, 0, t) { solve(); }
}
