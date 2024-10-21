# Biologists use a sequence of the letters A, C, T, and G to model a genome.

# A gene is a substring of a genome that starts after a triplet ATG and ends before a triplet TAG, TAA, or TGA.
# Furthermore, the length of a gene string is a multiple of 3, and the gene does not contain any of the triplets ATG, TAG, TAA, or TGA.



# Write a function find_genes() that takes as input a genome string, and returns a string with genes, separated by comma, as here:
# "TTT,GGGCGT"

genome = input("Enter a genome string: ")

def find_genes(genome):
    genes = []
    gene = ""
    for i in range(len(genome)):
        if genome[i:i+3] == "ATG":
            gene = ""
            for j in range(i+3, len(genome), 3):
                if genome[j:j+3] in ["TAG", "TAA", "TGA"]:
                    break
                gene += genome[j:j+3]
            if len(gene) % 3 == 0:
                genes.append(gene)
    return ",".join(genes)

if find_genes(genome) == "":
    print("NO GENE FOUND")
else:
    print("GENE FOUND", find_genes(genome))
