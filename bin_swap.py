#!/usr/bin/env python3

import sys
import os
import os.path
import argparse


parser = argparse.ArgumentParser(
    prog = 'BIN/CUE Byte swap',
    description = 'Allows you to byte swap only audio tracks in a BIN file. '+
    "This assumes a 16 bit data type and swaps the two 8 bit segments."
    )

parser.add_argument('bin_name', nargs='?')

# Primary function parameters
parser.add_argument('-t', '--time', default=None,
                    help='CUE timestamp of first INDEX to seek to')
parser.add_argument('-s','--seek', default=0, type=int,
                    help='Seek number of frames (u16) into BIN')
parser.add_argument('-o','--output', default=None,
                    help="Output filename")

# Run argument parsing
args = parser.parse_args()

size=0
# Input validation
if args.bin_name is not None:
    size=os.path.getsize(args.bin_name)
    print("Byte swapping ["+args.bin_name+"] ["+str(size)+"] bytes")
else:
    print("ERROR: Please provide a file to byte swap\n")
    parser.print_help()
    sys.exit(1)

seek = int(args.seek)*2

if args.time is not None:
    msf = args.time.split(":")
    seek = int(msf[0])*60*75+int(msf[1])*75+int(msf[2])
    print("Using time ["+args.time+"] as ["+str(seek)+"] frames")

if args.output is not None:
    bin_out = args.output
else:
    bin_out = args.bin_name+"-swap.bin"
print("Output ["+bin_out+"]")


pos=0
with open(args.bin_name, "rb") as r:
    with open(bin_out, "w+b") as w:
        while pos <= size:
            if pos < seek:
                # Direct copy
                w.write(r.read(2))
            else:
                # Direct copy
                hold = r.read(1)
                w.write(r.read(1))
                w.write(hold)


            # Seek to block
            #r.seek(1)
            #w.seek(1)

            pos+=2

