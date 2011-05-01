#!/usr/bin/python3
#-*- coding: utf-8 -*-
import sys
import os

to_convert = {"ಿ": "ೀ", "ೆ":"ೇ", "ೊ":"ೋ"}
broken_dict = {"ೆ":"ೊ"}

def repair_broken(line):
    text = list(line)
    num_letters = len(text)

    i = 0

    output = []
    while i < num_letters:
        # Broken case like u case, example ku 
        if text[i] == "\\" and text[i+1] == "2":
            output += ["ು"]
            i += 2
        # Broken case like kU or Ko case
        elif text[i] == "\\" and text[i+1] == "3":
            if output[-1] in broken_dict:
                output[-1] = broken_dict[text[i - 1]]
            else :
                output += ["ೂ"]
            i += 2
        # Broken case like KRu
        elif text[i] == "\\" and text[i+1] == "4":
            output += ["ೃ"]
            i += 2
        # Broken case like Kai
        elif text[i] == "\\" and text[i+1] == "5":
            output[-1] = "ೈ"
            i += 2                        
        else :
            output += [text[i]] # Normal flow - No change
            i += 1
            
    return "".join(output)



def repair_text(line):
    text = list(line)
    num_letters = len(text)

    i = 0
    output = []
    while i < num_letters:
        # If substitution of letter required
        if text[i] == "\\" and text[i+1] == "1":
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
            f_out.write(repair_text(repair_broken(line)))       

        print ("[OK] processed ", input_file, ", Written ", output_file )
