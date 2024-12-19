class LinearIndexing:
    def __init__(self, data):
        self.data = data

    def search(self, key):
        for index, value in enumerate(self.data):
            if key == value:
                return index
        return -1
    
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    key = 20
    indexer = LinearIndexing(data)
    index = indexer.search(key)
    if index != -1:
        print(f"key {key} found at index {index} in {data}")
    else:
        print(f"key not found in {data}")