'''
Author : Anil Sharma
version: 0.1
Date   : 03/02/2022
Desc   : This script tests the city Population and Age
'''

###########Insalling Module ###################################################

import subprocess


def install(name):
    subprocess.call(['pip', 'install', 'sparqlwrapper'])


# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/
##############################################################

import sys
from SPARQLWrapper import SPARQLWrapper, JSON
# import pandas as pd
from collections import OrderedDict
from unittest import TestCase


class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def ask(self, question: str):

        #  debug
        # import pdb
        # pdb.set_trace()

        if 'population' in question:
            city = question.replace("what is the population of ", "", 1)
            return self.get_city_poputlation(city)
        elif 'old' in question:
            person = question.replace("how old is ", "", 1)
            return self.get_age(person)
        else:
            return

    def get_age(self, person):
        person_data = {}
        person_query = """#List of countries by age of the head of government
                #added by Jura1, rev. 2016-11-08
                SELECT DISTINCT ?hgovernmentLabel ?age  
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
        results = self.get_results(person_query)
        for item in results['results']['bindings']:
            person_query[item['hgovernmentLabel']['value']
            ] = item['age']['value']

        return person_data[person]
        # pass

    def get_city_poputlation(self, city):
        city_query = """#Largest cities of the world
            #defaultView:BubbleChart
            SELECT DISTINCT ?cityLabel ?population
            WHERE
            {
            ?city wdt:P31/wdt:P279* wd:Q515 .
            ?city wdt:P1082 ?population .
            ?city wdt:P625 ?gps .

            SERVICE wikibase:label {
            bd:serviceParam wikibase:language "en" .
            }
            }
            ORDER BY DESC(?population) LIMIT 1000"""

        city_data = {}
        results = self.get_results(city_query)
        for item in results['results']['bindings']:
            city_data[item['cityLabel']['value']
            ] = item['population']['value']

        return city_data[city]

    def get_results(self, query):
        user_agent = "WDQS-example Python/%s.%s" % (
            sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(self.endpoint, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()


class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on

        self.assertEqual('8908081', guru.ask(
            'what is the population of London'))
        self.assertEqual('2165423', guru.ask(
            'what is the population of Paris'))
        # self.assertEqual('68', guru.ask('how old is Tony Blair'))
        # note Sometime person_query wiki url gives https error(get post issue). This is upstream data issue
        # self.assertEqual('75', guru.ask('how old is trump'))


#
if __name__ == "__main__":
    t = TestGuru()
    t.test_ask()
