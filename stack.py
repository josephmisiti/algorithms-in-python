
import re,os,sys

class Node(object):
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
		
	def setnext(self,next):
		self.next = next
		
	def __str__(self):
		return "%s" % self.data


class LinkedListStack(object):
	def __init__(self,max=0):
		self.max = max
		self.head = None
		self.z = None
		self.size = 0
		
	def push(self,data):
		if self.size == 0:
			self.head = Node(data=data)
			self.size += 1
		else:
			head = self.head
			temp = Node(data=data)
			self.head = temp
			temp.setnext(head)
	
	def pop(self):
		temp = self.head.next
		self.head = temp
		
	def isempty(self): 
		return self.size == 0

	def __str__(self):
		d = ""
		if self.isempty():
			return ""
		else:
			temp = self.head
			d += "%s\n" % temp
			while temp.next != None:
				temp = temp.next
				d += "%s\n" % temp
			return d
				
		


class Stack(object):
	def __init__(self):
		self.size = 0
		self.data = []
		
	def push(self,data):
		self.data.insert(0,data)
		self.size += 1
		
	def pop(self):
		if self.size == 0: return
		temp = self.data[0]
		self.data = self.data[1:]
		self.size -= 1
		
	def __str__(self):
		d = ""
		for item in self.data:
			d += "%s\n" % item
		return d[:-1]
		
def parse(line):
	s = Stack()
	datas = re.findall(r"([\w\*])",line)
	for d in datas:
		if d == "*":
			s.pop()
		else:
			s.push(d)
		print s
		print "--------------------"
		
if __name__ == "__main__":
	#parse("A * S A * M * P * L * E S * T * * * A * C K")
	
	ll = LinkedListStack(max = 20)
	ll.push("1")
	ll.push("2")
	ll.push("3")
	ll.push("4")
	print ll
	ll.pop()
	print ll
