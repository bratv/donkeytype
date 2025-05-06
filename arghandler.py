# This is temp file that holds input parsing code that will eventually
# be used in the Typing commandline CLI program.

import argparse
import sys
import start

programName = 'donkeytype'
helpLower = 'lowercase letters'
helpUpper = 'uppercase letters'
helpSymbols = 'symbols'
helpNumber = 'NUMBER of keypresses before test ends'
helpLetters = 'userdefined set of letters and or symbols to excersize'
description ="""This is a program that lets you practice your typing skills.
You are supposed to type the last letter that shows up in the upper row
of letters and what you have typed will show in a lower row of previously 
typed letters. It also marks what letters you typed wrong and shows basic
stats on exit. Press Esc when you want to finish."""

parser = argparse.ArgumentParser(prog=programName, description=description)
parser.add_argument('-l','--lower-case',action='store_true',help=helpLower)
parser.add_argument('-u','--upper-case',action='store_true',help=helpUpper)
parser.add_argument('-s','--symbols',action='store_true',help=helpSymbols)
parser.add_argument('-n','--number',type=int,default=10,help=helpNumber)
parser.add_argument('letters',nargs='*',default='',help=helpLetters)

the_args = parser.parse_intermixed_args(sys.argv)

lower = the_args.lower_case
upper = the_args.upper_case
number = the_args.number
symbols = the_args.symbols
custom = []

if len(the_args.letters) > 1:
    custom = list(the_args.letters[1])

print(lower,upper,symbols,custom)
start.init(upper,lower,symbols,custom,number)
start.main()


