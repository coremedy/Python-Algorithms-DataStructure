'''
Created on 2015-10-31
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        dq, q = collections.deque(), []
        dq.append(root)
        q.append(str(root.val))
        while dq:
            node = dq.popleft()
            if node:
                dq.append(node.left if node.left else None)
                q.append(str(node.left.val) if node.left else '')
                dq.append(node.right if node.right else None)
                q.append(str(node.right.val) if node.right else '')
        return '#'.join(q).rstrip('#')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        d, dq, index = data.split('#'), collections.deque(), 1
        root = TreeNode(int(d[0]))
        dq.append(root)
        while index < len(d):
            num_to_read = len(dq) * 2
            for num_index in range(index, min(index + num_to_read, len(d))):
                if len(d[num_index]) > 0:
                    dq.append(TreeNode(int(d[num_index])))
                    if (num_index - index) % 2 == 0:
                        dq[(num_index - index) // 2].left = dq[-1]
                    else:
                        dq[(num_index - index) // 2].right = dq[-1]
            index, num_to_read = min(index + num_to_read, len(d)), num_to_read // 2
            while num_to_read > 0:
                dq.popleft()
                num_to_read -= 1
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    pass