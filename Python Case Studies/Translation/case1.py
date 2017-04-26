inputfile = "dna.txt"

def read_seq(inputfile, cds_start=0, cds_stop=0, mod_crop=1):
    with open(inputfile, "r") as f:
        seq = f.read()
    
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    crop = len(seq) % mod_crop
    seq = seq[0:len(seq)-crop]
    if cds_start > 0 and cds_stop > cds_start:
        cds_start -= 1
        seq = seq[cds_start:cds_stop]
    return seq
    
    
def translate(seq):
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""    
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]  
    else:
        pass
    
    return protein

NM207618_2 = read_seq(inputfile, cds_start=21, cds_stop=938)
translated_protein = translate(NM207618_2)
if translated_protein[-1] == "_":
    NM207618_2 = NM207618_2[0:len(NM207618_2)-3]
    translated_protein = translate(NM207618_2)
prt = read_seq("protein.txt")     
print("Comparison of translated sequence and downloaded sequence: ", translated_protein == prt)

    