#linear search

'''
# binary search
ls=[1,2,3,6,8,9]
k=3
l=0
r=len(ls)-1
while l<=r:
    mid=(l+r)//2
    if ls[mid]==k:
        print(mid)
        break
    elif ls[mid]<k:
        l=mid+1
    else:
        r=mid-1

'''
# bubble sort
'''
l=[8,22,0,3,4,55,1,2]
for i in range(0,len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''
# selection sort
'''
l=[8,22,0,3,4,55,1,2]
for i in range(0,len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)
    '''
# insertion sort
'''
l=[8,22,0,3,4,55,1,2]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)
'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        cur=head
        while cur:
            l.append(cur.val)
            cur=cur.next
        print(l)
        for i in range(1,len(l)):
            v=l[i]
            j=i-1
            while j>=0 and l[j]>v:
                l[j+1]=l[j]
                j-=1
            l[j+1]=v
        print(f"{l} this is the list")
        newnode=ListNode(0)
        cur=newnode
        for i in l:
            cur.next=ListNode(i)
            cur=cur.next
        return newnode.next
    
