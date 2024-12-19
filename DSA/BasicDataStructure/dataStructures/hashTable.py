class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, "Not found")

    def delete(self, key):
        if key in self.table:
            del self.table[key]
        else:
            return "Key not found"


ht = HashTable()
ht.insert("name", "Alice")
print(ht.get("name"))
ht.delete("name")
print(ht.get("name"))
