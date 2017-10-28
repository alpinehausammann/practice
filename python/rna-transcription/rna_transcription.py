from string import ascii_uppercase


def to_rna(dna_strand):
    
    dna_to_rna = {"A":"U","C":"G","G":"C","T":"A"}
    rna_strand = ""
    
    for letter in str(dna_strand):
        try:
            rna_strand += dna_to_rna[letter]
        except KeyError:
            return ""
    print(rna_strand)
    return rna_strand

