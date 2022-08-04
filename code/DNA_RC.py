"""
------------------------------------

  DNA - Reversing & Complementing

------------------------------------
@ Chloé Stévenne    Victor Mangeleer

-------------
Documentation
-------------

This library has for purpose to compute the reverse and 
complement ADN sequence of an input file in FASTA format.

The input files must be placed inside the folder named INPUT
and the output files will be placed automatically inside the
folder named OUTPUT.

"""

import glob
from Bio.Seq import Seq

#----------
# Functions
#----------
# Retreives all the input files' name as a list
def inputFileName():

	# file name with extension
	return glob.glob("input/*.txt")


# Generates all the output files' name as a list
def outputFileName(input_fn):

	# Contains all the outputs name
	outputs_fn = []

	# Generate outputs name
	for i in input_fn:
		outputs_fn.append(i.replace("input/", "output/"))

	return outputs_fn


# Load the different DNA sequences as well as their 
# corresponding FASTA line from a .txt file in FASTA format
def loadSequences(input_file):

	# Opening the file
	with open(input_file) as f:
	    lines = f.readlines()

	# Contains all the DNA sequences
	DNA_sequences = []

	# Contains all the FASTA lines
	FASTA_lines = []

	# Reading all the lines
	for line in lines:
	    
	    # Removes unwanted characters
	    line = line.replace("\n", "")

	    if line[0] == ">":
	    	FASTA_lines.append(line)
	    else:
	    	DNA_sequences.append(line)

	return FASTA_lines, DNA_sequences


# Computes the reverse and complement of a list of DNA sequences
def DNA_ReverseComplement(DNA_sequences):

	# Contains the reversed and complemented sequences
	DNA_sequences_RC = []

	# Computes the RC
	for dna in DNA_sequences:
		DNA_sequences_RC.append(str(Seq(dna).reverse_complement()))

	return DNA_sequences_RC


# Saves the DNA sequences in the output folder
def saveDNA(output_file, DNA_sequences_RC, FASTA_lines):

	# Creation of the output file
	file = open(output_file, 'w')

	# Writting the file
	for i in range(len(DNA_sequences_RC)):

		# Current DNA_RC sequence and its corresponding FASTA line
		DNA = DNA_sequences_RC[i]
		FAS = FASTA_lines[i]

		file.write(FAS + "\n")
		file.write(DNA + "\n")

	file.close()





























