/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;

        unordered_map<Node*, Node*> old_to_new;
        queue<Node*> q;
        old_to_new[node] = new Node(node->val);
        q.push(node);

        while (!q.empty()) {
            Node* cur = q.front(); q.pop();
            for (Node* n : cur->neighbors) {
                if (old_to_new.find(n) == old_to_new.end()) {
                    old_to_new[n] = new Node(n->val);
                    q.push(n);
                }
                old_to_new[cur]->neighbors.push_back(old_to_new[n]);
            }
        }

        return old_to_new[node];
    }
};
