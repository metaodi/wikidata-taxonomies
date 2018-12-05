# -*- coding: utf-8 -*-

# URL of IPTC controlled vocabulary (CV): http://cv.iptc.org/newscodes/mediatopic/?format=json&lang=de
# json-ld

# swissinfo uses IPTC on 3 levels

from rdflib import Graph
from rdflib.namespace import Namespace, RDF, XSD, SKOS, RDFS
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from pprint import pprint

g = Graph()

g.parse("http://cv.iptc.org/newscodes/mediatopic/?format=rdfxml&lang=de")

# get top concepts with 2 levels down (3 levels total)
ref = next(g.subjects(RDF.type, SKOS.ConceptScheme))

iptc = Node("IPTC") 
for top_ref in g.objects(ref, SKOS.hasTopConcept):
    top = Node(unicode(g.preferredLabel(top_ref)[0][1]), parent=iptc)
    for sub_ref in g.objects(top_ref, SKOS.narrower):
        sub = Node(unicode(g.preferredLabel(sub_ref)[0][1]), parent=top)
        for subsub_ref in g.objects(sub_ref, SKOS.narrower):
            if len(g.preferredLabel(subsub_ref)) > 0:
                subsub = Node(unicode(g.preferredLabel(subsub_ref)[0][1]), parent=sub)

for pre, fill, node in RenderTree(iptc):
    print("%s%s" % (pre, node.name))
# DotExporter(iptc).to_picture("iptc.png")
# if __name__ == '__main__':
#     arguments = docopt(__doc__, version='Naval Fate 2.0')
#     print(arguments)
