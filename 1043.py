N = input()
class Tree:
    is_mirror = False
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def mid_order_traverse(self):
        if self.left:
            for node in self.left.mid_order_traverse():
                yield node

        yield self.value

        if self.right:
            for node in self.right.mid_order_traverse():
                yield node

    def post_order_traverse(self):
        if self.left:
            for node in self.left.post_order_traverse():
                yield node

        if self.right:
            for node in self.right.post_order_traverse():
                yield node

        yield self.value

    def check(self):
        tmp = -1
        for node in self.mid_order_traverse():
            if tmp==-1: tmp = node
            elif (not Tree.is_mirror and node < tmp) or \
                (Tree.is_mirror and node > tmp):
                return False
            tmp = node
        return True

def build_tree(pre_order):
    is_mirror = Tree.is_mirror
    if not pre_order:
        return None
    root = pre_order.pop(0)
    if not pre_order:
        return Tree(root, None, None)
    right = -1
    for i, node in enumerate(pre_order):
        if (not is_mirror and node >= root) or \
            (is_mirror and node < root):
            right = i
            break
    if right == -1:
        left_tree = build_tree(pre_order)
        right_tree = None
    else:
        left_tree = build_tree(pre_order[:right])
        right_tree = build_tree(pre_order[right:])
    return Tree(root, left_tree, right_tree)

pre_order = map(int, raw_input().split())
if N > 1:
    Tree.is_mirror = False if pre_order[1] < pre_order[0] else True
tree = build_tree(pre_order)
if not tree.check():
    print 'NO'
else:
    print 'YES'
    for node in tree.post_order_traverse():
        print node,
    print