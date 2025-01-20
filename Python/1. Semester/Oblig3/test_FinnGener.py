import unittest
from FinnGener import find_genes

class TestFindGenes(unittest.TestCase):
    def test_find_genes_with_genes(self):
        genome = "ATGCGATACGCTTGAATGTGAATGTAG"
        expected_result = "GENE FOUND", find_genes(genome)
        self.assertEqual(find_genes(genome), expected_result)

    def test_find_genes_no_genes(self):
        genome = "STRING WITH NO GENES"
        expected_result = "NO GENES FOUND"
        self.assertEqual(find_genes(genome), expected_result)

    def test_find_genes_empty_string(self):
        genome = ""
        expected_result = "NO GENE FOUND"
        self.assertEqual(find_genes(genome), expected_result)

if __name__ == '__main__':
    unittest.main()