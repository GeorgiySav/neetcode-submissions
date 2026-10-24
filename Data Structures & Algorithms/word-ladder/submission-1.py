class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        def is_edge(w1, w2):
            dif = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if dif != 0:
                        return False
                    dif = 1
            return True

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if is_edge(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        for j in range(len(wordList)):
            if is_edge(beginWord, wordList[j]):
                adj[beginWord].append(wordList[j])
                adj[wordList[j]].append(beginWord)
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()

        while queue:
            cur, depth = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)

            for nei in adj[cur]:
                if nei == endWord:
                    return depth+1
                queue.append((nei, depth+1))
        
        return 0
