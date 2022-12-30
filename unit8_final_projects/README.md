Unit 8: Final Projects
======================


Here are some possible final projects. Feel free to propose something else. You
are encouraged to work in pairs. Each project below is ranked by difficulty
from low to high.


| Name           | Difficulty | Short Description
|:---------------|:-----------|:---------------------------------------------
| elvish         | 2          | create plausible elvish (or other languages)
| hgt_detector   | 1          | detect horizontal gene transfer
| imeter         | 1          | build the IMEter from scratch
| mRNA2protein   | 1          | find the longest ORF in an mRNA
| pwm_draw       | 2          | draw PWMs as SVGs given FASTA
| old2new        | 1          | convert old sequence data to fastq
| overlaps       | 2          | find the overlap of exons and SNPs, for example
| smith-waterman | 3          | the classic local alignment algorithm
| uncigar        | 2          | convert CIGAR format to pairwise alignment
| viterbi        | 3          | the classic HMM decoder

## elvish ##

When writing fantasy novels, authors must somehow come up with new names that
sound like they come from a different language. Make a language generator using
Nth-order Markov models. For example, generate Evlish words from a mixture of
Finnish and Welsh (or whatever you think Elvish is supposed to look like).

+ Read books (e.g. Gutenberg Project) into tables of letter frequencies
+ Generate new words from the tables of frequencies

## hgt_detector ##

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

## pwm_draw ##

One of the most common ways to represent sequence patterns is the position
weight matrix (PWM). Make a program that reads a file of sequences and outputs
a PWM as an SVG (scalable vector graphic).

+ Download real sequences or make them up yourself (ask for help if needed)
+ Make a PWM data structure (2D list or list of dict)
+ Create SVG (without importing an SVG module)

## old2new ##

Back at the dawn of genome sequencing, Phred quality values were stored as
spaced-delimited integers in FASTA files. Today, quality values are stored as
ASCII characters in FASTQ files. Pretend you are working for a company who has
a lot of old data. Your job is to write a program that converts their old data
into modern FASTQ.

+ Reserarch quality values to understand Phred scores
+ Read in parallel, sequences and qualifty values
+ Write FASTQ

## smith-waterman ##

The Smith-Waterman algorithm is one of the classic bioinformatics algorithms
for finding the maximum scoring local alignment between two sequences. Make a
program that inputs two sequences and outputs the best alignment.
Alternatively, you might do the very similar Needleman-Wunsch algorithm.

+ Provide command line options for match, mismatch, and gap scores
+ Report the score of the maximum alignment
+ Report the aligned sequences

## uncigar ##

The CIGAR format is used to describe pairwise alignment in a compressed format
that isn't very human-readable. Write a program that turns CIGAR strings in
SAM files into something like a BLAST report.

+ Get SAM files from the instructor if you can't find them yourself
+ Learn about CIGAR format and BLAST output
+ Convert CIGAR to BLAST

## viterbi ##

The Viterbi algorithm is used frequently in bioinformatics. For example, it is
used to find protein domains within a protein or to find genes in a genome.
Write a simple Viterbi decoder.

+ Choose a sequence feature to model (ask instructor for help)
+ Decode some real sequences
