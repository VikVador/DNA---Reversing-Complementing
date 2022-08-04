"""
------------------------------------

	DNA - Reverse & Complementing

------------------------------------
@ Chloé Stévenne    Victor Mangeleer

"""

from DNA_RC import *
from DNA_RC_UI import *

# GUI INTERFACE
DNA_RC_title()
DNA_RC_USAGE()

# 1 - Loading the different files and creating their output name
input_fn  = inputFileName()
output_fn = outputFileName(input_fn)

# Check if files are available
if len(input_fn) == 0:
	print("----- No files were found in the INPUT folder ! ------ \n")
	exit()

# GUI INTERFACE
DNA_RC_FilesFound(input_fn)
DNA_RC_Results()

# 2 - Looping over the files, loading sequences and computing their RC
for i in range(len(input_fn)):

	# Current input and output
	inp = input_fn[i]
	out = output_fn[i]

	FASTA_sequences, DNA_sequences = loadSequences(inp)

	DNA_sequences_RC = DNA_ReverseComplement(DNA_sequences)

	saveDNA(out, DNA_sequences_RC, FASTA_sequences)

	# GUI INTERFACE
	DNA_RC_ShowResults(inp, FASTA_sequences, DNA_sequences, DNA_sequences_RC)

# GUI INTERFACE
DNA_RC_Conversion()
