from toolkit import DnaToolKit

tk = DnaToolKit()
dna = tk.generate_dna_sequence(10)
dna = tk.validate_sequence(dna)
print(tk.nucleotide_frequency(dna))
