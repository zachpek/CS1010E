def rna_segment(rna):
    init_codons = ['UU', 'UG']
    term_codons = ['AC', 'AA']
    len_rna = len(rna)
    i = 0
    while rna[i : i + 2] not in init_codons and i + 1 < len_rna:
        i += 1
    if rna[i : i + 2] not in init_codons:
        return ''
    j = i
    while rna[j : j + 2] not in term_codons and j + 1 < len_rna:
        j += 2
    if rna[j: j + 2] not in term_codons:
        return ''
    return rna[i: j + 2]

def poly_property(poly):
    acidic_aas = ('F', 'P', 'Q')
    basic_aas = ('M', 'A', 'C', 'R')
    polar_aas = ('S', 'T', 'Y')
    nonpolar_aas = ('L', 'O')
    acidic_aa_count = 0
    basic_aa_count = 0
    polar_aa_count = 0
    nonpolar_aa_count = 0
    for aa in poly:
        if aa in acidic_aas:
            acidic_aa_count += 1
        elif aa in basic_aas:
            basic_aa_count += 1
        elif aa in polar_aas:
            polar_aa_count += 1
        elif aa in nonpolar_aas:
            nonpolar_aa_count += 1
    if acidic_aa_count > basic_aa_count:
        return 'Acidic'
    if acidic_aa_count < basic_aa_count:
        return 'Basic'
    if polar_aa_count > nonpolar_aa_count:
        return 'Polar'
    return 'Neutral'

def auspicious_number(n, bad):
    return len([i for i in range(10 ** (n - 1), 10 ** n) if all(int(j) not in bad for j in str(i))])
