class TrieNode {
public:
    TrieNode* children[26];
    bool end;

    TrieNode() {
        for (int i = 0; i < 26; ++i) children[i] = nullptr;
        end = false;
    } 
};

class PrefixTree {
public:
    PrefixTree() { 
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = root;

        for (char c : word) {
            int i = c - 'a';
            if (cur->children[i] == nullptr) {
                cur->children[i] = new TrieNode();
            }
            cur = cur->children[i];
        }
        cur->end = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root; 

        for (char c : word) {
            int i = c - 'a';
            if (cur->children[i] == nullptr) return false;
            cur = cur->children[i];
        }

        return cur->end;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root; 

        for (char c : prefix) {
            int i = c - 'a';
            if (cur->children[i] == nullptr) return false;
            cur = cur->children[i];
        }

        return true;
    }

private:
    TrieNode* root;
};
