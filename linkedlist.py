

class Node(object):
	def __init__(self, nextnode=None,data=None,isHead=False,isTail=False):
		self.next = nextnode
		self.isHead = isHead
		self.isTail = isTail
		self.data = data

	def getnext(self):
		return self.next
	
	def setnext(self,nextnode):
		self.next = nextnode	
	
	def __str__(self):
		return "data: %s" % self.data

class LinkedList(object):
	def __init__(self,):
		self.list = {}
		self.length = 0
		self.head = None
		
	def add(self,data):
		# if this is the first node, make it the head
		if self.length == 0:
			print "adding head"
			self.head = Node(data=data)
			self.length += 1
		else:
			temp = self.head
			indx = 1	
			print "adding another node"
			while temp.getnext() != None:
				temp = temp.getnext()
			node = Node(data=data)
			temp.setnext(node)
			self.length += 1
			
	def remove(self,data):
		pass
		
	def printlist(self):
		if self.head == None:
			print "empty list"
		else:
			temp = self.head
			while temp.getnext() != None:
				print temp
				temp = temp.getnext()
			print temp

if __name__ == "__main__":
	ll = LinkedList()
	ll.add("item 1")
	ll.add("item 2")
	ll.add("item 3")
	ll.add("item 4")
	ll.printlist()
