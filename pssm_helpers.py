import itertools
import random
from Bio import SeqIO

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC


#LG is some predefined constant
LG = 5
def pssm_sdt(matrix):
    #construct empty matrix of size 20 * LG
    pssm_sdt = [[0 for x in range( 20 )] for y in range(LG) ]
    #loop through all i's i.e amino acids
    for lg in range(0, LG):
        for i in range(len(matrix[1] ) ): #number of features
            pssm_sdt[lg][i] = 0
            for j in range(0, len(matrix) - lg):
                pssm_sdt[lg][i] += matrix[j][i] * matrix[j + lg][i] / (len(matrix) - lg)
    return pssm_sdt


#pssm distance transformation of different proteins
def pssm_ddt(matrix):
    #lets first calculate a permutations of all indexes in the matrix
    #we can calculate indices for pssm_ddt later on
    a = [x for x in range(20 )] # 20 is total number of amino acids
    #generates matrix of size 380
    indices_matrix = list(itertools.permutations(a, 2)) #combinations of two residues

    #empty matrix
    pssm_ddt = [[0 for x in range(19 * 20 )] for y in range(LG)]

    for lg in range(0, LG):
        for i1 in range(len(matrix[1])): #number of features
            for i2 in range(len(matrix[1])) :
                if i1 == i2:
                    continue
                index = indices_matrix.index((i1, i2))
                for j in range(0, len(matrix) - lg):
                    pssm_ddt[lg][index] += matrix[j][i1] * matrix[j + lg][i2] / (len(matrix) - lg)
    return pssm_ddt


def feature_space(matrix):
    #pssm_sdt1 = pssm_sdt(matrix)
    pssm_ddt1 = []
    pssm_ddt1 = [item for sublist in  pssm_ddt(matrix) for item in sublist]
    pssm_sdt1 = [item for sublist in pssm_sdt(matrix) for item in sublist]
    #pssm_ddt1 = [item for sublist in pssm_ddt(matrix) for item in sublist]
    returnVal = []
    #for x in range(LG):
    #    returnVal.append(pssm_sdt1[x] + pssm_ddt1[x])
    #return [item for sublist in returnVal for item in sublist]
    return pssm_sdt1 + pssm_ddt1 # + [random.random() for x in range(300)]
matrix = [[ random.random() for x in range(20)] for x in range(30) ]

import random
from helpers import *
#random.seed(5000)
def load_data(positive, negative):
    dataset = []
    returnval = []
    with open(positive) as file1:
        content2 = file1.read().replace("\n", " ").split(">")
        content = [a.split(" ", 1) for a in content2]
        for a in content[1:]:
          if a != "" and a!= [""] and a != []:
            returnval.append([a[0], a[1].replace(" ", " "), 1])

    with open(negative) as file2:
      content2 = file2.read().replace("\n", " ").split(">")
      content = [a.split(" ", 1) for a in content2][:1000]
      for a in content[1:]:
        if a != "" and a != [""] and a != []:
          returnval.append([a[0], a[1].replace(" ", ""), 0])
    random.shuffle(returnval, random.random)
    return returnval


if __name__ == "__main__":
    import helpers
    #print feature_space(matrix)[1]
    #print len(list(itertools.permutations([x for x in range(20)], 2) ))
    #dataset = []
    #with open("positive.txt", "r") as positive:
    data = load_data("Supp-S1/binding-0.txt", "Supp-S1/non-binding.txt") 
    print(data)
    for x in data:
      print( x )

    import pickle
    #print(helpers.read_files("training_file/generated_dataset.pickle", None))
    with open("training_file/training_dataset.pickle", "rb") as f:
      a = pickle.load(f)
      print(a)




