# simple linked list

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def insert(self, val):
        while self.next:
            self = self.next
        self.next = Node(val)

    def show_lst(self):
        while self.next:
            print(self.val)
            self = self.next
        print(self.val)

####

Ll1 = Node(10)
Ll1.insert(20)
Ll1.insert(30)

Ll1.show_lst()

print()
print(Ll1.val)
print(Ll1.next.val)
print(Ll1.next.next.val)
print(Ll1.next.next.next)