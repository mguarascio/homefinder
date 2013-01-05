import db
import requests
from lxml import etree

cities_url = 'http://api.greatschools.org/cities/%s/%s?key=%s'
key = ''

sample_response = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
                    <city>
                        <name>Patchogue</name>
                        <rating>4</rating>
                        <totalSchools>10</totalSchools>
                        <elementarySchools>8</elementarySchools>
                        <middleSchools>4</middleSchools>
                        <highSchools>0</highSchools>
                        <publicSchools>7</publicSchools>
                        <charterSchools>0</charterSchools>
                        <privateSchools>3</privateSchools>
                    </city>"""


def load(state, city):
    r = requests.get(cities_url % (state, city, key))
    print r.text
    xml = r.text.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '') # better way to do this?
    print xml
    root = etree.fromstring(xml)
    schooldata = {'state': state, 'city': city}
    # there is probably a more pythonic way to create this dict?
    for child in root:
        schooldata[child.tag] = child.text
    print schooldata
    #db.insert('towns_database', 'town_schools', schooldata)

if __name__ == '__main__':
    load("NY", "Montauk")
