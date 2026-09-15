class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.order.remove((key, value))
            self.order.append((key, value))
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            k, v = self.order.popleft()
            self.cache.pop(k)
        if key in self.cache:
            self.order.remove((key, self.cache[key]))
        self.order.append((key, value))
        self.cache[key] = value