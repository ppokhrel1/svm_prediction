
import pandas as pd

#df = pd.read_csv('1AT0.mat', sep=" ", )
#print(df.values)
with open("1AT0.mat", "r") as f:
 # print(f.readlines())
 array = f.readlines()[2:]
 residues = [ x for x in array[0].strip().split(" ") if x != '' ]
 print(residues)
 my_pssm = []
 for line in array[1:]:
    pssm_column = {}
    matrix = [ x.strip() for x in line.split(" " ) if x != ''  ]
    # we only need the first element
    element = matrix
    #residue = element[1]
    if len(element) > 25:
      residue = element[1]
      pssm_scores = element[2:22]
      for x in range(len(pssm_scores)  ):
        pssm_column[residues[x]] = int(pssm_scores[x] )
    if pssm_column != {}:
      my_pssm.append((residue, pssm_column)   )
    #print(pssm_scores   )

print(my_pssm ) 



