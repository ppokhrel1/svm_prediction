import Bio
from Bio.PDB import PDBList
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Alphabet import *
from Bio.Blast import *


'''Selecting structures from PDB'''
pdbl = PDBList()
PDBlist2=['4B97','4IPH','4HNO','4HG7','4IRG','4G4W','4JKW','4IPC','2YPM','4KEI']
for i in PDBlist2:
    #pdbl.retrieve_pdb_file(i,pdir='PDB')
    pass

input_sequence = "INFYGELVDLGVKEKLIEKAGAWYSYKGEKIGQGKANATAWLKDNPETAKEIEKKVRELLLSN"
psi_blast = NCBIWWW.qblast("blastp", "refseq_protein", input_sequence,
service="psi")
psi_blast = NCBIXML.parse(psi_blast)
print(psi_blast)
#for x in psi_blast.description:
#  print(x)
for record in psi_blast:
    id_query = record.alignments[0].hit_id
    print(id_query)
E_VALUE = 0.04
for alignment in psi_blast.alignments:
    for hsp in alignment.hsps:
      if (hsp.expect < E_VALUE):
        print('****Alignment****')
        print('sequence:', alignment.title)
        print('e value:', hsp.expect)
        print(hsp.query[0:75] + '...')
        print(hsp.match[0:75] + '...')
        print(hsp.sbjct[0:75] + '...')
#print(psi_blast.MultipleAlignmenti().to_generic(generic_protein)  )


