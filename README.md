________________________________________
Antibody-Antigen Contact Finder 🔬
A collection of simple yet powerful scripts for PyMOL and UCSF ChimeraX to identify, visualize, and export contact residues at the interface between antibody chains (heavy and light) and a target protein/antigen.
These scripts automate the tedious process of finding an interaction footprint, saving the results to a clean text file for analysis, and highlighting the interface directly in the viewer.
________________________________________
Features ✨
•	Dual Software Support: Provides scripts for both popular molecular viewers, PyMOL and ChimeraX.
•	Multi-Chain Analysis: Easily define multiple antibody chains (e.g., Heavy and Light) to find contacts against a single antigen chain.
•	Customizable Cutoff: Define what constitutes a "contact" by setting a custom distance cutoff in angstroms ($Å$).
•	Clean Data Export: Automatically generates a formatted .txt file listing the contact residues for each chain, perfect for documentation or further analysis.
•	Automatic Visualization: The scripts color and highlight the identified contact residues, providing an immediate visual representation of the binding interface.
•	Water Removal: The PyMOL script automatically removes solvent molecules to ensure the analysis is focused on protein-protein interactions.
________________________________________
Prerequisites
You need to have one of the following molecular visualization programs installed:
•	PyMOL (A user-sponsored molecular visualization system)
•	UCSF ChimeraX (Free for academic use)
________________________________________
🚀 Usage
PyMOL Script (find_contacts.py)
The PyMOL script is a self-contained Python function.
1. Configure the Script
Open the find_contacts.py file in a text editor and modify the parameters in the "Parameters to Customize" section at the bottom of the file.
Python
# --- Parameters to Customize ---
PDB_FILE_PATH = "path/to/your/structure.pdb"  # e.g., "1abc.pdb" or "/Users/me/Desktop/1abc.pdb"
ANTIBODY_CHAIN_IDS = ["H", "L"]  # Provide both Heavy and Light chain IDs here
PROTEIN_CHAIN_ID = "A"
DISTANCE = 4.5 # Distance in Angstroms
OUTPUT_FILENAME = "contacts_HL_output.txt"
•	PDB_FILE_PATH: The full path to your PDB or mmCIF structure file.
•	ANTIBODY_CHAIN_IDS: A Python list of the chain IDs for your antibody (e.g., ["H", "L"]).
•	PROTEIN_CHAIN_ID: The chain ID for the target antigen.
•	DISTANCE: The distance cutoff in angstroms ($Å$) to define a contact. 4.0-5.0 Å is a common range.
•	OUTPUT_FILENAME: The name of the text file where results will be saved.
2. Run the Script
There are two ways to run the script in PyMOL:
1.	Recommended Method (Run Script File):
o	In the PyMOL top menu, go to File > Run Script....
o	Navigate to and select your edited find_contacts.py file.
2.	Alternative Method (Paste into Console):
o	Copy the entire contents of the find_contacts.py file.
o	Paste it directly into the PyMOL command console and press Enter.
The script will execute, and a confirmation message will appear in the console. The contact residues will be colored yellow/orange (antibody) and cyan (protein) and displayed as sticks.
ChimeraX Script (find_contacts.cxc)
The ChimeraX script is a series of commands that can be run directly.
1. Configure the Script
Open the find_contacts.cxc file in a text editor and modify the parameters and command lines as needed. Note: You must open your PDB file in ChimeraX before running the script.
Code snippet
# --- Parameters to Edit ---
let distance = 4.5
let output_file = ~/Desktop/chimerax_contacts_HL.txt # ‼️ USE A FULL/ABSOLUTE PATH

# --- Script Commands ---
select clear

# ‼️ EDIT THIS LINE with your model number and chain IDs (e.g., #1/H,L and #1/A)
zone #1/H,L ${distance} #1/A

# ... (edit the model/chain IDs in the listr commands as well)
log cmd "\n## Antibody Heavy Chain (H) Contacts:"
listr sel & #1/H attr resname,number log true # ‼️ EDIT #1/H

log cmd "\n## Antibody Light Chain (L) Contacts:"
listr sel & #1/L attr resname,number log true # ‼️ EDIT #1/L

# ... and so on
•	Important: Replace #1 with the correct model number of your structure in ChimeraX. Replace H, L, and A with your chain IDs in all the indicated lines.
•	output_file: You must provide a full (absolute) path where the file will be saved. ~/ is a shortcut for your home directory on Mac/Linux.
2. Run the Script
1.	First, open your PDB file in ChimeraX (e.g., open 1abc).
2.	In the ChimeraX command line, type open followed by the path to your saved find_contacts.cxc script and press Enter.
3.	open /path/to/your/find_contacts.cxc
The script will highlight the interface and generate the output file at the specified path.
________________________________________
Example Output (contacts_HL_output.txt)
The generated text file will be clearly formatted like this:
# Contact Residues within 4.5 Å
# Structure: path/to/your/structure.pdb

## Antibody Chain (H) Contact Residues:
PHE27
TRP33
HIS99
TYR101
ASP102

## Antibody Chain (L) Contact Residues:
TYR32
TYR49
PHE91
TRP96

## Protein Chain (A) Contact Residues:
ARG55
GLU58
LYS121
PRO122
PRO124
TYR125
________________________________________
Contributing 🤝
Found a bug or have an idea for an improvement? Feel free to open an issue or submit a pull request!
License
This project is licensed under the MIT License. See the LICENSE file for details.

