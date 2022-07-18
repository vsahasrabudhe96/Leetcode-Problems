## Creating the root

class Node:
	def __init__(self,data):
		self.right = None
		self.left = None
		self.data = data

	## insert a node
	def insert(self,data):
		if self.data:
			if data < self.data:
				if self.left ==None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data>self.data:
				if self.right  == None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()


