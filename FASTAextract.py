#This script is to extract sequence of your interest from a bigger FASTA into a new file

import sys
import re
import os


if len(sys.argv) !=4:
    print "Usage: python easy_subsetFASTA.py [infile] [outfile] [chrname]"
    sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]
chrname = sys.argv[3]



with open(infile, "r")as fin, open(outfile, "w")as fout:
    newline = ""
    for line in fin:
        newline = newline + str(line)

    split_up = [s.strip() for s in newline.split(">")]

    dict = {}
    for item in split_up:
        if item == "":
            continue
        else:
            fields = item.split("\n")
            ID = fields[0]
            if ID not in dict:
                dict[ID] = item

    print "The original FASTA file has {} sequence(s)".format(len(dict))


    if os.path.isfile(chrname):
        with open(chrname, "r")as fin2:
            list = ()
            for line in fin2:
                if line.strip() in dict:
                    fout.write(">"+dict[line.strip()]+"\n")
                    print "{} has been written into {}".format(dict[line.strip()],outfile)
                else:
                    continue        

    else:

        if chrname in dict:
            fout.write(">")
            fout.write(dict[chrname])
            fout.write("\n")
            print "{} has been written into {}".format(dict[chrname],outfile)
        else:
            print "chromosome not found"
