from Bio import SeqIO
import matplotlib.pyplot as plt

fasta_file = "results/assembly/scaffolds.fasta"
output_file = "results/plots/contig_length_distribution.pdf"

lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]

plt.figure(figsize=(8, 5))
plt.hist(lengths, bins=20, edgecolor="black")
plt.xlabel("Scaffold length (bp)")
plt.ylabel("Count")
plt.title("Scaffold Length Distribution")
plt.tight_layout()
plt.savefig(output_file)
