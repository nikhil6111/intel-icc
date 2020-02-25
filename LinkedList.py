# n = actual node(current node); it will follow properties of node & LL also
# start_node = head

##We will pass data to the every new Node
##it's next node pointer is set to None

Class Node:

	def __init__(self,data):
		self.data = data
		self.nextnode = None



#In the beginning the list is empty, so start node is None
#and size is zero

Class LinkedList:

	def __init__(self):
		self.start_node = None
		self.size = 0



#Check if start_node is None(list is empty)
#initialize a variable n; set it to start node; 
#loop until get None; print the data & set n to next node reference
#n is current Node

	def traverse_list(self):
		if self.start_node is None:
			print ("List is empty")
			return 
		else:
			n = self.start_node
			while n is not None:
				print (n.data, end=" ")
				n = n.nextnode



#Increment list size & create a new node by passing data to node class.
#If start_node is None(list is empty) then assign this newNode to start node.
#Else set newNode ref to current start_node & assign this new node to new start_node

	def insert_at_start(self,data):
		self.size = self.size + 1
		newNode = Node(data)

		if self.start_node is None:		
			self.start_node = newNode
		else:
			newNode.nextnode = self.start_node
			self.start_node = newNode



#If start_node is None(list is empty) then assign this newNode to start node.
#Else go to end(nextnode is None), and line this new node to next node

	def insert_at_end(self,data):
		self.size = self.size + 1
		newNode = Node(data)

		if self.start_node is None:		
			self.start_node = newNode
			return 
		else:
			n = self.start_node
			while n.nextnode is not None:
				n = n.nextnode
			n.nextnode = newNode



#Find the node first, n is at the required node & n.nextnode contains next node address
#copy the ref of n.nextnode to nextNoderef of your newly crearted node and
#redirect n.nextnode to you newNode

	def insert_after_data(self,x, value):
		n = self.start_node
		while n is not None:
			if n.data == x:
				break
			n = n.nextnode
		if n is None:
			print ("Item is not in list")
		else:
			newNode = Node(data)
			newNode.nextnode = n.nextnode
			n.nextnode = newNode


			
#Check either list is empty or the given value'snode is start node
#traverse the list and check nextnode.data is given value
#redirect newnode.nextnode to current nextnode & nextnode to newNode

	def insert_before_data(self,x, value):
		if self.start_node is None:
			print ("List is empty")
			return

		if x == self.start_node.data:
	        new_node = Node(data)
	        new_node.nextnode = self.start_node
	        self.start_node = new_node
	        return

		n = self.start_node
        while n.nextnode is not None:
            if n.nextnode.data == x:
                break
            n = n.nextnode
        if n.nextnode is None:
            print("data not in the found")
        else:
            new_node = Node(data)
            new_node.nextnode = n.nextnode
            n.nextnode = new_node


#index is given, check if it 1; then insert at the beginning
#start from start_node with index no. 1; iterate through index-1
#check the given value is in range or not

	def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.nextnode = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.nextnode
            i = i+1
        if n is None:
            print("Index out of range")
        else: 
            new_node = Node(data)
            new_node.nextnode = n.nextnode
            n.nextnode = new_node


#First Check the given list is empty
#iterate through end and increment your counter
	
	def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.nextnode
        return count



	 def search_item(self, x):
        if self.start_node is None:
            print("List is empty")
            return
        n = self.start_node
        while n is not None:
            if n.data == x:
                print("Item found")
                return True
            n = n.nextnode
        print("item not found")
        return False



	def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)



	def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.nextnode



	def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
		elif self.start_node.nextnode == None:
			self.start_node = None
			return 
        else:
			n = self.start_node
        	while n.nextnode.nextnode is not None:
            	n = n.nextnode
        	n.nextnode = None


	
	def delete_element_by_value(self, x):
    if self.start_node is None:
        print("The list has no element to delete")
        return

    if self.start_node.item == x:
        self.start_node = self.start_node.nextnode
        return

    n = self.start_node
    while n.nextnode is not None:
        if n.nextnode.data == x:
            break
        n = n.nextnode

    if n.nextnode is None:
        print("item not found in the list")
    else:
        n.nextnode = n.nextnode.nextnode



	def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.nextnode
            n.nextnode = prev
            prev = n
            n = next
        self.start_node = prev

