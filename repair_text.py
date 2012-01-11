#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Repair the misspellings caused by OCR. (Improper Unicode recognized)
# The MIT License (MIT)
# Copyright (c) 2011 Aravinda VK<hallimanearavind@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

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
