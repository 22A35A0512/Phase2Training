class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class trees:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        if self.root==None:
            self.root=newnode
        else:
            cur=self.root
            while True:
                if cur.data<=data:
                    if cur.right==None:
                        cur.right=newnode
                        break
                    else:
                        cur=cur.right
                else:
                    if cur.left==None:
                        cur.left=newnode
                        break
                    else:
                        cur=cur.left
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
            
        
t=trees()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
inorder(t.root)
