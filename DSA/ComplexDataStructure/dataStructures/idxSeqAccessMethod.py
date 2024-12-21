class ISAM:
    def __init__(self, block_size=10):
        self.block_size = block_size
        self.data = []
        self.index = {}

    def build_index(self):
        self.index.clear()
        for i in range(0, len(self.data), self.block_size):
            self.index[self.data[i][0]] = i

    def insert(self, record):
        self.data.append(record)
        self.data.sort(key=lambda x: x[0])
        self.build_index()

    def search(self, key):
        block_start = None
        for index_key in sorted(self.index):
            if key >= index_key:
                block_start = self.index[index_key]
            else:
                break

        if block_start is None:
            return None

        block_end = min(block_start + self.block_size, len(self.data))
        for record in self.data[block_start:block_end]:
            if record[0] == key:
                return record

        return None

    def display(self):
        print("Data:")
        for record in self.data:
            print(record)
        print("\nIndex Table:")
        for key, index in self.index.items():
            print(f"Key: {key}, Block Start Index: {index}")


if __name__ == "__main__":
    isam = ISAM(block_size=3)

    isam.insert((10, "Record A"))
    isam.insert((20, "Record B"))
    isam.insert((5, "Record C"))
    isam.insert((15, "Record D"))
    isam.insert((25, "Record E"))

    isam.display()

    print("\nSearch Results:")
    print(isam.search(15))
    print(isam.search(30))
