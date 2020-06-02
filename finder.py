import requests
import json
import time

class Node():
	def __init__(self, value):
		self.value = value
		self.edges = []
		self.searched = False
		self.parent = None

	def addEdge(self,neighbour):
		self.edges.append(neighbour)
		neighbour.edges.append(self)

class Graph():
	def __init__(self):
		self.nodes = []
		self.graph = {}
		self.start = None
		self.end = None

	def add_node(self, n):
		self.nodes.append(n)
		title = n.value
		self.graph[title] = n

	def getNode(self, actor):
		try:
			return self.graph[actor]
		except:
			return None

	def setStart(self, actor):
		self.start = self.graph[actor]

	def setEnd(self, actor):
		self.end = self.graph[actor]

def return_actors():
	g = Graph()
	f = open('personal.json') 
	actors = []
	data = json.load(f) 
	for i in data:
		for x in data[i]:
			actors.append(x)
	actors = set(actors)
	return actors

def return_track(start_name, end_name):
	g = Graph()
	f = open('personal.json') 
	actors = []
	data = json.load(f) 
	
	for m in data:
	    	title = m
	    	cast = data[m]
	    	movieNode = Node(title)
	    	g.add_node(movieNode)


	    	for c in cast:
	    		actor = c
	    		actorNode = g.getNode(actor)
	    		if(actorNode == None):
	    			actorNode = Node(actor)

	    		g.add_node(actorNode)
	    		movieNode.addEdge(actorNode)





	g.setStart(start_name)
	g.setEnd(end_name)


	queue = []
	track = []

	start = g.graph[start_name]
	end = g.graph[end_name]

	start.searched = True
	queue.append(start)
	found = False

	while(queue):
		current = queue[0]
		queue.pop(0)
		if(current == end):
			found = True
		edges = current.edges
		for neighbour in edges:
			if not neighbour.searched:
				neighbour.searched = True
				neighbour.parent = current
				queue.append(neighbour)
		if(found):
			break


	path = []
	path.append(end)
	next = end.parent
	while(next != None):
		path.append(next)
		next = next.parent
	#print(len(data))
	for p in range(len(path)-1,-1, -1):
		#print(path[p].value)
		track.append(path[p].value)

	print(track)
	return (track)
