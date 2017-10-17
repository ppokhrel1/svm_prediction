
import pandas as pd

#df = pd.read_csv('1AT0.mat', sep=" ", )
#print(df.values)

def get_pssm(pdb_id):
  
  with open("new_dataset/PSSM/" + pdb_id +  ".mat", "r") as f:
    # print(f.readlines())
    array = f.readlines()[2:]
    residues = [ x for x in array[0].strip().split(" ") if x != '' ]
    #print(residues)
    #print(pdb_id)
    my_pssm = []
    for line in array[1:]:
      pssm_column = {}
      matrix = [ x.strip() for x in line.split(" " ) if x != ''  ]
      # we only need the first element
      element = matrix
      #print(matrix)
      #residue = element[1]
      if len(element) > 25:
        residue = element[1]
        
        
        pssm_scores = sanitize(element[2:22] ) [:20]
        for x in range(len(pssm_scores)  ):
          try:
            pssm_column[residues[x]] = int(pssm_scores[x] )
          except:
            print(pssm_scores[x] )    
        if pssm_column != {}:
          my_pssm.append((residue, pssm_column)   )
    return my_pssm

def sanitize(pssm):
  y = [ x.split("-") if len(x) > 2 else x for x in pssm]
  merged = []
  for m in y:
      if isinstance(m, list):
        for x in range(len(m)):
          if x != 0 and m[x] != "":
            merged.append("-" + m[x])
          elif x == 0 and m[x] != "":
            merged.append( m[x] )
      else:
        merged.append(m)
  return merged

