def remove_gaps(sequence):
  # Remove all '-' characters (gaps) from the sequence
  return sequence.replace('-', '')

def linearize_fasta(fasta_content):
  """Linearizes the FASTA sequence by removing line breaks."""
  lines = fasta_content.splitlines()
  # Skip the first line (usually header)
  sequence = ''.join(lines[1:])
  return sequence

def format_sequence(sequence, width=60):
  # Format the sequence to wrap every 'width' characters and add newline
  formatted_sequence = ''
  for i in range(0, len(sequence), width):
    formatted_sequence += sequence[i:i+width] + '\n'
  return formatted_sequence.strip()  # Remove trailing newline

def process_fasta_file(file_path, width=60):
  """
  Processes a FASTA file: removes gaps, linearizes sequence, and formats lines.
  """
  try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
      # Read the entire FASTA content
      fasta_content = file.read()
  except FileNotFoundError:
    print(f"File not found: {file_path}")
    return None

  # Linearize the FASTA sequence
  sequence = linearize_fasta(fasta_content)

  # Remove gaps from the sequence
  sequence_without_gaps = remove_gaps(sequence)

  # Format the sequence with line breaks every 'width' characters
  formatted_sequence = format_sequence(sequence_without_gaps, width)

  return formatted_sequence

# Specify the FASTA file path
file_path = "/home/hugodpo/JF357905.fasta"

# Process the FASTA file
formatted_sequence = process_fasta_file(file_path)

if formatted_sequence:
  print(formatted_sequence)

