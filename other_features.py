

def get_base_counts(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        counts[base] += 1
    return counts

def get_base_frequencies_v1(dna):
    counts = get_base_counts(dna)
    return {base: count*1.0/len(dna)
        for base, count in counts.items()}

def get_base_frequencies_v2(dna):
    return {base: dna.count(base)/float(len(dna))
        for base in 'ATGC'}
dna = "ACTGTAGAGATAGATG"
frequencies = get_base_frequencies_v2(dna)
print(dna, " frequency: ", frequencies)









