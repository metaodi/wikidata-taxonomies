# -*- coding: utf-8 -*-

# URL of IPTC controlled vocabulary (CV): http://cv.iptc.org/newscodes/mediatopic/?format=json&lang=de
# json-ld

# swissinfo uses IPTC on 3 levels

import sys
from rdflib import Graph
from rdflib.namespace import Namespace, RDF, XSD, SKOS, RDFS
from anytree import Node, RenderTree, ContRoundStyle
from anytree.exporter import DotExporter

from SPARQLWrapper import SPARQLWrapper, JSON

from pprint import pprint

num = 0
def buildIPTCTree(ref):
    iptc = Node("IPTC", wikidata=None, label='IPTC') 
    for top_ref in g.objects(ref, SKOS.hasTopConcept):
        wd = findWikiData(top_ref)
        
        top = generateNode(top_ref, iptc)
        for sub_ref in g.objects(top_ref, SKOS.narrower):
            sub = generateNode(sub_ref, top)
            for subsub_ref in g.objects(sub_ref, SKOS.narrower):
                if len(g.preferredLabel(subsub_ref)) > 0:
                    subsub = generateNode(subsub_ref, sub)
    sys.stdout.flush()
    return iptc

def generateNode(ref, parent):
    global num
    num = num + 1
    sys.stdout.write("\r%s" % (num*'.'))
    wikidata = findWikiData(ref)
    node = Node(ref, label=unicode(g.preferredLabel(ref)[0][1]), wikidata=wikidata, parent=parent)
    return node

def findWikiData(ref):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

    # get wikidata ref from URI
    iptc_code = ref.replace('http://cv.iptc.org/newscodes/', '')

    # ?item wdt:P5429 ?iptc .
    # FILTER (?iptc IN ("mediatopic/20000735", "productgenre/entertainment" ) )
    # WikiData Property
    sparql.setQuery("""
            SELECT ?item ?itemLabel
            WHERE
            {
               ?item wdt:P5429 "%s" .
               SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
            }
            """ % (iptc_code))
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    if results['results']['bindings']:
        return results['results']['bindings'][0]
    return None

g = Graph()

g.parse("http://cv.iptc.org/newscodes/mediatopic/?format=rdfxml&lang=de")

# get top concepts with 2 levels down (3 levels total)
ref = next(g.subjects(RDF.type, SKOS.ConceptScheme))
iptc = buildIPTCTree(ref)
for pre, fill, node in RenderTree(iptc, style=ContRoundStyle()):
    wd = node.wikidata
    if wd:
        wd = wd['item']['value'].replace('http://www.wikidata.org/entity/', '')

    print("%s%s (%s)" % (pre, node.label, wd))
# DotExporter(iptc).to_picture("iptc.png")
