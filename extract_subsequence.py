from Bio import SeqIO

def extract_subsequences(input_file, output_file, start, end):
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            sequence = record.seq[start - 1:end]
            out_handle.write(f">{record.id}\n{sequence}\n")

N = "4"
input_file = f"alignment{N}.fasta"
output_file = f"frag_1.fasta"
start = 5
end = 486

extract_subsequences(input_file, output_file, start, end)

