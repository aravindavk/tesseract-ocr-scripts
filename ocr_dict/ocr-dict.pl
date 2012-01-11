#!/usr/bin/perl
# OCR dictionary
# The MIT License (MIT)
# Copyright (c) 2012 Aravinda VK<hallimanearavind@gmail.com>

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

use File::Slurp;

# If required number of arguments not given(-1 is file name, 0 is first, 1 is second)
if ($#ARGV != 1 ) {
	print "usage: perl ocr-dict.pl in_file out_file\n";
	exit;
}

# Open input file and copy data
open FILE, $ARGV[0] or die "Couldn't open file: $!";
my $text = <FILE>;
close FILE;

$dict_file = 'dict_data';
open (F, $dict_file) || die ("Could not open $dict_file!");

# Replace each bad word
while ($line = <F>){
  ($key,$value) = split '=', $line;

  # Trim
  $key =~ s/^\s+//;
  $key =~ s/\s+$//;
  $value =~ s/^\s+//;
  $value =~ s/\s+$//;
  
  # Replace the bad words
  $text =~ s/$key/$value/g;
}

close (F);

# Write to output file
open FILE, ">", $ARGV[1] or die "Couldn't open file: $!";
print FILE $text;
close FILE;
print "[OK] Generated ", $ARGV[1], " \n"; 
