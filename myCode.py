import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def align(genome_seq, gene_seq, genome_name, gene_name, match, mismatch, open_gap, extend_gap):
    alignments = pairwise2.align.globalms(genome_seq, gene_seq, match, mismatch, open_gap, extend_gap, penalize_end_gaps=(False, False), one_alignment_only=True)
    alignment = format_alignment(*alignments[0])
    with open("alignment_"+genome_name+gene_name, "w") as file:
       file.write(alignment)
    enterIndex = alignment.find("\n")
    firstSeq = alignment[0:enterIndex]
    secondSeq = alignment[2*enterIndex+2:3*enterIndex+2]
    for i in range(len(secondSeq)):
        if secondSeq[i]!="-":
            break
    startIndex = i
    for i in range(len(secondSeq)-1, 0, -1):
        if secondSeq[i]!="-":
            break
    endIndex = i
    gene = firstSeq[startIndex: endIndex+1].replace("-","")
    with open("myGene_"+genome_name+gene_name, "w") as file:
       file.write(gene)


def open_fasta(filename):
    gene = ""
    with open(filename) as file:
        data = file.readlines()
        for i in range(len(data) - 1):
            gene += data[i+1]
    gene = gene.replace("\n", "")
    return gene

if __name__ == "__main__":
    genomeName = sys.argv[1]
    geneName = sys.argv[2]
    genome = open_fasta(genomeName+"_genome.fasta")
    gene = open_fasta(geneName+".txt")
    match = 1
    mismatch = -1
    open_gap = -1
    extend_gap = -1
    align(genome, gene, genomeName, geneName, match, mismatch, open_gap, extend_gap)
