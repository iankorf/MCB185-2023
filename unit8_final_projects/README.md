Unit 8: Final Projects
======================

Here are some possible final projects. Feel free to propose something else. You
are encouraged to work in pairs. Each project below is ranked by difficulty (D)
from low (1) to high (5).


| Name                | D | Short Description
|:--------------------|:--|:---------------------------------------------
| animate32           | 1 | animate 32xcoverage.py
| colorname           | 1 | classify the color spectrum
| fasta stats         | 1 | report information about a fasta file
| hgt detector        | 2 | predict horizontal gene transfer
| imeter              | 2 | build the IMEter from scratch
| life                | 2 | re-create Conway's game of life
| mRNA2protein        | 2 | find the longest ORF in an mRNA
| overlaps            | 2 | find the overlap of exons and SNPs, for example
| overlaps fast       | 3 | as above, but much faster
| plausible elvish    | 3 | create new languages
| scoring matrix      | 3 | build your own alignment scoring matrix
| simulate chemotaxis | 4 | make artificial bacteria find food
| smith-waterman      | 4 | the classic local alignment algorithm
| svg pwm             | 4 | draw PWMs as SVGs
| viterbi             | 5 | the classic HMM decoder

## anmiate32 ##

Make a program that visualizes random genome coverage (like 32xcoverage.py).
Use the **Processing** environment to draw images in Python.

+ Download Processing
+ Install Python mode
+ Animate mapping reads to a genome

## colorname ##

The usual representation for colors has 24 bits: 8 bits for each of red, green,
and blue. This creates 16.7 million colors. In practice, we use only a handful
of color names. Create a program that converts any of the 16.7 millon colors to
a list of your favorites by choosing closest matching spectrum.

+ Get the hexcodes for your favorite colors
+ Minimize the distance between an input color and your colors

## fasta stats ##

Write a program the reads in a FASTA file and reports the following
information:

+ Number of sequences
+ Total length
+ Shortest sequence
+ Longest sequence
+ Median sequence length
+ N50 length
+ Composition of each letter in the sequence

## hgt detector ##

One way to find genes that have been recently added to a bacterial genome is to
look for outliers in codon usage. Using a GenBank file for a complete bacterial
genome (e.g. E. coli), compute the average codon usage of a genome and then
compare individual genes to the genome as a whole. Outliers in codon usage bias
could be genes that used to reside in a different genome.

+ Create a codon usage table for the entire genome
+ Compare individual frequencies to the whole genome frequency
+ Use K-L or Manhattan distance for comparisons

## imeter ##

Intron-mediated enhancement (IME) is the general phenomenon that introns
somehow provide a general boost to gene expression. In Rose et al. 2008, the
paper describes a simple method (IMEter) to determine how powerful an intron
is. Recreate the code from the description in the paper.

+ Read the paper
+ Get intron data from instructor (unless you want to try doing this)
+ Train the IMEter with kmer frequencies
+ Test the IMEter with various experimentally-validated introns

## life ##

John Conways game of life is a famous example of cellular automata. Create a
python version of the game/simulation using **Processing**

+ Download Processing
+ Install Python mode
+ Have the user fill the board by clicking with the mouse

## mRNA2protein ##

The public sequence database contains millions of proteins. And yet nobody
really sequences proteins. Instead, they sequence mRNAs and derive the protein
as the longest ORF. Create a program that reads in transcripts and reports the
longest ORF as a protein. The program should optionally report 3-frame or
6-frame translations.

+ Download an mRNA dataset (get help from instructor if needed)
+ Compare your translations to the _official_ translations

## overlaps ##

Genomic features like genes, exons, introns, repeats, SNPs, ChIP-seq peaks,
etc. are generally represented by chrom, begin, end, and sometimes strand.
Given a file of exons and SNPs, for example, find out which exons have SNPs in
them.

+ Make up your own data for testing purposes
+ Get real data from an instructor if needed
+ Output a table of exons and their SNPs

## overlaps fast ##

As above, but write the algorithm so that it runs much faster by indexing
chromosomes and/or positions.

## plausible elvish ##

When writing fantasy novels, authors must somehow come up with new names that
sound like they come from a different language. Make a language generator using
Nth-order Markov models. For example, generate Evlish words from a mixture of
Finnish and Welsh (or whatever you think Elvish is supposed to look like).

+ Read books (e.g. Gutenberg Project) into tables of letter frequencies
+ Generate new words from the tables of frequencies

## scoring matrix ##

Scoring matrices, like BLOSUM and PAM, are created from multiple alignments.
You can create your own scoring matrices. If you want to try something a little
different, you could make a nucleotide scoring matrix rather than using
something like +1 match, -1 mismatch.

+ Get some multiple alignment data (e.g. from PFAM)
+ Count observed changes
+ Create all of the Sij values from log(obs/exp)

## simulate chemotaxis ##

Bacteria move using very simple rules. If the concentration of food is
increasing, they swim straight. Otherwise they tumble. Animate this behavior
using **Processing**.

+ Download Processing
+ Install Python mode
+ Make bacteria find food by swimming straight or tumbling

## smith-waterman ##

The Smith-Waterman algorithm is one of the classic bioinformatics algorithms
for finding the maximum scoring local alignment between two sequences. Make a
program that inputs two sequences and outputs the best alignment.
Alternatively, you might do the very similar Needleman-Wunsch algorithm.

+ Provide command line options for match, mismatch, and gap scores
+ Report the score of the maximum alignment
+ Report the aligned sequences

## svg pwm ##

One of the most common ways to represent sequence patterns is the position
weight matrix (PWM). Make a program that reads a file of sequences and outputs
a PWM as an SVG (scalable vector graphic).

+ Download real sequences or make them up yourself (ask for help if needed)
+ Make a PWM data structure (2D list or list of dict)
+ Create SVG (without importing an SVG module)

## viterbi ##

The Viterbi algorithm is used frequently in bioinformatics. For example, it is
used to find protein domains within a protein or to find genes in a genome.
Write a simple Viterbi decoder.

+ Choose a sequence feature to model (ask instructor for help)
+ Decode some real sequences
