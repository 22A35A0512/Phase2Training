class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        self.count=0
    def insert(self,val):
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def print(self):
        cur=self.head
        while cur!=None:
            print(cur.data)
            self.count+=1
            cur=cur.next
        print(self.count)
    def middle(self,val):
        newnode=node(val)
        i=1
        half=self.count//2
        if self.head==None:
            self.head=newnode
        else:
            cur=self.head
            while i!=half:
                cur=cur.next
                i+=1
            newnode.next=cur.next
            cur.next=newnode
        print(cur.next.data)
    def fast(self,val):
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        else:
            fast=self.head
            slow=self.head
            while fast.next!=None and fast.next.next!=None:
                slow=slow.next
                fast=fast.next.next
            newnode.next=slow.next
            slow.next=newnode
    def deleteatmiddle(self):
        if self.head==None:
            self.head=newnode
        else:
            fast=self.head
            slow=self.head
            temp=None
            while fast.next!=None and fast.next.next!=None:
                temp=slow
                slow=slow.next
                fast=fast.next.next
            temp.next=slow.next               
    def insertend(self,val):
        newnode=node(val)
        if self.head==None:
            self.head=newnode
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=newnode
    def deleteatbeg(self):
        if self.head==None:
            print("list is empty")
        else:
            self.head=self.head.next
    def deleteatend(self):
        if self.head==None:
            print("list id empty")
        else:
            cur=self.head
            while cur.next.next!=None:
                cur=cur.next
            cur.next=None
    def reverse(self):
        if self.head==None:
            print("list is empty")
        else:
            prev=None
            cur=self.head
            nex=None
            while cur!=None:
                nex=cur.next
                cur.next=prev
                prev=cur
                cur=nex
            self.head=prev
        
l=linkedlist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insertend(7)
l.insertend(6)
l.insertend(5)
l.print()
print("hiii")
l.reverse()
#l.fast(20)
#l.deleteatmiddle()
l.print()

