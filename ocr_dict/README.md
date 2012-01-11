# What?

When OCR misspells the text because of inaccuracy in pattern identification or patterns close enough to differenciate. Reads input file and replaces the bad words with good words as mentioned in dict_data.

# How to Use

    perl ocr_dict.pl inp_file out_file

Reads the input file named inp_file and replaces all bad words which are specified in dict_data file in the same folder. Generates out_file.

# Dictionary format

dict_data is a simple text file with bad and good words mapping.

    bad = good

Example format is shown below.

    ಸೂಯ9 = ಸೂರ್ಯ
    ಸೂಯ೯ = ಸೂರ್ಯ
   
