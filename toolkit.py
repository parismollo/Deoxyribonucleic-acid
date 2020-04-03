from typing import List
import random


nucleotide = str


class DnaToolKit:
    nucleotides: List[nucleotide] = ['A', 'C', 'G', 'T']

    def validate_sequence(self, dna_sequence: str) -> str:
        sequence = dna_sequence.upper()
        for e in sequence:
            if e not in self.nucleotides:
                raise TypeError(f"Element '{e}' is not a nucleotide")
        return sequence

    def generate_dna_sequence(self, sequence_legnth: int = 20) -> str:
        return ''.join(
                random.choice(self.nucleotides)
                for e in range(sequence_legnth)
            )

    def nucleotide_frequency(self, dna_sequence: str) -> dict:
        nuc_freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for n in dna_sequence:
            try:
                nuc_freq[n] += 1
            except KeyError:
                print(f'Key {n} not found')
        return nuc_freq
