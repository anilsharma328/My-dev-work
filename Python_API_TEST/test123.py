# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON ,POST

endpoint_url = "https://query.wikidata.org/sparql"

query = """#List of countries by age of the head of government
#added by Jura1, rev. 2016-11-08
SELECT DISTINCT ?age ?country ?countryLabel ?hgovernment ?hgovernmentLabel
{
  ?country wdt:P31 wd:Q3624078 .
  FILTER NOT EXISTS {?country wdt:P31 wd:Q3024240}
  ?country p:P6 ?statement .    
  ?statement ps:P6 ?hgovernment .
  ?country wdt:P6 ?hgovernment .
  FILTER NOT EXISTS { ?statement pq:P582 ?x } 
  ?hgovernment wdt:P569 ?dob . BIND(YEAR(now())-YEAR(?dob) as ?age)
  FILTER(?age>=65)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
ORDER BY DESC(?age)"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(POST)
    #return sparql.query()
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
