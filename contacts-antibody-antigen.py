from pymol import cmd
import collections

def find_ab_contacts_multichain(pdb_file, antibody_chains, protein_chain, distance_cutoff=4.0, output_file="contact_residues_multi.txt"):
    """
    Identifies and exports contact residues between multiple antibody chains (e.g., heavy and light) 
    and a protein chain, after removing water.
    """
    # Load the structure
    cmd.delete("all")
    cmd.load(pdb_file)

    # 💧 REMOVE WATER MOLECULES (HOH, WAT, etc.)
    cmd.remove("solvent")

    # Define the protein chain selection
    prot_selection = f"chain {protein_chain}"
    
    # This will store the results, e.g., {'H': {('TYR', '101')}, 'L': {('SER', '32')}}
    ab_contacts_by_chain = collections.defaultdict(set)
    
    # --- Logic for finding Antibody contacts ---
    # Loop through each provided antibody chain
    for chain_id in antibody_chains:
        ab_chain_selection = f"chain {chain_id}"
        
        # Define a unique name for the selection of contacts for this specific chain
        ab_contacts_sel_name = f"ab_contacts_{chain_id}"
        
        # Select residues in this antibody chain that are near the protein
        cmd.select(ab_contacts_sel_name, f"({ab_chain_selection}) within {distance_cutoff} of ({prot_selection})")
        
        # Use iterate to get the residue info and add it to our dictionary
        cmd.iterate(ab_contacts_sel_name, f"ab_contacts_by_chain['{chain_id}'].add((resn, resi))", space=locals())

    # --- Logic for finding Protein contacts ---
    # First, create a combined selection of all antibody chains
    combined_ab_selection = f"chain {','.join(antibody_chains)}"
    prot_contacts_sel = "prot_contacts"
    cmd.select(prot_contacts_sel, f"({prot_selection}) within {distance_cutoff} of ({combined_ab_selection})")
    
    prot_residues = set()
    cmd.iterate(prot_contacts_sel, "prot_residues.add((resn, resi))", space=locals())
    
    # --- Writing Output File ---
    with open(output_file, "w") as f:
        f.write(f"# Contact Residues within {distance_cutoff} Å\n")
        f.write(f"# Structure: {pdb_file}\n\n")
        
        # Write the contacts for each antibody chain
        for chain_id in antibody_chains:
            f.write(f"## Antibody Chain ({chain_id}) Contact Residues:\n")
            sorted_ab_residues = sorted(list(ab_contacts_by_chain[chain_id]), key=lambda x: int(x[1]))
            if not sorted_ab_residues:
                f.write("None\n")
            else:
                for resn, resi in sorted_ab_residues:
                    f.write(f"{resn}{resi}\n")
            f.write("\n")

        # Write the contacts for the protein chain
        f.write(f"## Protein Chain ({protein_chain}) Contact Residues:\n")
        sorted_prot_residues = sorted(list(prot_residues), key=lambda x: int(x[1]))
        if not sorted_prot_residues:
            f.write("None\n")
        else:
            for resn, resi in sorted_prot_residues:
                f.write(f"{resn}{resi}\n")

    print(f"✅ Contact analysis complete. Results saved to '{output_file}'.")

    # --- Visualization ---
    colors = ["yellow", "orange", "palegreen", "lightpink"]
    for i, chain_id in enumerate(antibody_chains):
        cmd.color(colors[i % len(colors)], f"ab_contacts_{chain_id}")
        cmd.show("sticks", f"ab_contacts_{chain_id}")

    cmd.color("cyan", prot_contacts_sel)
    cmd.show("sticks", prot_contacts_sel)
    cmd.zoom(f"({prot_contacts_sel} or {combined_ab_selection})")


# --- HOW TO USE ---
# 1. Change the parameters below.
# 2. Save as a .py file and run in PyMOL via File > Run Script...

# --- Parameters to Customize ---
PDB_FILE_PATH = r"path"  # e.g., "1abc.pdb"
ANTIBODY_CHAIN_IDS = ["A", "C"]  # Provide both Heavy and Light chain IDs here
PROTEIN_CHAIN_ID = "F"
DISTANCE = 3.5
OUTPUT_FILENAME = "contacts_HL_output.txt"

# --- Run the function ---
find_ab_contacts_multichain(PDB_FILE_PATH, ANTIBODY_CHAIN_IDS, PROTEIN_CHAIN_ID, DISTANCE, OUTPUT_FILENAME)