import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import editdistance

def editDistance(genome1, genome2):
    score = editdistance.eval(genome1, genome2)
    print(score)
    #
    with open("edit_distance_"+a+b, "w") as file:
       file.write(str(score))
    # firstSeq = alignment[0:enterIndex]
    # secondSeq = alignment[2*enterIndex+2:3*enterIndex+2]
    # for i in range(len(secondSeq)):
    #     if secondSeq[i]!="-":
    #         break
    # startIndex = i
    # for i in range(len(secondSeq)-1, 0, -1):
    #     if secondSeq[i]!="-":
    #         break
    # endIndex = i
    # gene = firstSeq[startIndex: endIndex+1].replace("-","")
    # with open("myGene_"+genome_name+gene_name, "w") as file:
    #    file.write(gene)


def open_fasta(filename):
    gene = ""
    with open(filename) as file:
        data = file.readlines()
        for i in range(len(data) - 1):
            gene += data[i+1]
    gene = gene.replace("\n", "")
    return gene

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    genome_1 = open_fasta(a+"_genome.fasta")
    genome_2 = open_fasta(b+"_genome.fasta")
    editDistance(genome_1, genome_2)