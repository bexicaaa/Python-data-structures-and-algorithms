#Implementation of a doubly linked lists in Python 

#Implementation of a doubly linked list: we want to be able to ->
# Add a new node to the head (beginning) of the list 
# Add a new node to the tail (end) end of the list 
#Remove a node from the head of the list
#Remove a node from the tail of the list
#Find and remove a specific node by its value
#Print out the nodes in the list in order from head to tail

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
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None  
    
# 1.) ADDING TO THE HEAD
#Check to see if there is a current head to the list 
#If there is (meaning the list is not empty), then we want to reset the pointers a the head of the list:

# Set the current head’s previous node to the new head
# Set the new head’s next node to the current head
# Update the head property to be the new head
# Finally, if there isn’t a current tail to the list (meaning the list was empty):
# Update the tail property to be the new head since that node will be both the head and tail of the list

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
      
    self.head_node = new_head

    if self.tail_node == None:
      self.tail_node = new_head
      
## 2.) ADDING TO THE TAIL 
    # Start by checking to see if there is a current tail to the list
    # If there is (meaning the list is not empty), then we want to reset the pointers at the tail of the list:
    #     Set the current tail’s next node to the new tail
    #     Set the new tail’s previous node to the current tail
    # Update the tail property to be the new tail
    # Finally, if there isn’t a current head to the list (meaning the list was empty):
    #     Update the head property to be the new tail since that node will be both the head and tail

  def add_to_tail(self, new_value):
   new_tail = Node(new_value)
   current_tail = self.tail_node
   
   if current_tail != None: 
     current_tail.set_next_node(new_tail)
     new_tail.set_prev_node(current_tail)
     
     #setting the lists tail to the new_tail
   self.tail_node = new_tail

   if self.head_node == None:
      self.head_node = new_tail
      
#3.) REMOVING THE HEAD 
    # Start by checking if there’s a current head to the list.
    #     If there isn’t, the list is empty, so there’s nothing to remove and the method ends
    # Otherwise, update the list’s head to be the current head’s next node
    # If the updated head is not None (meaning the list had more than one element when we started):
    #     Set the head’s previous node to None since there should be no node before the head of the list
    # If the removed head was also the tail of the list (meaning there was only one element in the list):
    #     Call .remove_tail() to make the necessary changes to the tail of the list (we will create this method in the next exercise!)
    # Finally, return the removed head’s value
  def remove_head(self):
    removed_head = self.head_node
    
    #Check if removed_head has no value. If so, that means there’s nothing to remove, so return None to end the method
    if removed_head == None:
      return None
    
    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()
  
  #4.) REMOVING THE TAIL 

    # Start by checking if there’s a current tail to the list.
    #     If there isn’t, The list is empty, so there’s nothing to remove, and the method ends
    # Otherwise, update the list’s tail to be the current tail’s previous node
    # If the updated tail is not None (meaning the list had more than one element when we started):
    #     Set the tail’s next node to None since there should be no node after the tail of the list
    # If the removed tail was also the head of the list (meaning there was only one element in the list):
    #     Call .remove_head() to make the necessary changes to the head of the list
    # Finally, return the old tail’s data

  def remove_tail(self):
    removed_tail = self.tail_node
    
    #Check if removed_tail has no value. If so, that means the list is empty and there’s nothing to remove
    
    if removed_tail == None:
      return None
    
    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()

    return removed_tail.get_value()
  
  # 5.) REMOVING BY VALUE I.
  #removing a specific element from anywhere in the list 
    # Iterate through the list to find the matching node
    # If there is no matching element in the list:
    #     Return None
    # If there is a matching node, we will then check to see if it is the head or tail of the list:
    #     If so, call the corresponding .remove_head() or .remove_tail() method
    # If not, that means the node was somewhere in the middle of the list. In that case:
    #     Remove it by resetting the pointers of its previous and next nodes
    # Finally, return the node’s value property

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
      break
      
    current_node = current_node.get_next_node()

#Outside your while loop, check if node_to_remove has any value. If it doesn’t, that means there was no matching node in the list
    if node_to_remove == None:
      return None

    # 6.) REMOVING BY VALUE 
    
#     his means resetting the pointers around the node.

# There are three cases here:

#     The node was the head of the list, in which case we can just call .remove_head()
#     The node was the tail of the list, in which case we can just call .remove_tail()
#     The node was somewhere in the middle of the list, in which case we will need to manually change the pointers for its previous and next nodes

#check if node to remove is the lists head
    if node_to_remove == self.head_node:
      self.remove_head()
    if node_to_remove == self.tail_node:
      self.remove_tail()
      
  #Else, we know that the node is somewhere in the middle of the list. To remove it, we will need to reset the pointers for the nodes around it.
# Now that we have our nodes, we can remove the pointers to and from node_to_remove and have next_node and prev_node point to each other.
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node) 
      prev_node.set_next_node(next_node) 
    return node_to_remove


    
  