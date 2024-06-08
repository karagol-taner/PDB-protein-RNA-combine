def reassign_chain_id(pdb_lines, new_chain_id):
    reassigned_lines = []
    for line in pdb_lines:
        if line.startswith(('ATOM', 'HETATM')):
            line = line[:21] + new_chain_id + line[22:]
        reassigned_lines.append(line)
    return reassigned_lines

def combine_pdb_files(protein_pdb, rna_pdb, output_pdb):
    with open(protein_pdb, 'r') as protein_file, open(rna_pdb, 'r') as rna_file, open(output_pdb, 'w') as outfile:
        protein_lines = protein_file.readlines()
        rna_lines = rna_file.readlines()

        # Reassign chain IDs
        protein_lines = reassign_chain_id(protein_lines, 'A')
        rna_lines = reassign_chain_id(rna_lines, 'B')

        # Write protein lines
        for line in protein_lines:
            outfile.write(line)
        outfile.write('TER\n')

        # Write RNA lines
        for line in rna_lines:
            outfile.write(line)
        outfile.write('TER\nEND\n')

# Example usage
combine_pdb_files('eaa5c.pdb', '5iso2.pred1.min.pdb', 'combined.pdb')
