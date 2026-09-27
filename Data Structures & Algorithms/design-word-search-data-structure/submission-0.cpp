class TrieNode {
public:
    TrieNode* children[26];
    bool end;

    TrieNode() {
        for (int i = 0; i < 26; ++i) children[i] = nullptr;
        end = false;
    }
};

class WordDictionary {
    bool search(string_view word, int i, TrieNode* cur) {
        if (!cur) return false;
        if (i == word.size()) return cur->end;
        if (word[i] == '.') {
            for (int j = 0; j < 26; ++j) {
                if (search(word, i+1, cur->children[j])) return true;
            }
        } else {
            int j = word[i] - 'a';
            return search(word, i+1, cur->children[j]);
        }
        return false;
    }
public:
    WordDictionary() {
        root = new TrieNode(); 
    }
    
    void addWord(string word) {
        TrieNode* cur = root;

        for (char c : word) {
            int i = c - 'a';
            if (cur->children[i] == nullptr) cur->children[i] = new TrieNode();
            cur = cur->children[i];
        }

        cur->end = true;
    }

    
    
    bool search(string word) {
        return search(word, 0, root);
    }

TrieNode* root;
};
