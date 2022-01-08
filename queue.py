
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

#Queue class
#setting an instace properties inside method to None
class Queue:
  def __init__(self, max_size = None):
    self.head = None
    self.tail = None  
    self.size = 0
    self.max_size = max_size
    
  def peek(self):
    return self.head.get_value()

#Queues Python Size 
# Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. To account for this, we will need to make some modifications to our Queue class so that we can keep track of and limit size where needed.

# We’ll be adding two new properties to help us out here:

#     A size property to keep track of the queue’s current size
#     A max_size property that bounded queues can utilize to limit the total node count

# In addition, we will add three new methods:

#     get_size() will return the value of the size property
#     has_space() will return True if the queue has space for another node
#     is_empty() will return true if the size is 0
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
        self.size += 1
    else:
        print("Sorry, no more room!")
        
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")



  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("Nothing to see here!")
  
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None: 
      return True
    else:
      return self.max_size > self.get_size() 
  
  def is_empty(self):
    if self.size > 0:
      return False
    else:
      return True 


#QUEUES PYTHON ENQUEUE
# enqueue = add to the queue - > with enqueue() method:
# There are three scenarios that we are concerned with when adding a node to the queue:

#     The queue is empty, so the node we’re adding is both the head and tail of the queue
#     The queue has at least one other node, so the added node becomes the new tail
#     The queue is full, so the node will not get added because we don’t want queue “overflow”

# Let’s put this into action by building out an enqueue() method for Queue.


q = Queue()
q.enqueue("all the fluffy kitties")

#QUEUES PYTHON DEQUEUE 
#We can add items to the tail of our queue, but we remove them from the head using a method known as dequeue(), which is another way to say “remove from a queue”
#Like enqueue(), we care about the size of the queue — but in the other direction, so that we prevent queue “underflow

#For dequeue, there are three scenarios that we will take into account:

    # The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
    # The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s head and tail to None
    # The queue has more than one node, and we just remove the head node and reset the head to the following node

print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")


deli_line.enqueue("western omelet with home fries")

print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()

deli_line.dequeue()
