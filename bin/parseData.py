""" 
    Import packages
"""
import argparse


"""
    Parser
"""
parser = argparse.ArgumentParser(description = "Parse gene names from data.bf file.")
parser.add_argument('-i',
                    '--input',
                    type = str,
                    metavar = '',
                    required = True,
                    help = 'File path to input file.')
parser.add_argument('-o',
                    '--output',
                    type = str,
                    metavar = '',
                    required = True,
                    help = 'File path to output file.')
parser.add_argument('-q',
                    '--question',
                    type = str,
                    metavar = '',
                    required = True,
                    help = 'Question associated with data.')
args = parser.parse_args() 


"""
    Function definitions
"""
def extractGeneSymbols(input_path, output_path, question):
    # Open and read input file
    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    # Extract gene names while ignoring header
    gene_names = [line.split('\t')[0] for line in lines[1: ]]

    # Write gene names to output directory
    with open(output_path, 'w') as outfile:
        # Write the question to the first line of the file
        outfile.write(question + '\n')

        # Write the genes to the file
        for gene in gene_names:
            outfile.write(gene + '\n')


"""
    Main function
"""
if __name__ == '__main__':   
    extractGeneSymbols(args.input, args.output, args.question)