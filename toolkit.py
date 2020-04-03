from typing import List

nucleotide = str


class DnaToolKit:
    nucleotides: List[nucleotide] = ['A', 'C', 'G', 'T']

    def validate_sequence(self, dna_sequence: str):
        sequence = dna_sequence.upper()
        for e in sequence:
            if e not in self.nucleotides:
                raise TypeError(f"Element '{e}' is not a nucleotide")
        return sequence
