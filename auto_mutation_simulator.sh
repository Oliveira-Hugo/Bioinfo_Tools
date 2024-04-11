#!/bin/bash

for (( i=0; i<3; i++ )); do
  output_filename="Res_$i"
  
  command="mutation-simulator -o $output_filename JF357905.fasta args -sn 0.1"
  
  echo "Running: $command"
  
  $command
done

echo "All iterations completed."

