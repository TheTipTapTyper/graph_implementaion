#!/usr/bin/env pypy3

from graphs import *

x = DirectedACyclicGraph("Test Graph")

x.add_node(Node("Fields of Study"))

x._make_and_add_from_list("Fields of Study", "Sub-Categories", ["Science", "Math", "Art", "History", "Medicin"])


x._make_and_add_from_list("Science", "Sub-Categories", ["Biology", "Chemistry", "Physics", "Computer Science"])
x._make_and_add_from_list("Medicin", "Sub-Categories", ["Anatomy", "Pharmacology", "Physical Therapy", "EMT", "Psychology"])
x._make_and_add_from_list("Math", "Sub-Categories", ["Algebra", "Trig", "Calculus", "Discrete", "Probability"])
#x._make_and_add_from_list("Art", "Sub-Categories", ["Science", "Math", "Art", "History"])
#x._make_and_add_from_list("History", "Sub-Categories", ["Science", "Math", "Art", "History"])

x._make_and_add_from_list("Algebra", "Sub-Categories", ["Algebra 1", "Algebra 2", "Linear Algebra"])
x._make_and_add_from_list("Calculus", "Sub-Categories", ["Calculus 1", "Calculus 2", "Calculus 3", "Lambda Calculus"])
x._make_and_add_from_list("Biology", "Sub-Categories", ["Neuro-Biology", "Micro-Biology", "Evolutionary Biology"])
x._make_and_add_from_list("Physics", "Sub-Categories", ["Astro Physics", "Nano Physics", "High-Engergy Physics", "Particle Physics"])







#x.add_arc("algebra", "Super-Categories", "math")

#x.add_arc("trig", "Super-Categories", "math")

#x.add_arc("algebra 1", "Super-Categories", "algebra")

#x.add_arc("algebra 2", "Super-Categories", "algebra")

#print(type(x.nodes["math"]))

#print(x.to_string(True))

#print(x.to_string(False))

print(x.decendent_tree_string("Fields of Study", "Sub-Categories"))

