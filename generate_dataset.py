from bioservices import QuickGO
import pickle
from pssm_helpers import *
from map_pdb_uniprot import *



data = load_data("Supp-S1/binding_fasta.txt", "Supp-S1/nonbinding_fasta.txt")
dataset = []
for x in data:
  x = x[0].split(":")[0]
  #print(x)
  value = []
  try:
    value = load_terms(x)
  except:
    print("Hello")  
  print(value)
  dataset.append([x, value])
print(dataset)
with open('new_dataset/generated_dataset.pickle', 'wb') as handle:
        pickle.dump(dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
        #handle.write(str(all_terms))


