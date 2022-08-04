"""
------------------------------------

	DNA - Reverse & Complementing

------------------------------------
@ Chloé Stévenne    Victor Mangeleer

-------------
Documentation
-------------

This library has for purpose to create a library
of functions allowing the user to display nicely
all the results obtained

"""

# Defining the colors to display the sequences
class bcolors:
    T       = '\u001b[34;1m' #Black
    A       = '\u001b[31;1m' #Red
    C       = '\u001b[32;1m' #Blue
    G       = '\u001b[33;1m' #Yellow
    RESET   = '\033[0m' #RESET COLOR

# Used to split a word into multiple letters
def split(word):
    return list(word)

# Used to color a DNA sequence over terminal
def DNA_RC_ColorSequence(seq):

	# Splitting the sequences into a list of bases
	DNA_split = split(seq)

	# New colored string
	DNA_colored = ""

	for l in DNA_split:

		if l == "T":
			DNA_colored = DNA_colored + bcolors.T + "T" + bcolors.RESET
		elif l == "A":
			DNA_colored = DNA_colored + bcolors.A + "A" + bcolors.RESET
		elif l == "C":
			DNA_colored = DNA_colored + bcolors.C + "C" + bcolors.RESET
		else:
			DNA_colored = DNA_colored + bcolors.G + "G" + bcolors.RESET

	return(DNA_colored)

def DNA_RC_title():

	print("\n")
	print("	o O       o O       o O       o O")
	print("     o | | O   o | | O   o | | O   o | | O")
	print("   O | | | | O | | | | O | | | | O | | | | O")
	print("  O-oO | | o   O | | o   O | | o   O | | oO-o")
	print(" O---o O o       O o       O o       O o O---o")
	print("O-----O                                 O-----o")
	print("o-----O                                 o-----O")
	print(" o---O   DNA - Reverse and complement    o---O")
	print("  o-O                                     o-O")
	print("   O      Chloé Stévenne                   O")
	print("  O-o					  o-0")
	print("  O--o                 &                   O--O")
	print(" O---o                                    O---o")
	print("O-----o               Victor Mangeleer   O-----o")
	print("o-----O                                 o-----O")
	print(" o---O o O       o O       o O       o O o---O")
	print("  o-Oo | | O   o | | O   o | | O   o | | Oo-O")
	print("   O | | | | O | | | | O | | | | O | | | | O")
	print("     O | | o   O | | o   O | | o   O | | o")
	print("       O o       O o       O o       O o")
	print("\n\n")

def DNA_RC_USAGE():

	print("---------\n")
	print("  USAGE  \n")
	print("---------\n")

	print("All the files in FASTA format that must be converted should")
	print("be placed inside the folder named INPUT. The output file will")
	print("be automatically placed inside the OUTPUT folder using the same")
	print("name as the one for the input.\n\n\n")


def DNA_RC_FilesFound(input_fn):

	print("----------------\n")
	print("  FILE(S) FOUND  \n")
	print("----------------\n")
	
	for inp in input_fn:
		print("---> " + inp.replace("input/", "") + "\n")

def DNA_RC_Results():

	print("\n\n-------------\n")
	print("   RESULTS   \n")
	print("-------------\n")

def DNA_RC_ShowResults(input_file, FASTA_seq, DNA_seq, DNA_seq_RC):

	print("---------- File = " + input_file.replace("input/", "") + " ---------- \n")

	for i in range(len(DNA_seq)):

		print(FASTA_seq[i] + "\n")
		print(DNA_RC_ColorSequence(DNA_seq[i]) + "\n")
		print(DNA_RC_ColorSequence(DNA_seq_RC[i]) + "\n\n\n\n")

def DNA_RC_Conversion():

	print("----------\n")
	print("  SAVING  \n")
	print("----------\n")
	print("Done")














