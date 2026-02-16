#include <bits/stdc++.h>

#include <ios>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<ll> vl;
class Node {
    public:
        ll linv, rinv, valid;
        Node() {
            linv = 0;
            rinv = 0;
            valid = 0;
        }
};

class SegmentTree {
    private:
        vector<Node> st;
        vector<char> words;
        int n;

        int left(int x) { return (x << 1) + 1; }
        int right(int x) { return (x << 1) + 2; }

        void build(int pos, int l, int r) {
            if (l == r) {
                if (words[l] == '(') {
                    st[pos].linv += 1;
                } else {
                    st[pos].rinv += 1;
                }
                return;
            }
            int mid = l + (r - l) / 2;
            build(left(pos), l, mid);
            build(right(pos), mid + 1, r);
            int new_valid = min(st[left(pos)].linv, st[right(pos)].rinv);
            st[pos].valid =
                st[left(pos)].valid + st[right(pos)].valid + new_valid;
            st[pos].linv = st[right(pos)].linv + st[left(pos)].linv - new_valid;
            st[pos].rinv = st[right(pos)].rinv - new_valid + st[left(pos)].rinv;
            return;
        }

        Node queryHelper(int pos, int l, int r, int L, int R) {
            if (l > R || r < L) return Node();
            if (l >= L && r <= R) {
                return st[pos];
            }
            int mid = l + (r - l) / 2;

            Node newNode = Node();
            Node s1 = queryHelper(left(pos), l, mid, L, R);
            Node s2 = queryHelper(right(pos), mid + 1, r, L, R);

            ll newValid = min(s1.linv, s2.rinv);
            newNode.valid = s1.valid + s2.valid + newValid;

            newNode.linv = s1.linv + s2.linv - newValid;
            newNode.rinv = s1.rinv + s2.rinv - newValid;
            return newNode;
        }

        void flipHelper(int pos, int idx, int l, int r) {
            if (l == r) {
                if (words[l] == '(') {
                    words[l] = ')';
                    st[pos].linv = 0;
                    st[pos].rinv = 1;
                } else {
                    words[l] = '(';
                    st[pos].rinv = 0;
                    st[pos].linv = 1;
                }
				st[pos].valid = 0;
                return;
            } else {
                int mid = l + (r - l) / 2;
                if (idx <= mid)
                    flipHelper(left(pos), idx, l, mid);
                else
                    flipHelper(right(pos), idx, mid + 1, r);
                int new_valid = min(st[left(pos)].linv, st[right(pos)].rinv);
                st[pos].valid =
                    st[left(pos)].valid + st[right(pos)].valid + new_valid;
                st[pos].linv =
                    st[right(pos)].linv + st[left(pos)].linv - new_valid;
                st[pos].rinv =
                    st[right(pos)].rinv - new_valid + st[left(pos)].rinv;
            }
            return;
        }

    public:
        SegmentTree(string words) {
            this->words.assign(words.begin(), words.end());
            n = words.size();
            st.assign(4 * n, Node());
            build(0, 0, n - 1);
        }
        ll query(int l, int r) {
            Node ans = queryHelper(0, 0, n - 1, l, r);
            return ans.valid;
        }
        void flip(int idx) { flipHelper(0, idx, 0, n - 1); }
};

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

void solve() {
    string word;
    cin >> word;
    SegmentTree* sg = new SegmentTree(word);
    int q;
    cin >> q;
    int l, r;
    loop(_, q) {
        cin >> l >> r;
        l--;
        r--;
        print(2 * sg->query(l, r));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
