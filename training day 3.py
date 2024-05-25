'''
l=[1,2,3]
k=5
t=len(l)
l2=[]
l3=[]
while t>0:
    temp=t/k
    if temp!=int(temp):
        temp=int(temp+1)
        t-=temp
        l2.append(temp)
        k=k-1
    else:
        t-=temp
        l2.append(int(temp))
        k=k-1
while k:
    l2.append(0)
    k=k-1
print(l2)
total=0
m=0
n=0
for i in l2:
    n+=i
    l3.append(l[m:n])
    m+=i
print(l3)
'''
'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        count=0
        if head==None:
            return None
        else:
            while cur:
                count+=1
                cur=cur.next
        i=1
        cur=head
        while i!=k:
            i+=1
            cur=cur.next
        a=cur.val
        print(a)
        j=(count-k)
        temp=head
        i=0
        while i!=j:
            i+=1
            temp=temp.next
        b=temp.val
        cur.val=b
        temp.val=a
        return head
        '''
