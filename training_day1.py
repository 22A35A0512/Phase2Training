'''
a=input()
b=input()
print(zip(a,b))
for i in a:
    if i not in b:
        print("not isomorphic")
print("isomorphic")
'''
'''
if print("hi"):
    print("hello")
else:
    print("false")
    '''
'''
class aridi:
    l=[]
    def __init__(self,l,s):
        self.l=l
        self.s=s
    def push(self,data):
        if len(self.l)<=self.s:
            self.l.append(data)
        else:
            print("stack is full")
    def pop(self):
        print(self.l.pop())
    def peek(self):
        print("element at the top is",end=" ")
        print(self.l[-1])
v=aridi([10,20,30,40],5)
v.push(10)
v.push(5)
v.pop()
v.peek()
'''
'''
class aridi:
    l=[]
    def __init__(self,l,s):
        self.l=l
        self.s=s
    def enqueue(self,data):
        if len(self.l)<=self.s:
            self.l.append(data)
        else:
            print("stack is full")
    def dequeue(self):
        print(self.l.pop(0))
    def peek(self):
        print("element at the top is",end=" ")
        print(self.l[-1])
        print(self.l)
v=aridi([10,20,30,40],5)
v.push(10)
v.push(5)
v.pop()
v.pop()
v.peek()
'''
'''
s="54367+-*+"
d="123456789"
l=[]
for i in s:
    if i in d:
        l.append(int(i))
    else:
        a=l.pop()
        b=l.pop()
        if i=='+':
            l.append(a+b)
        elif i=='-':
            l.append(a-b)
        elif i=='*':
            l.append(a*b)
        elif i=='/':
            l.append(a/b)
print(l)
'''
s=[1,2,3,4,5,6,7,8,9]
n=3
flag=0
while len(s)>1:
    if flag==0:
        for i in range(n):
            if len(s)>1:
                s.pop(0)
            else:
                break
            flag=1
    else:
        for i in range(n):
            if len(s)>1:
                s.pop()
            else:
                break
            flag=0
print(s[0])
    
    
    
       
    
