#!/usr/bin/env pypy3

class Entry:
	entry_dict = dict()

	def __init__(self, short_name, long_name, type_, tags=[], description=None):
		self.short_name
		self.long_name = long_name
		self.type_ = type_
		self.tags = Tag_list(tags)
		self.description = description

		Entry.entry_dict[short_name] = self

	def short_to_string(self):
		result = short_name + " (" + long_name + ")\n"

		return result

class Tag_list(list):
	def append(self, new):
	#appends the new category to the list and recursively adds its parents
		super().append(new)
		while new.parent:
			super().append(new.parent)
			new = new.parent


class Category:
	category_dict = dict()
	top_level_categories = list()

	def __init__(self, title, parent=None):
		#title must be unique as it is used as the key in the class level
		#categories dictionary. If no parent is given, the category is 
		#treated as a top level category
		if len(title) >= 1: #first letter upper case, rest of word lower case
			self.title = title[0].upper()
			if len(title) >= 2:
				self.title += title[1:].lower()

		self.parent = parent
		self.children = list()
		self.entries = list()

		Category.category_dict[title] = self

	@property
	def parent(self):
		return self._parent
	
	@parent.setter
	def parent(self, parent):
		if parent == None:
			Category.top_level_categories.append(self)
		else:
			parent.children.append(self)
		self._parent = parent

	def add_entry(self, entry):
		#adds the entry to the categories list of entries in the correct alphabetical 
		#location based on the short_name and recursively adds it
		#to its parent's list of entries(if it has a parent)
		self.entries.append(entry)
		self.entries.sort(compare)

		if self.parent:
			self.parent.add_entry(entry)


	def print_tree(self, category):
		pass

	def to_string(self):
		result = "Category:" + self.title + "\n\n"
		result +=" Entries:\n"
		for entry in self.entries:
			result += "\t\t" + entry.short_to_string()

		return result


	def get_num_entries(self):
		len(entries)

	def get_num_children(self):
		pass

#comparator function for sorting a category's entry list
def compare(a,b):
	return (a.short_name > b.short_name) - (a.short_name < b.short_name)


class Program:
	def __init__(self):
		pass





if __name__ == "__main__":
	pass

