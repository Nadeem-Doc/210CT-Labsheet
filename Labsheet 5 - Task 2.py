class Node():
      def __init__(self, value):
          self.value=value
          self.next=None # node pointing to next
          self.prev=None # node pointing to prev

class List():
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next = n.next
              n.next = x
              x.prev = n  
              if x.next != None:
                  x.next.prev = x              
          if self.head == None:
              self.head = self.tail = x #assigns the value of x to the head and tail
              x.prev = x.next = None
          elif self.tail == n:
              self.tail = x #reassigns the tail to the current node

      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ", ",".join(values))

      def lisrem(self,n):
            if n.prev != None:
                 n.prev.next = n.next
            else:
                  l.head = n.next
            if n.next != None:
                  n.next.prev = n.prev
            else:
                  l.tail = n.prev
          
if __name__ == '__main__':
      l=List()
      n = Node(6)
      n1 = Node(2)
      n2 = Node(3)
      n3 = Node(4)


      l.insert(None, n)
      l.insert(l.head,n1)
      l.insert(l.head,n2)
      l.insert(l.head,n3)
      l.lisrem(n)
      l.display()
