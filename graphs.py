class DirectedACyclicGraph:
	def __init__(self, graph_title):
		self.nodes = dict()
		self.title = graph_title

	def add_node(self, node):
		if node.name in self.nodes.keys():
			raise RepeatNodeExceptionError(node_name, self.title)
		self.nodes[node.name] = node

	def _make_and_add_from_list(self, root_node_name, arc_type, list_of_names):
		for node_name in list_of_names:
			self.add_node(Node(node_name))
			self.add_arc(root_node_name, arc_type, node_name)


	def remove_node(self, node_name):
		#remove all references to the node from all other nodes and from the graph's dict
		if node_name in self.nodes.keys():
			for node in self.nodes.values():
				for node_list in node.connections:
					for node_in_list in node_list:
						if node_in_list.name == node_name:
							node_list.remove(node)

			del self.nodes[node_name]

	def add_arc(self, origin_node_name, arc_type, destination_node_name):
		"""
		adds a connections of the specifiedd type between two already existing nodes
		"""
		if not destination_node_name in self.nodes.keys():
			raise NodeNotFoundError(destination_node_name)
		elif not origin_node_name in self.nodes.keys():
			raise NodeNotFoundError(origin_node_name)

		self.nodes[origin_node_name].add_arc(arc_type, self.nodes[destination_node_name])

	def to_string(self, long_or_short_bool):
		'''
		if long_or_short_bool is True then the long to_string will be returned.
		Otherwise the short to_string will be 
		'''
		result = "Title: " + self.title + "\n"
		for node in self.nodes.values():
			result += node.to_string(long_or_short_bool)

		return result

	def decendent_tree_string(self, root_node_name, branch_arc_type):
		if not root_node_name in self.nodes.keys():
			raise NodeNotFoundError(root_node_name)
		if not branch_arc_type in self.nodes[root_node_name].connections.keys():
			error_message = "root node has no arc type " + branch_arc_type
			raise Error(error_message)
		result = branch_arc_type + " of " + root_node_name + "\n" 
		result += self.nodes[root_node_name].decendent_tree_string(branch_arc_type, "")

		return result



class Node:
	def __init__(self, name):
		self.name = name
		self.connections = dict() #the key is the name of the arc type and the value is a list
							#of nodes that are accessable via that type of connection

	def add_arc(self, arc_type, destination_node):
		'''
		adds the supplied node to the list in the connections dict specified by the arc_type string.
		If such a list does not already exist, then one is first created. If the origin node is found to
		already be a decendent of destination_node, then a error is raised so as to prevent a cyclic graph
		'''
		if not arc_type in self.connections.keys():
			self.connections[arc_type] = list()

		if destination_node.has_descendant(self.name, arc_type):
			raise CyclicArcAttemptedError(self.name, destination_node.name)
		
		self.connections[arc_type].append(destination_node)

	def remove_arc(self, arc_type, destination_node_name):
		'''
		if it exists, node destination_node_name is removed from this nodes list.
		raises an InvalidArcTypeError if this node has no connections type arc_type
		raises a NodeNotFoundError if there is no node destination_node_name in this
		node's arc_type list
		'''
		if not arc_type in self.connections.keys():
			raise InvalidArcTypeError(self.name, arc_type)
		if not destination_node_name in self.connections[arc_type]:
			raise NodeNotFoundError(destination_node_name)



	def has_descendant(self, node_name, arc_type):
		'''
		recursively checks to see if this node is connected to another node
		via a certain arc type
		'''
		if not arc_type in self.connections.keys():
			return False

		for node in self.connections[arc_type]:
			if node.name == node_name:
				return True
			node.has_descendant(node_name, arc_type)

		#if it gets through all of the nodes in the list and hasn't returned true, then the node does
		#not have node_name as a descendant
		return False

	def to_string(self, long_or_short_bool):
		result = "    " + type(self).__name__ + ": " + self.name + "\n"

		for arc_type in self.connections.keys():
			result += "        " + arc_type + ": "
			if long_or_short_bool:
				result += "\n"
				for node in self.connections[arc_type]:
					result += "            " + node.name + "\n"
			else:
				result += str(len(self.connections[arc_type])) + "\n"
		return result

	def decendent_tree_string(self, branch_arc_type, spacer):
		result = spacer + self.name + "\n"
		spacer += "|   "
		if branch_arc_type in self.connections.keys():
			for node in self.connections[branch_arc_type]:
				result += node.decendent_tree_string(branch_arc_type, spacer)

		return result

#custon exceptions

#base exception class
class Error(Exception):
	pass

class NodeNotFoundError(Error):
	def __init__(self, node_name):
		print("Tried to access node %s, but node does not exist" % node_name)

class InvalidArcDestinationError(Error):
	def __init__(self, destination):
		print("Tried to add an arc to an object of type %s instead of a Node" % str(type(destination)))

class RepeatNodeExceptionError(Error):
	def __init__(self, node_name, graph_title):
		print("Tried to add node %s to graph %s, but node already exists" % (node_name, graph_title))

class RepeatArcExceptionError(Error):
	def __init__(self, origin_node_name, destination_node_name, graph_title):
		print("Tried to add arc between origin node %s and destination node %s in graph %s, but arc already exists" % (origin_node_name, destination_node_name, graph_title))

class InvalidArcTypeError(Error):
	def __init__(self, node_name, arc_type):
		print("Origin node %s is not connected to any nodes via an arc of type %s" % (node_name, arc_type))

class CyclicArcAttemptedError(Error):
	def __init__(self, origin_node_name, destination_node_name):
		print("Tried to add arc from node %s to node %s, but %s is a descendant of %s" % (origin_node_name, destination_node_name, origin_node_name, destination_node_name))	

