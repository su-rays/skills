class BTreeNode:
    def __init__(self, t, is_leaf=True):
        self.t = t
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, is_leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, k)

    def _split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        new_node = BTreeNode(t, child.is_leaf)
        
        parent.keys.insert(i, child.keys[t - 1])
        new_node.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        
        if not child.is_leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]
        
        parent.children.insert(i + 1, new_node)

    def _insert_non_full(self, node, k):
        if node.is_leaf:
            node.keys.append(k)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def delete(self, k):
        self._delete(self.root, k)
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]

    def _delete(self, node, k):
        t = self.t
        idx = self._find_key(node, k)
        
        if idx < len(node.keys) and node.keys[idx] == k:
            if node.is_leaf:
                node.keys.pop(idx)
            else:
                self._delete_internal_node(node, k, idx)
        else:
            if node.is_leaf:
                print(f"Key {k} not found in the tree.")
                return
            
            flag = idx == len(node.keys)
            if len(node.children[idx].keys) < t:
                self._fill(node, idx)
            
            if flag and idx > len(node.keys):
                self._delete(node.children[idx - 1], k)
            else:
                self._delete(node.children[idx], k)

    def _find_key(self, node, k):
        for i, key in enumerate(node.keys):
            if k <= key:
                return i
        return len(node.keys)

    def _delete_internal_node(self, node, k, idx):
        if len(node.children[idx].keys) >= self.t:
            pred = self._get_predecessor(node.children[idx])
            node.keys[idx] = pred
            self._delete(node.children[idx], pred)
        elif len(node.children[idx + 1].keys) >= self.t:
            succ = self._get_successor(node.children[idx + 1])
            node.keys[idx] = succ
            self._delete(node.children[idx + 1], succ)
        else:
            self._merge(node, idx)
            self._delete(node.children[idx], k)

    def _get_predecessor(self, node):
        while not node.is_leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _get_successor(self, node):
        while not node.is_leaf:
            node = node.children[0]
        return node.keys[0]

    def _fill(self, node, idx):
        if idx != 0 and len(node.children[idx - 1].keys) >= self.t:
            self._borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= self.t:
            self._borrow_from_next(node, idx)
        else:
            if idx != len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])
        if not sibling.is_leaf:
            child.children.insert(0, sibling.children.pop(-1))
        node.keys[idx - 1] = sibling.keys.pop(-1)

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys[idx])
        if not sibling.is_leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]
        child.keys.append(node.keys.pop(idx))
        child.keys.extend(sibling.keys)
        if not child.is_leaf:
            child.children.extend(sibling.children)
        node.children.pop(idx + 1)

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        print(indent, "`-" if last else "|-", node.keys)
        indent += "   " if last else "|  "
        for i, child in enumerate(node.children):
            self.print_tree(child, indent, i == len(node.children) - 1)

if __name__ == "__main__":
    t = 3  
    btree = BTree(t)
    keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]

    for key in keys_to_insert:
        btree.insert(key)

    print("B-Tree after insertion:")
    btree.print_tree()

    btree.delete(6)
    print("\nB-Tree after deleting 6:")
    btree.print_tree()