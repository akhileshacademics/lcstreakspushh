class MyHashSet:

    def __init__(self):
        self.size=1000
        self.seen=[[]for _ in range(self.size)]

    def hash(self, key):
        return key % self.size
        

    def add(self, key: int) -> None:
        seen=self.seen[self.hash(key)]
       
        if key not in seen:
            seen.append(key)

    def remove(self, key: int) -> None:
        seen=self.seen[self.hash(key)]
        if key in seen:
            seen.remove(key)

    def contains(self, key: int) -> bool:
        seen=self.seen[self.hash(key)]
        return key in seen
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)