import matplotlib.pyplot as plt
from Bio import SeqIO

def plot_alignment(records, start, end, ax):
    colors = {"a": "#77DD77", "c": "#FFFF66", "g": "#FF6961", "t": "#ADD8E6", "n": "black"}
    max_segment_length = max(end - start, 50) 
    for i, record in enumerate(records):
        segment = record.seq[start - 1:end]
        ax.text(0, -i, record.id, ha='left', va='center')
        for j, base in enumerate(segment):
            color = colors.get(base.lower(), "black")  # Change 'lower' to 'upper' accordingly
            x_coordinate = j * (50 / max_segment_length) + 5  # '5' determines the horizontal start spacing of the alignment from the plot
            ax.text(x_coordinate, -i, base, ha='left', va='center', backgroundcolor=color)

nt_alignment = "/prj/posgrad/hugodpo/Documentos/LABINFO/alignment4.fasta"
start, end = 5, 486
interval_length = 250
num_figures = (end - start) // interval_length + 1

records = list(SeqIO.parse(nt_alignment, "fasta"))

for fig_num in range(num_figures):
    fig_start = start + fig_num * interval_length
    fig_end = min(fig_start + interval_length - 1, end)
    
    segments = [(i, min(i + 49, fig_end)) for i in range(fig_start, fig_end + 1, 50)]

    fig, axes = plt.subplots(len(segments), 1, figsize=(10, len(segments)*2))
    for i, (seg_start, seg_end) in enumerate(segments):
        ax = axes[i]
        ax.set_title(f"Segment {i+1}: {seg_start}-{seg_end}")
        
        plot_alignment(records, seg_start, seg_end, ax)
        
        ax.set_xlim(0, 50)
        ax.set_ylim(-len(records), 1)
        ax.axis("off")

    plt.tight_layout()
    plt.show()
