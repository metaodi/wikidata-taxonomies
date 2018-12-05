# -*- coding: utf-8 -*-

# URL of IPTC controlled vocabulary (CV): http://cv.iptc.org/newscodes/mediatopic/?format=json&lang=de
# json-ld

# swissinfo uses IPTC on 3 levels

from rdflib import Graph
from rdflib.namespace import Namespace, RDF, XSD, SKOS, RDFS
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from pprint import pprint

namespaces = {
    'skos': SKOS,
}

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


# user need taxonomy
# extract from ASO, swissinfo site, facebook

needs = Node(u"User needs") 
out = Node(u"Auswandern", parent=needs) 
Node(u"Auswandern in einen EU/EFTA Staat", parent=out) 
work = Node(u"Arbeiten", parent=out) 
Node(u"Stellensuche im Ausland", parent=work) 
Node(u"Bewerbung", parent=work) 
Node(u"Arbeitsmarkt", parent=work) 
Node(u"Berufspraktika und Trainees", parent=work) 
Node(u"Selbstständig Erwerbende", parent=work) 


live = Node(u"Leben im Ausland", parent=needs) 
Node(u"Stellensuche im Ausland", parent=live) 

banks = Node("Banken", parent=live)
Node(u"BCGE", parent=banks)
Node(u"BCV", parent=banks)
Node(u"Credit Suisse", parent=banks)
Node(u"PostFinance", parent=banks)
Node(u"Raiffeisen", parent=banks)
Node(u"TKB", parent=banks)
Node(u"UBS", parent=banks)
Node(u"Valiant", parent=banks)
Node(u"Zürcher Kantonalbank", parent=banks)

politics = Node(u"Politische Rechte", parent=live)
Node(u"Wählen und Abstimmen", parent=politics)
Node(u"Anmeldeformular", parent=politics)
Node(u"Schwierigkeiten bei Abstimmungen", parent=politics)

insurance = Node(u"Sozialversicherungen", parent=live)
Node(u"AHV / IV", parent=insurance)
Node(u"Vorsorge", parent=insurance)
Node(u"Krankenversicherung", parent=insurance)

help = Node(u"Hilfe im Ausland", parent=live)
Node(u"Sozialhilfe", parent=help)
Node(u"Wohltätige Schweizer Gesellschaften", parent=help)

military = Node(u"Militärdienst", parent=live)
Node(u"Vor der Abreise", parent=military)
Node(u"Meldepflicht im Ausland", parent=military)
Node(u"Militärpflichtersatz", parent=military)
Node(u"Junge Auslandschweizer", parent=military)
Node(u"Studium in der Schweiz", parent=military)
Node(u"Freiwilliger Militärdienst", parent=military)
Node(u"Militärdienst in fremden Armeen", parent=military)
Node(u"Kurzaufenthalt in der Schweiz", parent=military)
Node(u"Doppelbürger", parent=military)

rights = Node(u"Bürgerrecht", parent=live)
Node(u"Schweizer(in) durch Geburt", parent=rights)
Node(u"Schweizer(in) durch Wiedereinbürgerung", parent=rights)
Node(u"Schweizer(in) durch Heirat", parent=rights)
Node(u"Doppelbürgerrecht", parent=rights)

id = Node(u"Pass, IDK", parent=live)
Node(u"Schweizer Pass", parent=id)
Node(u"Identitätskarte", parent=id)

tax = Node(u"Steuern", parent=live)
Node(u"Besteuerung von Renten aus der 2. Säule", parent=tax)
Node(u"Besteuerung von Kapitalauszahlungen aus der 2. Säule", parent=tax)
Node(u"Doppelbesteuerungsabkommen", parent=tax)
Node(u"Automatischer Informationsaustausch (AIA)", parent=live)
Node(u"Gesetzestexte", parent=live)

faq = Node(u"FAQ", parent=live)
Node(u"E-Voting", parent=faq)
Node(u"Schweizer-Verein", parent=faq)
Node(u"Nachlass", parent=faq)
Node(u"Testament", parent=faq)
Node(u"Schweizer Fahrausweis", parent=faq)
Node(u"Fundsachen", parent=faq)
Node(u"Zoll", parent=faq)
Node(u"Schweizer Fernsehen und Radio", parent=faq)
Node(u"Geburt, Ehe, Todesfall", parent=faq)
Node(u"Öffentlicher Verkehr", parent=faq)
Node(u"Individualverkehr", parent=faq)

back = Node(u"Rückwanderung in die Schweiz", parent=needs) 
Node(u"Jobsuche", parent=back)
Node(u"E.O. Kilcher-Fonds", parent=back)


edu = Node(u"Ausbildung in der Schweiz", parent=needs) 
Node(u"Studieren in der Schweiz", parent=edu)
Node(u"Öffentliche Schulen", parent=edu)
Node(u"Bildungssystem", parent=edu)
Node(u"Forschungstrends", parent=edu)


facts = Node(u"Fakten", parent=needs)
Node(u"Kennzahlen", parent=facts)
Node(u"Wetter/Klima", parent=facts)
Node(u"Geschichte", parent=facts)
Node(u"Währung", parent=facts)
Node(u"Sprachen", parent=facts)


culture = Node(u"Kultur/Reisen", parent=needs)
Node(u"Reisen", parent=culture)
Node(u"Brauchtum und Festivals", parent=culture)
Node(u"Freizeitangebote", parent=culture)
Node(u"Musik", parent=culture)
Node(u"Theater", parent=culture)
Node(u"Architektur", parent=culture)
Node(u"Film", parent=culture)
Node(u"Kulturförderung", parent=culture)

for pre, fill, node in RenderTree(needs):
    print("%s%s" % (pre, node.name))
# DotExporter(needs).to_picture("needs.png")
