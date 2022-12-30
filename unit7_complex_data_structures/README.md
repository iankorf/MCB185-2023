Unit 7: Complex Data Structures
===============================

## Outline ##

Here are some possible final projects. Feel free to propose something else. You
are encouraged to work in pairs. Each project is ranked in difficulty from


| Name           | Difficulty | Short Description
|:---------------|:-----------|:---------------------------------------------
| seqconverter   | moderate   | convert from old to new sequence formats
|


CIGAR displayer

+ Challenging
	+ Quality Value Converter
	+ Horizontal Gene Transfer
	+ Missing K-mers
	+ Prokaryotic Gene Finding
	+ IMEter
	+ Longest ORF
+ Difficult
	+ IID
	+ Overlaps
	+ PWM
	+ Smith-Waterman
+ Complex
	+ Genome JSON
	+ Plausible Elvish
	+ Viterbi

## Quality Value Converter ##

Back at the dawn of genome sequencing, Phred quality values were stored as
spaced-delimited intgers in FASTA files. Today, quality values are stored as
ASCII characters in FASTQ files. Over the years, there have been different
standards for the ASCII offset. Pretend you are working for a company who has a
lot of old data. Your job is to write a program that converts from old data
formats to new and from new to old.

+ Use

## Horizontal Gene Transfer ##

One way to find genes that have been recently added to a genome is to look for
outliers in codon usage. Using a GenBank file for a complete bacterial genome
(e.g. E. coli), compute the average codon usage of a genome and then compare
individual genes to the genome as a whole. Outliers in codon usage bias could
be genes that used to reside in a different genome.

+ Use regex to parse the GenBank file
+ Store codon usage frequency as dictionaries
+ Compare individual frequencies to the whole genome frequency
+ Use K-L or Manhattan distance for comparisons

## Genome JSON ##

Make a JSON file format that models the structure of genes in a genome.
Chromosomes contain genes. Genes contain transcripts. Transcripts have introns,
exons, UTRs, and coding sequences. It's all very complicated. Once you've
created an elegant model, populate it with some real data using GFF files and
then answer a few questions about the entire genome.

+ Design a JSON structure that encapsulates all of the features
+ Make a program that reads GFF and populates the structure
+ Navigate the structure to produce a histogram of exon lengths, for example

## IID ##

Local alignment statistics are an important model in bioinformatics because
they are used by BLAST. One of the assumptions is that the letters of the
sequences being aligned are IID (independent and identically distributed). How
valid is this assumption? How independent are the letters from each other? How
different is a single protein from the average? How different are single
proteins from each other?

+ Get a large protein dataset (ask instructor for help if needed)
+ Read protein sequences into tables of amino acid frequencies
+ Use Kullback-Leibler or Manhattan distance to compare
+ Create randomly generated proteins as a null model

## IMEter ##

Intron-mediated enhancement (IME) is the general phenomenon that introns
somehow provide a general boost to gene expression. In Rose et al. 2008, the
paper describes a simple method (IMEter) to determine how powerful an intron
is. Recreate the code from the description in the paper.

+ Read the paper
+ Get intron data from instructor (unless you want to try doing this)
+ Train the IMEter with kmer frequencies
+ Test the IMEter with various experimentally-validated introns

## Longest ORF ##

The public sequence database contains millions of proteins. And yet nobody
really sequences proteins. Instead, they sequence mRNAs and derive the protein
as the longest ORF. Create a program that reads in DNA/RNA sequences and
reports the longest ORF as a protein. The program should optionally report
3-frame or 6-frame translations.

+ Create a function that reports all ORFs in a sequence
+ Choose the longest ORF
+ Download an mRNA dataset (get help from instructor if needed)
+ Compare your translations to the _official_ translations

## Missing K-mers ##

Which K-mers are missing in a genome?

## Overlaps ##

Genome data is often described as a feature, which is just a part of a
chromosome with a specific location. An exon is a feature, as is a SNP, or a
ChIP-seq peak. Sometimes people ask "which exons overlap known mutations?"
Write a couple programs that make these comparisons and note the difference in
resources (time, CPU) required.

+ Make a random feature generator
+ Implement some feature comparison functions
	+ Simple lists
	+ Dictionaries
	+ Sorted lists
+ Compare time, memory, and programming effort

## Plausible Elvish ##

When writing fantasy novels, authors must somehow come up with new names that
sound like they come from a different language. Make a language generator using
Nth-order Markov models. For example, generate Evlish words from a mixture of
Finnish and Welsh (or whatever you think Elvish is supposed to look like).

+ Read books (e.g. Gutenberg Project) into tables of letter frequencies
+ Generate new words from the tables of frequencies

## Prokaryotic Gene Finding ##

A convenient way to find genes in prokaryotic genomes is to say that any ORF >
100 aa codes for a protein. But how accurate is this practice? Are there a lot
of fake genes in the genome because of this? Using simulations, how many genes
in a genome are probably not real?

+ Simulate a prokaryotic genome
+ Make a histogram of ORF sizes
+ Use various cutoffs and report the number of fake genes found
+ Estimate the number of fake genes in E. coli (for example)

## PWM ##

One of the most common ways to represent sequence patterns is the position
weight matrix (PWM). Make a program that reads a file of sequences and outputs
a PWM as an SVG (scalable vector graphic).

+ Download real sequences or make them up yourself (ask for help if needed)
+ Make a PWM data structure (2D list or list of dict)
+ Create SVG (without importing an SVG module)

## Smith-Waterman ##

The Smith-Waterman algorithm is one of the classic bioinformatics algorithms
for finding the maximum scoring pair between two sequences. Make a program that
inputs two sequences and outputs the best alignment. Alternatively, you might
do the very similar Needleman-Wunsch algorithm.

+ Provide command line options for match, mismatch, and gap scores
+ Report the score of the maximum alignment
+ Report the aligned sequences

## Viterbi ##

The Viterbi algorithm is used frequently in bioinformatics. For example, it is
used to find protein domains within a protein or to find genes in a genome.
Write a simple Viterbi decoder.

+ Choose a sequence feature to model (ask instructor for help)
+ Decode some real sequences






