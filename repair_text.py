#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import os

to_convert = {"ಿ": "ೀ", "ೆ":"ೇ", "ೊ":"ೋ"}

def repair_text(line):
    text = list(line)
    num_letters = len(text)

    i = 0
    output = []
    while i < num_letters:
        # If substitution of letter required
        if text[i] == "|" and text[i+1] == "e":
            if text[ i - 1] in to_convert and len(output) > 0:
                output[-1] = to_convert[text[i - 1]] # change the previous letter
                
            i += 2
        else :
            output += [text[i]] # Normal flow - No change
            i += 1
            
    return "".join(output)




if __name__ == "__main__":
    if len(sys.argv) < 3 :
        print ("[ERROR] Usage: ", sys.argv[0], " input_file output_file")
    else :
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        # Open input file in read only mode
        f = open(input_file, encoding='utf-8', mode='r')

        # Remove the output file if any
        try:
            os.unlink(output_file)
        except:
            print()

        # Open output file in append mode
        f_out = open(output_file, encoding='utf-8', mode='a')

        # Process each line and convert
        for line in f:
            f_out.write(repair_text(line))       

        print ("[OK] processed ", input_file, ", Written ", output_file )
