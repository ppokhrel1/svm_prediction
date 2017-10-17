import requests
import xmltodict
import json


url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<orgPdbQuery>

<version>B0907</version>

<queryType>org.pdb.query.simple.ExpTypeQuery</queryType>

<description>Simple query for a list of PDB IDs (1 IDs) : 3I5F</description>

<structureIdList>{}</structureIdList>

</orgPdbQuery>

"""

def load_terms(pdb_id):
  myqueryText = queryText.format(pdb_id)
  #req = requests.get(url, data=myqueryText)
  #print( req.text)
  #print( req.text )
  req = requests.get(url
  + " /pdb/rest/goTerms?structureId=" + pdb_id)
  print(req.text) 
  json_term =  json.dumps(xmltodict.parse(req.text ) ) 
  terms = [a["@id"] for a in json.loads(json_term)['goTerms']["term"]  ]
  return terms


#print( load_terms("1ADU" ) )

