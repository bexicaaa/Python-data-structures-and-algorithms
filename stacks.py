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
  
#Stack class

class Stack:
  def __init__(self, limit = 1000):
    self.top_item = None #setting an instance property top_item to None
    self.limit = limit
    self.size = 0 
    
  
  
  #Push and Pop
  def push(self, value):
    #adding an if clause that checks if stack has space, if there is rest of the method should execute:
    
    item = Node(value) #Instantiate a Node with value as an argument and assign it to the variable item (because this item is a node, we have easy access to Node’s class methods)
    item.set_next_node(self.top_item) #Set item‘s next node to the stack’s current top_item using the Node method set_next_node()
    self.top_item = item #Set the stack instance’s top_item equal to the new item, adding it to the top of the stack
    self.size += 1 #keeping track of our stack size when we add new items
    
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node() #If we’re removing our stack’s top_item, we need to set a new top_item! Set the top_item equal to the node after item_to_remove
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
   

  
    
  #returning the value of the stacks top item
  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    else:
       print("Nothing to see here!")
  
    
#Stack sizes pt1
#With stacks, size matters. If we’re not careful, we can accidentally over-fill them with data. Since we don’t want any stack overflow, we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

#Stacks pt 2
#using helper methods
#First, we want one that checks if our stack has room for more items. We can use this in .push() to guard against pushing items to our stack when it’s full.

# Second, it’s helpful to have a method that checks if the stack is empty…
  def has_space(self):
    if self.limit > self.size:
      return True
  
  def is_empty(self):
    return self.size == 0 
  #anywhere where we have written if self.size > 0: can be replaced with if not self.is_empty()
  
#Defining an empty pizza stack 
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.pop()