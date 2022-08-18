from faker import Faker
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import FOAF, RDF

# fake = Faker()

# print(fake.name())
g = Graph()
g.bind("foaf", FOAF)

n = Namespace("http://example.org/people/")

name = Literal("Bob")
age = Literal(24)

g.add((n.bob, RDF.type, FOAF.Person))
g.add((n.bob, FOAF.name, name))
g.add((n.bob, FOAF.age, age))

g.serialize(destination="out.ttl")