__author__ = 'codervinod@gmail.com'

from collections import deque

class PyGraph(object):

	def __init__(self):
		self.gdict = {}

	def add_edge(self, a, b):
		print "Adding edge from %s to %s"%(a,b)
		if a in self.gdict:
			self.gdict[a].append(b)
		else:
			self.gdict[a] = [b]

	def dfsUtil(self, node, visited):
		if node in visited:
			return

		visited.add(node)
		print "visiting %s"%(node)
		neighbor_list = self.gdict[node]
		for neighbor in neighbor_list:
			self.dfsUtil(neighbor, visited)
			
	def dfs(self):
		print "DFS Treversal"
		visited = set()
		for node in self.gdict.iterkeys():
			self.dfsUtil(node, visited)

	def bfs(self):
		print "BFS Treversal"
		
		if not self.gdict:
			return

		queue = deque()
		visited = set()
		start = self.gdict.iterkeys().next()

		queue.append(start)
		
		while queue:
			item = queue.popleft()
			if item in visited:
				continue
			print "visiting %s"%(item)
			visited.add(item)
			for neighbor in self.gdict[item]:
				queue.append(neighbor)

	def topoSortUtil(self, node, visited, topoStack):
		if node in visited:
			return

		visited.add(node)
		for neighbor in self.gdict[node]:
			self.topoSortUtil(neighbor, visited, topoStack)

		topoStack.append(node)

	def topoSort(self):
		print "Topology Sort"
		visited = set()
		topoStack = list()
		for node in self.gdict.iterkeys():
			self.topoSortUtil(node, visited, topoStack)

		while topoStack:
			print topoStack.pop()

def main():
	graph = PyGraph()
	graph.add_edge(1, 3)
	graph.add_edge(1, 2)
	graph.add_edge(3, 4)
	graph.add_edge(2, 4)
	graph.add_edge(4, 1)
	graph.add_edge(1, 4)

	graph.dfs()
	graph.bfs()
	graph.topoSort()

if __name__ == '__main__':
	main()
