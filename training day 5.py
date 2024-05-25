
'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return trav(p.left,q.left) and trav(p.right,q.right)
        return trav(p,q)

'''
'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root
'''
'''
class graph:
    def __init__(self):
        self.d={}
    def add(self,u,v):
        if u not in self.d:
            self.d[u]=[]
            self.d[u].append(v)
        else:
            self.d[u].append(v)
    def bfs(self,root):
        queue=[root]
        visited=[root]
        while queue:
            curr=queue.pop(0)
            print(curr)
            for ele in self.d[curr]:
                if ele not in visited:
                    visited.append(ele)
                    queue.append(ele)
        print(visited)
t=graph()
t.add(3,1)
t.add(1,3)
t.add(2,1)
t.add(1,2)
t.bfs(3)
print(t.d)
'''
l=[[1,1,0,1],
   [0,0,0,1],
   [0,0,0,1],
   [1,0,0,1]]
count=0
def dfs(i,j,l):
    if i<0 or i>=len(l) or j<0 or j>=len(l[0]):
        return
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    dfs(i+1,j,l)
    dfs(i,j+1,l)
    
for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j]==1:
            count+=1
            dfs(i,j,l)
print(count)


























