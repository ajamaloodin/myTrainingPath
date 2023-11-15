def to_rna(dna_strand):

    dna_strand = dna_strand.upper()

    nucleotide = 'GCTA'
    rna = 'CGAU'

    mytable = str.maketrans(nucleotide, rna)

    translation = dna_strand.translate(mytable)

    return(translation)