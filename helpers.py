import numpy as np
import pickle
codes = {
        'A': '0001',
        'C': '0010',
        'G': '0100',
        'T': '1000',
        'N': '0000'
        }
## maps the codes into binary format and
## then separate them into individual 1s and 0s as mentioned in the paper
def encode_nucleotide(sequence, k = 0.5):
    returnVal = []
    #print( sequence)
    for seq in sequence.decode('UTF-8'):
        #print(seq)
        for value in codes[seq]:
            returnVal.append(int(value))
    for x in range(25 - len(sequence)):
        for value in codes['N']:
            returnVal.append(int(value))
    return [x * k for x in returnVal]


def hybridization_space(trans_factor, tf_binding_factor):
    return np.append(trans_factor, tf_binding_factor ).T


def calculate_similarity(point1, point2):
    return np.dot(point1, point2) / (np.linalg.norm(point1) * np.linalg.norm(point2))


##creates the feature array when given with a hash and total_sample space
def create_features(hash, total_space):
    return_hash = {}
    #print(total_space)
    for key in hash.keys():
        go_terms = hash[key]
        #create an empty array of length equal to total_space
        feature = np.zeros(len(total_space))
        #print( len(total_space) )

        for go_term in go_terms:
            index = total_space.index(go_term)
            feature[index] = 1
        return_hash[key] = feature
    return return_hash


def read_files(tf_file, tf_binding_file):
    dataset = []
    #tf file is pickle
    tf_array = []
    with open(tf_file, "rb") as file:
        #open the dataset file and the nucleotide files and create hashes from both
         tf_array = pickle.load(file)
    myhash = {}
    for element in tf_array:
        #exclude the transcription factors with no go annotations
        if element[1] != [] or element[1] != '' or element[1] != ['']:
            myhash[element[0]] = list(set(element[1] ) )

    #open second file which is text and create
    tf_binding_hash = {}
    if (tf_binding_file != None):
      with open(tf_binding_file, "rb") as file:
          while True:
              line1 = file.readline().strip().upper()
              line2 = file.readline().strip().upper()
              if not line2:
                  break
              tf_binding_hash[line1] = np.array( encode_nucleotide(line2) )
    feature_space = []
    for values in myhash.values():
        for value in values:
            if value not in feature_space:
                feature_space.append(value )
    return create_features(myhash, feature_space ) ,  tf_binding_hash

def parse_dataset_file(tf_file, tf_binding_file, dataset, class_label):
    #print "starting....."
    tf_values, tf_binding_values = read_files(tf_file, tf_binding_file)
    all_data = []
    true_pairs = []
    with open(dataset, "r") as file:
        for line in file:
            for value in line.strip().split("\t"):
                true_pairs.append( value )
    #true_pairs = []
    #with open(dataset, "rb") as file:
    #    for line in file:
    #        for value in line.strip().split("\t"):
    #            true_pairs.append( value )


    return [ [ value, hybridization_space(tf_values[value.split("_")[0]],
        tf_binding_values[value.split("_")[1]]), class_label ] for value in true_pairs]

#tf_file is the pickle file
#dataset_ids is the list of pdb ids
def parse_dataset(tf_file, dataset_ids):
    tf_values, _ = read_files(tf_file, None)
    all_data = []
    true_pairs = []
    #with open(dataset, "r") as file:
    #    for line in file:
    #        for value in line.strip().split("\t"):
    #          true_pairs.append( value )
    #true_pairs = []
    return [ [value, hybridization_space(tf_values[value], [])] for value in dataset_ids ]
    

if __name__ == "__main__":
    print( read_files("test_dataset/generated_dataset.pickle",
    "test_dataset/nucleotide_sequence.txt")  )

    print(read_files("test_dataset/generated_dataset.pickle", None))
