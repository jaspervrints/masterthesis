from faker import Faker
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import FOAF, RDF

fake = Faker()
Faker.seed(0)

NUMBER_OF_ELEMENTS = 200000

g = Graph()
g.bind("foaf", FOAF)

n = Namespace("http://example.org/people/")

for i in range(NUMBER_OF_ELEMENTS):
    name = Literal(fake.name())
    age = Literal(fake.date_of_birth())
    name_n = URIRef("http://example.org/people/"+name.replace(" ","-"))
    g.add((name_n, RDF.type, FOAF.Person))
    g.add((name_n, FOAF.name, name))
    g.add((name_n, FOAF.age, age))

g.serialize(destination=f"dataset_{NUMBER_OF_ELEMENTS}.ttl")