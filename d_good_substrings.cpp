#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
        TrieNode* children[26];
        bool is_end;
        int count;

        TrieNode() {
            for (int i = 0; i < 26; i++) children[i] = nullptr;
            is_end = false;
            count = 0;
        }
};

class Trie {
    public:
        TrieNode* root;
        vector<int> goods;
        long long ans;

        Trie(const vector<int>& goods) {
            this->root = new TrieNode();
            this->goods = goods;
            this->ans = 0;
        }

        void insert(const string& word, int start, int k) {
            TrieNode* node = root;
            int bad = 0;
            long long local_ans = 0;

            for (int i = start; i < (int)word.size(); i++) {
                int idx = word[i] - 'a';
                bad += (goods[idx] == 0);

                if (!node->children[idx]) {
                    node->children[idx] = new TrieNode();
                    if (bad <= k) local_ans++;
                }

                node->count = bad;
                node = node->children[idx];

                if (bad > k) {
                    ans += local_ans;
                    return;
                }
            }

            node->is_end = true;
            ans += local_ans;
        }
};

void solve() {
    string s, g;
    int k;
    cin >> s >> g >> k;

    vector<int> goods(26);
    for (int i = 0; i < 26; i++) {
        goods[i] = g[i] - '0';
    }

    Trie trie(goods);

    for (int i = 0; i < (int)s.size(); i++) {
        trie.insert(s, i, k);
    }

    cout << trie.ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
