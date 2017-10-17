from bioservices.apps.fasta import FASTA
from bioservices import UniProt
from bioservices import pdb
from Bio import AlignIO
from Bio.Align import AlignInfo
from pssm_helpers import *
from Bio import *
from Bio.motifs.matrix import *


import open_file
#f= FASTA()
#f.load("P43403")
#acc = f.accession
#fasta = f.fasta

#u = UniProt()
#akt1 = u.retrieve("P31749", "fasta")
#akt2 = u.retrieve("P31751", "fasta")

#from Bio.Align import MultipleSeqAlignment
#from Bio.Alphabet import *
#from Bio.Seq import Seq
#from Bio.SeqRecord import SeqRecord
#import open_file
#to run blast
#from Bio.Blast import NCBIWWW, NCBIXML
#from Bio import motifs
def get_pssm(fasta_file):
    #alignment = MultipleSeqAlignment(
    #          [SeqRecord(Seq(fasta, Gapped( generic_protein ) ), id ="Human")  ]
    #          )
    alignment = AlignIO.read(fasta_file, "fasta" )
    #sequence = [
    #  Seq(fasta, IUPAC.extended_protein )
    #]
    summary_align = AlignInfo.SummaryInfo(alignment)
    #print(summary_align.information_content() )
    consensus = summary_align.dumb_consensus( )
    my_pssm = summary_align.pos_specific_score_matrix(consensus, chars_to_ignore = ["N", "-"] )
    #print(my_pssm.pssm)
    #print(len(my_pssm.pssm) )
    return my_pssm.pssm


#F = FASTA()
#p = pdb.PDB()
#u.mapping("ACC", "PDB_ID", query=x)
import helpers
import pickle
import os
import os.path

def save_training_sample():    
    data = load_data("Supp-S1/binding_fasta.txt", "Supp-S1/nonbinding_fasta.txt")
    ## use fasta sequence from binding and non-binding dataset and create
    inputs = []
    targets = []
    
    go_data = helpers.parse_dataset("new_dataset/generated_dataset.pickle", [x[0].split(":")[0] for x in data])
    go_scores = dict(go_data)
    for datum in data:
      path = "new_dataset/PSSM/" + datum[0].split(":")[0]  +  ".mat"
      if (not os.path.isfile(path) ):
          continue
      #print( map_pdb_to_uniprot(x[0]) )
      my_pssm = []
      my_pssm = open_file.get_pssm(datum[0].split(":")[0] )
      #print(my_pssm)
      array = []
      #print( len(datum[1]))
      array = [ [ 0 for x in range( 20  ) ] for y in range( len(my_pssm )) ]
      targets.append(datum[2])
      for x in  range(len(my_pssm)):
          value = my_pssm[x]
          #print( len(value) )
          mylist = sorted(list(value[1].keys()) )
          #print(mylist )
          #print(value)
          for y in range(len(mylist ) ):
            #print(x, y)
            #print(array[x][y])
            print(x, y)
            print(len(my_pssm), " ", len(array )  )
            array[x][y] = value[1] [ mylist[y] ]
      #array = [[
      #ifor x in 
      #go_scores = helpers.parse_dataset("generated_dataset.pickle",[datum[0].split(":")[0]] )[0][1]
      go_score = go_scores[datum[0].split(":")[0] ]
      value = go_score.tolist() + feature_space(array)
      #value = feature_space(array)
      inputs.append(value) 
    return inputs, targets
        
import pickle
def training_sample():
  with open("generated_dataset.pickle", "rb") as f:
    inputs, outputs = pickle.load(f)
    return inputs, outputs

if __name__ == "__main__":
  with open("generated_dataset.pickle", "wb" ) as f:
    inputs, outputs = save_training_sample()
    pickle.dump([inputs, outputs], f )
