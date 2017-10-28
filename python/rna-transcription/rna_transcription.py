from string import ascii_uppercase


def to_rna(dna_strand):
    
    dna_to_rna = {"A":"U","C":"G","G":"C","T":"A","U":"A"}
    rna_strand = ""
    
    for letter in str(dna_strand):
        print(letter)
        if letter.upper() in ascii_uppercase:
            rna_strand += dna_to_rna[letter]
        else:
            continue
    print(rna_strand)
    return rna_strand

