class SuffixArray:
    def __init__(self, text):
        self.text = text
        self.suffix_array = self.build_suffix_array(text)
    
    def build_suffix_array(self, text):
        suffixes = [(text[i:], i) for i in range(len(text))]
        suffixes.sort()
        return [suffix[1] for suffix in suffixes]
    
    def display(self):
        return self.suffix_array


text = "banana"
suffix_arr = SuffixArray(text)
print(suffix_arr.display())