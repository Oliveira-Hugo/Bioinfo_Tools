def process_fasta_header(header):
    """
    Processes a FASTA header to retain only the accession code.
    
    Args:
    header (str): The FASTA header line to be processed.
    
    Returns:
    str: The processed header containing only the accession code.
    """
    # Split the header by the '|' character
    parts = header.split('|')
    
    # The accession code is expected to be the second part in the given format
    if len(parts) > 1:
        return parts[1].split()[0]
    else:
        # If there's no '|' in the header, return the whole header
        return header.split()[0]

def process_fasta_file(input_file, output_file):
    """
    Processes a FASTA file to retain only the accession code in the headers.
    
    Args:
    input_file (str): Path to the input FASTA file.
    output_file (str): Path to the output FASTA file with processed headers.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # Process the header line
                new_header = process_fasta_header(line)
                outfile.write('>' + new_header + '\n')
            else:
                # Write the sequence lines as-is
                outfile.write(line)

# Example usage
input_file = '/home/hugodpo/Downloads/BVBRC_DENV_genomes_2024.fasta'
output_file = '/home/hugodpo/Downloads/BVBRC_DENV_genomes_2024_nometadata.fasta'
process_fasta_file(input_file, output_file)

